binario = int(input("Binário: "))

aux = binario
soma = 0
pot2 = 1

while binario != 0:
    digito = binario % 10
    soma = soma + digito * pot2
    binario = binario // 10
    pot2 = pot2 * 2

print(f"({aux}) => ({soma})")