num_a = float(input("Digite um número: "))
op = input("Operador (+-/*): ")
num_b = float(input("Digite um número: "))

if op == '+':
    resultado = num_a + num_b
    print("Resultado=", resultado)
elif op == '-':
    resultado = num_a - num_b
    print("Resultado=", resultado)
elif op == '*':
    resultado = num_a * num_b
    print("Resultado=", resultado)
elif op == '/':
    #Teste se o num_b é diferente de zero

    resultado = num_a / num_b
    print("Resultado=", resultado)
else:
    print("Operador inválido!")