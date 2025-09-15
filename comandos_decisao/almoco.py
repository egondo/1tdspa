dia_semana = input("Informe o dia da semana: ")

match dia_semana:
    case 'segunda':
        print("Virado a Paulista")
    case 'terça':
        print("Dobradinha ou filé à parmeggiana")
    case 'quarta':
        print("Feijoada")
    case 'quinta':
        print("Massa")
    case 'sexta': 
        print('Peixe')
    case "sabado":
        print('Pizza')
    case _:
        print("Almoço da mãe ou da avó")