cpf = int(input("CPF (só digitos): "))

dc = cpf % 100
cpf = cpf // 100

parte3 = cpf % 1000
cpf = cpf // 1000

parte2 = cpf % 1000
cpf = cpf // 1000

parte1 = cpf

print(f"{parte1}.{parte2}.{parte3}-{dc}")
