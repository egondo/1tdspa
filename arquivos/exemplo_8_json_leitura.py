import json

arq = open("pacientes.json", mode="r")

lista = json.load(arq)
for item in lista:
    print(type(item), item)

arq.close()
