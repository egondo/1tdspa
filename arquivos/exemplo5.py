#Abrindo arquivos grandes
import datetime

with open("bigfile.txt", mode = "r", encoding="latin1") as arq:
    ini = datetime.datetime.now()
    linha = 0
    for info in arq:
        linha = linha + 1
    fim = datetime.datetime.now()
    print(f"Finalizando leitura dos dados {fim - ini}")
    print("Linha", linha)