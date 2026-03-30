import json

def pacientes_load() -> list:
    with open('paciente.json', mode="r") as arq:
        pacientes = json.load(arq)
    return pacientes

if __name__ == "__main__":
    lista_pacientes = pacientes_load()
    print(lista_pacientes)

