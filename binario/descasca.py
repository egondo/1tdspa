numero = int(input("Informe o numero: "))

while numero != 0:
    digito = numero % 10
    print(digito)
    numero = numero // 10
