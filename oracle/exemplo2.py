import oracledb

conn = oracledb.connect(user='pf0313', password='professor#23', dsn="oracle.fiap.com.br/orcl")

rem = input("Rementente: ")
dest = input("Destinatario: ")
assunto = input("Assunto: ")
conteudo = input("MSG: ")

dado = {"remetente": rem, "para": dest, "assunto": assunto, "conteudo": conteudo}

sql = "INSERT INTO T_PS_MENSAGEM(assunto, conteudo, remetente, destinatario) VALUES(:assunto, :conteudo, :remetente, :para)"

cur = conn.cursor()
cur.execute(sql, dado)

#executando commit
conn.commit()

cur.close()
conn.close()