binario = int(input("binario: "))
soma = 0
pot2 = 1

while binario != 0:
    dig = binario % 10
    soma = soma + dig * pot2
    binario = binario // 10
    pot2 = pot2 * 2

