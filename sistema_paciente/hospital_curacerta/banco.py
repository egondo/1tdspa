import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

#recupera paciente pelo cpf
def rec_paciente_cpf(cpf: str) -> list:
    sql = "SELECT id_paciente, nome FROM t_ps_paciente WHERE cpf = :cpf"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"cpf": cpf})
            return cur.fetchone()

#fazer a consulta da sequence S_PS_SENHA
def rec_senha() -> int:
    sql = "SELECT s_ps_senha.nextval FROM dual"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            resultado = cur.fetchone()
            return resultado[0]

def insere_paciente(paciente: dict):
    sql = "INSERT INTO t_ps_paciente(nome, telefone, convenio, cpf, nascimento) values(:nome, :telefone, :convenio, :cpf, to_date(':nascimento', 'DD-MM-YYYY'))"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, paciente)
        conn.commit()

def insere_visita(visita: dict):
    sql = "INSERT INTO t_ps_visita(id_paciente, chegada) values(:id_paciente, to_date(':chegada', 'DD-MM-YYYY HH24:MI'))"    
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
