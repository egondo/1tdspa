arq = open("exemplo1.py", mode="r")

conteudo = arq.read()

arq.close()  #fechando o arquivo

print(conteudo)