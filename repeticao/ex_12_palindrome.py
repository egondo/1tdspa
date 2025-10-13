num = int(input("Digite um nº: ")) #º = alt+167

aux_num = num
invertido = 0   #soma ou acumulador
while aux_num != 0:
    dig = aux_num % 10
    invertido = invertido * 10 + dig
    aux_num = aux_num // 10

if num == invertido:
    print(f'{num} é palindromo')
else:
    print(f'{num} não é palindromo')