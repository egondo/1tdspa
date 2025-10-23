agenda = {
    'ana': 'ana@gmail.com',
    'beto': 'betao@yahoo.com.br',
    'cida': 'cidinha@fiap.com.br'
}

agenda['dani'] = 'danilo@microsoft.com'

print("")
print(agenda)
print("")

agenda['beto'] = 'roberto_soares@gmail.com'

for c in agenda.keys():
    print(f"{c} => {agenda[c]}")


for v in agenda.values():
    print(v)

