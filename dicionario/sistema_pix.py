def menu() -> int:
    print('1 cadastra')
    print('2 consulta')
    opcao = int(input("Informe uma opção: "))
    return opcao

def coleta_dados() -> dict:
    chave = input("Chave pix: ")
    tipo = input("Tipo (tel, email, cpf,...): ")
    nome = input("Nome: ")
    banco = input("Banco: ")
    agencia = input("Agencia: ")
    numero = input("Numero: ")
    dic = {
        "chave": chave, 
        "tipo": tipo, 
        "nome": nome, 
        "banco": banco, 
        "agencia": agencia, 
        "numero": numero
        }
    return dic


#programa principal
opcao = 0
armazenamento_pix = {} 
while opcao != 3:
    opcao = menu()
    if opcao == 1:
        info = coleta_dados()
        chave = info['chave']
        if not chave in armazenamento_pix:
            armazenamento_pix[chave] = info
            print("Cadastro feito com sucesso!")
        else:
            print("Cadastro nao efetuado, chave ja existe")
    elif opcao == 2:
        info = coleta_dados()
        chave = info['chave']
        if chave in armazenamento_pix:
            armazenamento_pix[chave] = info
            print("Alteração feita com sucesso!")
        else:
            print("Chave pix nao encontrada")
    elif opcao == 3:
        print("Saindo do sistema")
    else:
        print("Opção inválida!")