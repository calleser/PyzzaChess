from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ARQUIVO = "cadastro.json"

def salvar(lista):
    lista_usuarios = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as a:
            lista_usuarios = json.load(a)

    lista_usuarios.append(lista)

    with open(ARQUIVO, "w") as arquivo:
        json.dump(lista_usuarios, arquivo)


@app.route("/cadastro", methods=["POST"])

def adicionar_usuario():
    dados = request.get_json()

    salvar(dados)
    return jsonify({"mensagem": "Usuario cadastrado"}), 201 

if __name__ == "__main__":
    app.run(debug=True, port=5000)