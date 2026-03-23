def soma_linha(matriz: list, lin: int):
    col = len(matriz[0])
    soma = 0
    for j in range(col - 1):
        soma = soma + matriz[lin][j]
    matriz[lin][col - 1] = soma

mat = [
    [23, 45, 29, 90, None],
    [19, 67, 71, -9, None],
    [-2, 89, 54, 43, None],
    [-7, 18, -6, 36, None]
]

for i in range(len(mat)):
    soma_linha(mat, i)

for lin in mat:
    print(lin)