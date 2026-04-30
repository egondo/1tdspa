#API do Hospital Cura Certa
#Funciona como um adaptador entre a interface e a camada de ngócio da aplicação (adapter)

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import negocio

app = Flask("API Cura Certa")
CORS(app)

@app.route("/hospital/senha/<cpf>", methods=['GET'])
@cross_origin()
def gera_senha(cpf: str):
    senha = negocio.gerando_senha(cpf)
    info = {"numero": senha, "cpf": cpf}
    return (info, 200)

app.run(debug=True)