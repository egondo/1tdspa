import json
import datetime

def pacientes_load() -> list:
    with open('paciente.json', mode="r") as arq:
        pacientes = json.load(arq)
    return pacientes

def prontuarios_load() -> dict:
    try:
        with open('prontuario.json', mode='r') as arq:
            prontuarios = json.load(arq)
    except FileNotFoundError as erro:
        return {}
    return prontuarios


def prontuarios_save(dados: dict):
    with open('prontuario.json', mode="w") as arq:
        json.dump(dados, arq)

def menu() -> int:
    print("Sistema Hospitalar")
    msg = "1 - triagem\n2 - consulta\n3 - atendimento\n4 - retorno\n5 - sair\nopcao: "
    opcao = int(input(msg))
    return opcao

def triagem(prontuarios: dict):
    cpf = input("Informe cpf: ")
    atendente = "Maria do Socorro"
    pressao = input("Pressao: ")
    temperatura = input("Temperatura: ")
    batimentos = input("Ritmo cardíaco: ")
    sintomas = input("Sintomas: ")
    if cpf in prontuarios:
        lista = prontuarios[cpf] #prontuarios.get(cpf)
    else:
        lista = []
        prontuarios[cpf] = lista
    
    ficha = {
        "entrada": str(datetime.datetime.now()),
        "sintomas": sintomas,
        "sinais_vitais": f"{pressao}, {temperatura}, {batimentos}",
        "atendentes":[atendente],
        "atendimento": "Triagem"
    }

    lista.insert(0, ficha)
    prontuarios_save(prontuarios)


def consulta_medica(prontuarios: dict):
    cpf = input("Cpf: ")
    medico = "Andreia Souza"
    ficha = prontuarios.get(cpf)[0]
    print(f"Sinais vitais: {ficha['sinais_vitais']}")
    print(f"Sintomas: {ficha['sintomas']}")
    diagnostico = input("Diagnostico: ")
    tratamento = input("Tratamento: ")
    ficha['atendimento'] = f"{ficha['atendimento']}; {tratamento}"
    ficha['diagnostico'] = diagnostico
    if not medico in ficha['atendentes']:
        ficha['atendentes'].append(medico)
    prontuarios_save(prontuarios)



if __name__ == "__main__":
    lista_pacientes = pacientes_load()
    prontuarios = prontuarios_load()
    opcao = 0
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            triagem(prontuarios)
        elif opcao == 2:
            consulta_medica(prontuarios)
        elif opcao == 3:
            atendimento(lista_pacientes, prontuarios)
        elif opcao == 4:
            retorno(lista_pacientes, prontuarios)
        elif opcao == 5:
            print("Saindo, obrigado pela preferência")
        else:
            print("Opcao inválida")


