from flask import Flask, request, jsonify

import db

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def get_todos_carros():
    return db.carros, 200

@app.route("/carros/<int:id>", methods=["GET"])
def get_carro_id(id: int):
    for c in db.carros:
        if c['id'] == id:
            return (c, 200)
        
    info = {'title': f"nenhum carro encontrado: {id}", 'status': 404}
    return info, 404

@app.route("/carros", methods=["POST"])
def adiciona_carro():
    carro = request.json
    #verificacao se os campos obrigatorios estao presentes no json
    chaves = ["id", "marca", "modelo", "placa"]
    for c in chaves:
        if not c in carro:
            info = {'title': f'Json incorreto, chave faltante: {c}', 'status': 404}
            return (info, 404)

    db.carros.append(carro)
    return (carro, 201)

@app.route("/carros", methods=["PUT"])
def altera_carro():
    carro = request.json
    lista = db.carros
    i = 0
    while i < len(lista):
        c = lista[i]
        if c['id'] == carro['id']:
            lista[i] = carro
            return (carro, 201)
        i = i + 1
    info = {'title': f"Nenhum carro com o id: {carro['id']}", 'status': 404}
    return info



app.run(debug=True)