import requests


url = "https://onetdspa.onrender.com/hospital/triagem"

triagem = {
    "senha": 102,
    "id_funcionario": 1,
    "batimentos": 190,
    "sintomas": "dor nos olhos, fadiga e sono",
    "obs": 'Profissional de TI',
    "alergia": None,
    "temperatura": 35.7,
    "pressao": '14/8'
}

try:
    resp = requests.post(url, json=triagem)
    if resp.status_code == 200 or resp.status_code == 201:
        obj = resp.json()
        print(obj)
    else:
        print("Erro na gravacao da triagem")
except Exception as erro:
    print(erro)