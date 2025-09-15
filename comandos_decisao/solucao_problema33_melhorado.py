num_a = float(input("Digite um número: "))
op = input("Operador (+-/*): ")
num_b = float(input("Digite um número: "))
fez_conta = True

if op == '+':
    resultado = num_a + num_b
elif op == '-':
    resultado = num_a - num_b
elif op == '*':
    resultado = num_a * num_b
elif op == '/':
    #Teste se o num_b é diferente de zero
    resultado = num_a / num_b
else:
    print("Operador inválido!")
    #quit() -> encerra o programa
    fez_conta = False

if fez_conta:
    print(f"{num_a} {op} {num_b} = {resultado:.3f}")



