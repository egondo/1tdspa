#Escreva um algoritmo que transforma de binário para decimal

binario = int(input("Informe o número binário"))
soma = 0
pot2 = 1   #variavel que armazenara as potencias de 2

while binario != 0:
    digito = binario % 10
    soma = soma + digito * pot2
    binario = binario // 10
    pot2 = pot2 * 2

print(f"Decimal: {soma}")