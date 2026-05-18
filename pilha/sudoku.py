import os
import time
from pilha import Pilha

def matriz_original() -> list:
    mat = []
    for i in range(9):
        mat.append([0] * 9)
    mat[0][0] = 1
    mat[0][1] = 6
    mat[0][2] = 8
    mat[0][6] = 9
    mat[0][8] = 2

    mat[1][3] = 3
    mat[1][5] = 1

    mat[2][1] = 3
    mat[2][3] = 6
    mat[2][4] = 2

    mat[3][2] = 9
    mat[3][6] = 1
    mat[3][8] = 6

    mat[4][2] = 1
    mat[4][6] = 3
    mat[4][7] = 7

    mat[5][1] = 4
    mat[5][2] = 3
    mat[5][3] = 5
    mat[5][8] = 9

    mat[6][3] = 8
    mat[6][5] = 2
    mat[6][6] = 6

    mat[7][3] = 9
    mat[7][5] = 5
    mat[7][7] = 2
    mat[7][8] = 3

    mat[8][0] = 2
    mat[8][2] = 6
    mat[8][4] = 3
    mat[8][6] = 7

    return mat

def proxima_posicao(posicao: list) -> list:
    resp = [0, 0]
    if posicao[1] == 8: #coluna
        resp[0] = posicao[0] + 1
        resp[1] = 0
    else:
        resp[0] = posicao[0]
        resp[1] = posicao[1] + 1
    return resp


def get_posicoes_originais(mat: list) -> dict:
    retorno = {}
    for i in range(9):
        for j in range(9):
            if mat[i][j] != 0:
                retorno[(i, j)] = (i, j)
    return retorno


def colocou(valor, matriz, pos) -> bool:
    lin = pos[0]
    col = pos[1]
    if pode_linha(lin, valor, matriz) and pode_coluna(col, valor, matriz) and pode_regiao(lin, col, valor, matriz):
        matriz[lin][col] = valor
        return True
    return False

def pode_linha(l, v, mat) -> bool:
    for c in range(9):
        if mat[l][c] == v:
            return False
    return True

def pode_coluna(c, v, mat) -> bool:
    for l in range(9):
        if mat[l][c] == v:
            return False
    return True


def pode_regiao(lin, col, v, mat) -> bool:
    l = (lin // 3) * 3   #encontrando posicoes iniciais da regiao
    c = (col // 3) * 3
    for x in range(3):
        if mat[l + x][c + x] == v:
            return False
    return True

def imprime(mat: list):
    os.system('cls')
    for lin in mat:
        print(lin)
    time.sleep(0.1)

pilha_posicoes = Pilha(100)
mat = matriz_original()
posicoes_originais = get_posicoes_originais(mat)
pos = [0, 0]

imprime(mat)

while True:
    lin = pos[0]
    col = pos[1]

    if (lin, col) in posicoes_originais:   #nao faco nada (original)
        pos = proxima_posicao(pos)
    else:
        valor = mat[lin][col] + 1
        while not colocou(valor, mat, pos) and valor < 10:
            valor = valor + 1

        imprime(mat)

        if valor < 10: #colocou o valor na matriz
            pilha_posicoes.put(pos)
            pos = proxima_posicao(pos)
        else:
            mat[lin][col] = 0
            pos = pilha_posicoes.pop()
    
    if pos[0] >= 9:  #cheguei no índice 9 da linha da matriz, ou seja, passei por todas as 9 linhas
        break


imprime(mat)