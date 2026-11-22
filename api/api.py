from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ARQUIVO = "cadastro.json"

def salvar(lista):
    lista_aluno = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as a:
            lista_aluno = json.load(a)

    lista_aluno.append(lista)

    with open(ARQUIVO, "w") as arquivo:
        json.dump(lista_aluno, arquivo)


@app.route("/alunos", methods=["POST"])

def adicionar_aluno():
    dados = request.get_json()

    salvar(dados)
    return jsonify({"mensagem": "Aluno salvo"}), 201 

if __name__ == "__main__":
    app.run(debug=True, port=5000)