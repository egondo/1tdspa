nota1 = float(input("Digite a nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida! Digite novamente: "))

#print(f"A 1 nota informada foi {nota1}")

nota2 = float(input("Digite a nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida! Digite novamente: "))

media = (nota1 + nota2) / 2
print(f"A media é {media}")
