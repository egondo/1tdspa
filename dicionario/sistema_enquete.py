'''Criar um sistema de perguntas e (talvez) respostas com as seguintes funcionalidades:
a) cadastra pergunta (inserir, alterar e excluir)
b) exibir as perguntas
c) aplicar as perguntas cadastradas com o objetivo de capturar as respostas'''

def menu():
    print('1 - cadastra pergunta')
    print('2 - altera pergunta')
    print('3 - exclui pergunta')
    print('4 - listar perguntas')
    print('5 - aplicar as perguntas')
    print('6 - sair')
    return int(input("Opcao: "))

def monta_pergunta() -> dict:
    print('PERGUNTA MONTAGEM: ')
    num = int(input("Número da pergunta: "))
    enunciado = input('Enunciado: ')
    tipo = input('Tipo (ABERTA, MULTIPLA, UNICA): ')

    pergunta = {"numero": num, "texto": enunciado, "tipo": tipo}
    if tipo != 'ABERTA':
        itens = []
        print('Alternativas - (enter em branco quando quiser parar)')
        opcao = input('item: ')
        while opcao != '':
            itens.append(opcao)
            opcao = input('item: ')
        pergunta['itens'] = itens

    return pergunta     

def aplica_pergunta(quest):
    print(f"{quest['numero']}) {quest['texto']}")
    if quest['tipo'] != 'ABERTA':
        s = 'abcdefghijklmnopqrstuvxyz'
        i = 0
        alter = ''
        itens = quest['itens']
        while i < len(itens):
            alter = alter + f"{s[i]}) {itens[i]}\n"
            i = i + 1
        print(alter)
    resp = input("Resposta: ")
    return resp




print('='*80)
print('Sistema de Enquete')
opcao = 0
lista_perguntas = []
lista_respostas = []
while opcao != 6:
    opcao = menu()
    if opcao == 1:
        questao = monta_pergunta()
        lista_perguntas.append(questao)
    
    elif opcao == 2:
        print("Altera pergunta")
        questao = monta_pergunta()
        num = questao['numero']
        alterado = False
        i = 0
        while i < len(lista_perguntas):
            perg = lista_perguntas[i]
            if perg['numero'] == num:
                lista_perguntas[i] = questao
                alterado = True
                i = len(lista_perguntas) #para sair do while
            i = i + 1

        if alterado:
            print("Questão {num} foi alterada com sucesso")
        else:
            print("Não existe questão {num} na lista de perguntas")

    elif opcao == 3: 
        print('UNDER construction...')
        for info in lista_respostas:
            print(info)

    elif opcao == 4:
        for p in lista_perguntas:
            print(p)

    elif opcao == 5:
        for p in lista_perguntas:
            resp = aplica_pergunta(p)
            registro = {'pergunta': p, 'resposta': resp}
            lista_respostas.append(registro)

    elif opcao == 6:
        print("Saindo do sistema, as perguntas cadastradas não serão salvas")

    else:
        print("Opção inválida")
