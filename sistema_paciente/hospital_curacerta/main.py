import negocio

def menu() -> int:
    info = '''Hospital Cura Certa
    1 - senha
    2 - triagem
    3 - guichê
    4 - consulta <- fazer esta funcionalidade
    5 - procedimentos
    6 - sair
    '''
    print(info)
    opcao = int(input("Selecione: "))
    return opcao

def consulta(): 
    senha = int(input("Senha: "))
    id_funcionario = 2
    consulta = input("diagnostico e encaminhamentos: ")
    situacao = input("Paciente recebeu alta? (s/n) ")
    proc = {"descricao": consulta, "id_funcionario": id_funcionario}
    #TODO fazer esta funcionalida e a alta_paciente
    negocio.cadastra_procedimento(proc, senha)
    if situacao == 's':
        negocio.alta_paciente(senha)


def triagem():
    senha = int(input("Senha: "))
    id_funcionario = 1 #Maria de Fatima - enfermeira
    batimentos = int(input("Batimentos: "))
    temperatura = float(input("Temperatura: "))
    pressao = input("Pressão: ")
    sintomas = input("Sintomas: ")
    alergia = input("Alergias: ")
    obs = input("Observacão: ")

    tri = {"senha": senha, "id_funcionario": id_funcionario, "batimentos": batimentos, "temperatura": temperatura, "pressao": pressao, "sintomas": sintomas, "alergia": alergia, "obs": obs}

    negocio.cadastra_triagem(tri)

if __name__ == "__main__":
    op = menu()
    while op != 6:
        if op == 1:
            cpf = input("CPF: ")
            senha = negocio.gerando_senha(cpf)
            print(f"Senha: {senha}")
        elif op == 2:
            triagem()
        elif op == 3:
            print("Daqui a pouco!")
        input("digite enter para continuar...")
        op = menu()