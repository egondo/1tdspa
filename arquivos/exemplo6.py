with open("feira.txt", mode="a") as arq:
    arq.write("\n")
    prod = ["Pimentão", "Pastel", "Mandioca", "Caldo de Cana"]
    for item in prod:
        arq.write(item)
        arq.write("\n")

print("Final da feira")