import random


def cria_matriz(lin: int, col: int) -> list:
    mat = []
    for i in range(lin):
        mat.append([0] * col)
    return mat

def preenche(matriz: list):
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            matriz[i][j] = random.randint(1, 200)


def contagem(matriz: list) -> list:
    contador = [0] * 201
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            v = matriz[i][j]
            contador[v] = contador[v] + 1
    
    return contador

if __name__ == "__main__":
    mat = cria_matriz(30, 50)
    preenche(mat)
    #for lin in mat:
    #    print(lin)
    
    resultado = contagem(mat)
    for i in range(1, 201):
        print(f"{i} -> {"**" * resultado[i]}")
        print(f"{i} -> {resultado[i]}")