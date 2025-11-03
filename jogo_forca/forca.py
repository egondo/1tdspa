def transforma_palavra(palavra: str, descoberto: list) -> str:
    resposta = ''
    i = 0
    while i < len(palavra):
        if descoberto[i]:
            resposta = resposta + palavra[i] + ' '
        else:
            resposta = resposta + '_ '
        i = i + 1
    return resposta


def busca_letra(palavra: str, letra: str, descoberto: list) -> bool:
    i = 0
    encontrou = False
    while i < len(palavra):
        if letra == palavra[i]:
            descoberto[i] = True
            encontrou = True
        i = i + 1
    return encontrou

def descobriu_palavra(descoberto: list) -> bool:
    for valor in descoberto:
        if valor == False:
            return False
    
    return True


palavra = 'abacaxi'
descoberto = [False] * len(palavra)
erros = 0

while erros < 6 and not descobriu_palavra(descoberto):
    tracejado = transforma_palavra(palavra, descoberto)
    print(tracejado)
    print(f"Erros: {erros}")
    letra = input("Letra: ")
    resultado = busca_letra(palavra, letra, descoberto)
    if resultado == False:
        erros = erros + 1

if erros >= 6:
    print(f"Vc perdeu, a palavra era {palavra}")
else:
    print(f"Parabéns, vc acertou a palavra {palavra}")