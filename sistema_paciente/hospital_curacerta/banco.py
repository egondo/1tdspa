import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

def rec_id_visita_senha(senha: int) -> dict:
    sql = "SELECT id_visita FROM t_ps_visita WHERE senha = :senha AND saida IS NULL ORDER BY chegada DESC"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"senha": senha})
            reg = cur.fetchone()
            if reg:
                return reg[0]
            else:
                raise Exception(f"Nenhuma visita encontrada com senha {senha}")


def altera_visita(visita: dict):
    sql = "UPDATE T_PS_VISITA SET batimentos=:batimentos, temperatura=:temperatura, pressao=:pressao, alergia=:alergia, sintomas=:sintomas, observacao=:obs WHERE id_visita=:id_visita"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, visita)
        conn.commit()



def rec_id_paciente_senha(senha: int) -> int:
    sql = "SELECT id_paciente FROM T_PS_VISITA WHERE senha = :senha ORDER BY id_visita DESC"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"senha": senha})
            reg = cur.fetchone()
            if reg == None:
                raise Exception("Não existe pessoa associada a senha")
            return reg[0]
            
def altera_paciente(paciente: dict):
    sql = "UPDATE T_PS_PACIENTE SET nome=:nome, cpf=:cpf, convenio=:convenio, telefone=:telefone, nascimento=to_date(:nascimento, 'DD-MM-YYYY') WHERE id_paciente=:id_paciente"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, paciente)
        conn.commit()
    
def insere_procedimento(proc: dict):
    sql = "INSERT INTO t_ps_procedimento(id_visita, descricao, hora, id_funcionario) values(:id_visita, :descricao, to_date(:hora, 'DD-MM-YYYY HH24:MI'), :id_funcionario)"    
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, proc)
        conn.commit()




#recupera paciente pelo cpf
def rec_paciente_cpf(cpf: str) -> dict:
    sql = "SELECT id_paciente, nome, nascimento FROM t_ps_paciente WHERE cpf = :cpf"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"cpf": cpf})
            registro = cur.fetchone()
            if registro == None:
                return None
            else:
                pac = {"id_paciente": registro[0], "nome": registro[1], "nascimento": registro[2], "cpf": cpf}
            return pac

#fazer a consulta da sequence S_PS_SENHA
def rec_senha() -> int:
    sql = "SELECT s_ps_senha.nextval FROM dual"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            resultado = cur.fetchone()
            return resultado[0]

def insere_paciente(paciente: dict):
    sql = "INSERT INTO t_ps_paciente(nome, telefone, convenio, cpf, nascimento) VALUES(:nome, :telefone, :convenio, :cpf, to_date(:nascimento, 'DD-MM-YYYY')) RETURNING ID_PACIENTE INTO :id_paciente"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            new_id = cur.var(oracledb.NUMBER) #criando obj para armazenar o id
            paciente['id_paciente'] = new_id
            cur.execute(sql, paciente)
            paciente['id_paciente'] = new_id.getvalue()[0] #colocando o id gerado pelo banco no dicionario que foi passado como parametro
        conn.commit()

def insere_visita(visita: dict):
    sql = "INSERT INTO t_ps_visita(id_paciente, chegada, senha) values(:id_paciente, to_date(:chegada, 'DD-MM-YYYY HH24:MI'), :senha)"    
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, visita)
        conn.commit()


if __name__ == "__main__":
    valor = rec_senha()
    pac = rec_paciente_cpf('000')
    pac2 = rec_paciente_cpf('001')

    print(f'Valor: {valor}')
    print(f'Pac1: {pac}')
    print(f'Pac2: {pac2}')
