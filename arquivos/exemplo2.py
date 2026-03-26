with open("feira.txt", mode="r") as arq:
    produtos = arq.readlines()

print(produtos)

for item in produtos:
    print(item.strip())