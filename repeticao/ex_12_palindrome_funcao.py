def inverte(numero: int) -> int:
    resposta = 0
    while numero != 0:
        dig = numero % 10
        resposta = resposta * 10 + dig
        numero //= 10
    return resposta


num = int(input("Digite um nº: ")) #º = alt+167

invertido = inverte(num)
print(invertido)
if num == invertido:
    print(f'{num} é palindromo')
else:
    print(f'{num} não é palindromo')