import oracledb

conn = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

print("Alterando remetente da msg:")
id_mensagem = input("ID: ")
novo_rem = input("Remetente: ")

sql = f"UPDATE T_PS_MENSAGEM SET remetente = :novo_rem WHERE Destinatario=:dest"

cur = conn.cursor()
cur.execute(sql, {"novo_rem": novo_rem, "dest": id_mensagem})
conn.commit()
cur.close()
conn.close()