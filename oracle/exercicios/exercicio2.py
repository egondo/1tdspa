from faker import Faker
import random

fake = Faker("pt_BR")

convs = ["Amil", "Prevent Senior", "Unimed", "Care Plus", "SUS", "Particular", "Bradesco"]

sqls = []
for _ in range(100):
    i = random.randint(0, len(convs) - 1)
    sqls.append(f"INSERT INTO T_PS_PACIENTE(nome, telefone, convenio, nascimento) VALUES('{fake.name()}', '{fake.phone_number()}', '{convs[i]}', to_date('{fake.date_of_birth()}', 'YYYY-MM-DD'));")
    
for comando in sqls:
    print(comando)