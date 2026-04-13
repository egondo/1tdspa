import banco 

def gerando_senha(cpf: str) -> int:
    paciente = banco.rec_paciente_cpf(cpf)

    if paciente == None: 
        pac = {"nome": "Jonh Doe", "convenio": "", "telefone": "", "cpf": cpf, "nascimento": '29-02-1994'}
        banco.insere_paciente(pac)
        #nao tenho ainda como recuperar o id do paciente??
        #na proxima aula veremos como fazer.




