def esta_ordenado(lista: list, chave: str) -> bool:
    i = 0
    while i < len(lista) - 1:
        if lista[i][chave] <= lista[i+1][chave]:
            i = i + 1
        else:
            return False
    return True

carros = [
    {"placa": "BJU 8932", "modelo": "Corcel", "montadora": "Ford", "ano": 1980},
    {"placa": "CKR 0293", "modelo": "Fusca", "montadora": "Volkswagen", "ano": 1984},
    {"placa": "ADF 5620", "modelo": "Monza", "montadora": "GM", "ano": 1994}, 
    {"placa": "HJW 0394", "modelo": "Ram", "montadora": "Dodge","ano": 2020},
    {"placa": "DHU 8282", "modelo": "Virtus", "montadora": "Volkswagen", "ano": 2025},
]

chaves = ["placa", "modelo", "montadora", "ano"]
for c in chaves:
    resp = esta_ordenado(carros, c)
    if resp:
        print(c)

