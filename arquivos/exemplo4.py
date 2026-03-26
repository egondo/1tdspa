lista = [
    "Computational Thinking",
    "Domain Driven Design",
    "Building Relational Database",
    "Front End Design Engineering",
    "AI & Chatbot",
    "Software Engineering and Business Model"
]

#for i in range(len(lista)):
#    lista[i] = lista[i] + "\n"

outra_lista = [item + "\n" for item in lista]

#outra_lista = []
#for item in lista:
#    outra_lista.append(item + "\n")

with open("disciplinas.data", mode="w") as file:
    file.writelines(outra_lista)

print("Gravado com sucesso!")