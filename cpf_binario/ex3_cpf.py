cpf_nove = int(input("Digite os 9 primeiros dígitos do cfp: "))
aux_cpf = cpf_nove

soma = 0
mult = 2

while mult <= 10:
    dig = cpf_nove % 10
    soma = soma + dig * mult
    cpf_nove = cpf_nove // 10
    mult = mult + 1

resto = soma % 11
if resto < 2:
    dc = 0
else:
    dc = 11-resto
#print(f"primeiro DC vale {dc}")

cpf_nove = aux_cpf * 10 + dc
soma = 0
mult = 2
while cpf_nove != 0:
    dig = cpf_nove % 10
    soma = soma + dig * mult
    cpf_nove = cpf_nove // 10
    mult = mult + 1

resto = soma % 11
if resto < 2:
    dc2 = 0
else:
    dc2 = 11 - resto

print(f"Os digitos de controle do {aux_cpf} sao {dc * 10 + dc2}")
