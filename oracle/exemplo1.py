import oracledb

#criar conexao com o banco
conn = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

#print(conn.version)
#abrindo cursor: comunicar com o banco
cur = conn.cursor()
cur.execute("SELECT * FROM T_PS_MENSAGEM")
rows = cur.fetchall()

for reg in rows:
    print(reg)

cur.close()
conn.close()

