''' Implementar o algoritmo busca em largura (BFS) com o 
objetivo de encontrar a saída de um labirinto representado
pela matriz abaixo'''
import time
import os

def busca_vizinhos(pos, matriz) -> list:
    resp = []
    l = pos[0]
    c = pos[1]
    ind_last_col = len(matriz[0]) - 1
    ind_last_lin = len(matriz) - 1

    #norte
    if l > 0 and matriz[l - 1][c] == 0:
        resp.append( (l - 1, c) )
    
    #leste
    if c < ind_last_col and matriz[l][c + 1] == 0:
        resp.append( (l, c + 1) )

    #sul
    if l < ind_last_lin and matriz[l + 1][c] == 0:
        resp.append( (l + 1, c) )

    #oeste
    if c > 0 and matriz[l][c - 1] == 0:
        resp.append( (l, c - 1) )

    return resp

def imprime(mat):
    for lin in mat:
        print(lin)


fila = []
lab = [
  [ 0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0],
  [ 0, -1,  0,  0, -1,  0, -1,  0, -1, -1,  0],
  [ 0,  0, -1,  0, -1,  0, -1,  0,  0,  0, -1],
  [ 0, -1,  0, -1,  0,  0,  0, -1, -1,  0,  0],
  [ 0,  0,  0, -1,  0, -1,  0,  0,  0, -1,  0],
  [ 0, -1,  0,  0,  0,  0,  0,  0, -1,  0,  0]
]

#iniciando a minha busca
pos = (0, 0)
fila.append(pos)
lab[0][0] = 1

#estabelecendo a posicao de saida do labirinho
lin = len(lab)
col = len(lab[0]) 
saida = (lin - 1, col - 1)

while pos != saida:
    pos = fila.pop(0)
    lista = busca_vizinhos(pos, lab)
    #lista é um list de tuplas, cada tupla representa um vizinho da primeira posicao da fila
    l = pos[0]
    c = pos[1]
    valor = lab[l][c] + 1
    for aux in lista:
        l = aux[0]
        c = aux[1]
        lab[l][c] = valor 
        fila.append(aux)
        
    os.system('clear')
    imprime(lab)
    time.sleep(0.5)

    
