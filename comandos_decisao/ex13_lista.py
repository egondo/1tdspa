dia = int(input("Dia: "))
mes = int(input("Mês: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print(f"{dia}/{mes}: Data inválida")
    quit() #encerra o programa

if mes == 2 and dia > 28:
    print(f"{dia}/{mes}: Data inválida")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 31:
    print(f"{dia}/{mes}: Data inválida")
else:
    print(f"{dia}/{mes}: Data válida")