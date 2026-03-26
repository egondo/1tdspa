herois = [
    "Capitão América",
    "Hulk",
    "Capitã Marvel",
    "Homem de Ferro",
    "Homem Aranha",
    "Homem Formiga",
    "Thor",
    "Guardiões da Galáxia",
    "Doutor Estranho",
    "Thanos",
    "Surfista Prateado",
    "Viúva Negra"
]

arq = open("lutas.txt", mode="w")

for i in range(len(herois)):
    for j in range(i+1, len(herois)):
        arq.write(f"{herois[i]} VS {herois[j]}\n")

arq.close()
print("Gravacao de arquivo com sucesso")