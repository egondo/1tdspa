import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

if __name__ == "__main__":
    nome = input("Nome: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    telefone = input("Telefone: ")
    convenio = input("Convenio: ")

    pac = {'nome': nome, "nasc": nascimento, "tel": telefone, "convenio": convenio}

    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO T_PS_PACIENTE(nome, telefone, convenio, nascimento) VALUES(:nome, :tel, :convenio, to_date(:nasc, 'DD-MM-YYYY'))"

            cur.execute(sql, pac)
        
        con.commit()
    
    print("Paciente incluido com sucesso!")
    