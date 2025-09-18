import math

num = float(input("Digite um número: "))

if num >= 0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} vale {raiz}")
else:
    print("Não é possível extrair raiz quadrada de número negativo")
