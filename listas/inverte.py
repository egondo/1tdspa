'''Inverte o conteudo de uma lista sem a criacao de uma lista auxiliar'''

def inverte(lista: list) -> None:
    ini = 0
    fim = len(lista) - 1

    while ini < fim:
        aux = lista[ini]
        lista[ini] = lista[fim]
        lista[fim] = aux
        ini = ini + 1
        fim = fim - 1


lst = [4, 82, -98, 0, 34, 6, -10, -16]
inverte(lst)
print(lst)