aux = input("Base: ")
base = float(aux)

aux = input("Altura: ")
altura = float(aux)

area = base * altura / 2

print("A area vale ", area, "cm^2") #varios parametros para o print
print("A area vale " + str(area)) #concatenando 2 strings
print(f"A area vale {area}") #f-string: importante aprender!
