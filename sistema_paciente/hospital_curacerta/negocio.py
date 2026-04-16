import banco
import util

#paciente: nome, cpf, nascimento, telefone e convenio
def atualizacao_paciente(senha: int, paciente: dict):
    id_pac = banco.rec_id_paciente_senha(senha)
    paciente['id_paciente'] = id_pac
    banco.altera_paciente(paciente)



def gerando_senha(cpf: str) -> int:
    paciente = banco.rec_paciente_cpf(cpf)

    senha = banco.rec_senha()
    chegada = util.get_data_hora()

    if paciente == None: 
        paciente = {"nome": None, "convenio": None, "telefone": None, "cpf": cpf, "nascimento": None}
        banco.insere_paciente(paciente)
        
    #gravar a visita com a data e hora da chegada mais a senha e o ID do paciente que foi gerado pelo banco ou recuperado atraves da consulta
    visita = {"chegada": chegada, "senha": senha, "id_paciente": paciente['id_paciente']}
    #print(visita)
    banco.insere_visita(visita)
    
    return senha

if __name__ == "__main__":
    #valor = gerando_senha('111')
    #print(f"senha: {valor}")

    pac = {"nome": "Pato Donald", "nascimento": '1-1-1958', 'convenio': 'Walt Disney', 'telefone': '(11) 83720-9822', 'cpf': '23400898756'}
    atualizacao_paciente(22, pac)

