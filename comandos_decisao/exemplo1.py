salario = float(input("Salario: "))
sal_min = 1518.00
qtd = salario / sal_min

if qtd > 10:
    print("Puxa vida, vc ganha bem!")
    print("......")

print(f"Seu salário de {salario} equivale a {qtd} de salários mínimos")


