dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1582:
    print(f"{dia}/{mes}/{ano}: Data inválida")
    quit() #encerra o programa

if mes == 2 and dia > 28:
    if dia == 29:
        if ano % 400 == 0:
            print(f"{dia}/{mes}/{ano}: Data válida")
        elif ano % 100 == 0:
            print(f"{dia}/{mes}/{ano}: Data inválida")
        elif ano % 4 == 0:
            print(f"{dia}/{mes}/{ano}: Data válida")
        else:
            print(f"{dia}/{mes}/{ano}: Data inválida")

    else:
        print(f"{dia}/{mes}/{ano}: Data inválida")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 31:
    print(f"{dia}/{mes}/{ano}: Data inválida")
else:
    print(f"{dia}/{mes}/{ano}: Data válida")