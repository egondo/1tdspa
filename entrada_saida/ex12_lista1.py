aux = input("RM: ")
rm = int(aux)
aux_rm = rm
ac = 0 #acumulador

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

resto = rm % 10
ac = ac + resto
rm = rm // 10

print("A soma dos digitos do RM:", aux_rm, "vale", ac)
print(f"A soma dos digitos do RM: {aux_rm} vale {ac}")

