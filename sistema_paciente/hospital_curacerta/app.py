#API do Hospital Cura Certa
#Funciona como um adaptador entre a interface e a camada de ngócio da aplicação (adapter)

from flask import Flask, jsonify, request
import negocio

app = Flask("API Cura Certa")

@app.route("/hospital/senha/<cpf>", methods=['GET'])
def gera_senha(cpf: str):
    senha = negocio.gerando_senha(cpf)
    info = {"numero": senha, "cpf": cpf}
    return (info, 200)

app.run(debug=True)