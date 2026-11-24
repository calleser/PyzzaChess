from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import chess

tabuleiro = chess.Board()
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

@app.route("/jogo", methods=["GET"])
def ver_jogo():
    return jsonify({"fen": tabuleiro.fen()})
    # TODO: devolver o FEN do tabuleiro num jsonify

@app.route("/jogo/mover", methods=["POST"])
def mover():
    dados = request.get_json()
    # TODO: montar o lance com origem + destino
    # TODO: se for válido -> push e devolver o FEN novo
    # TODO: se não for -> devolver um erro com status 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
