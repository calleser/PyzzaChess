id_username = document.getElementById("username")
id_senha = document.getElementById("senha")

const API_URL = "http://127.0.0.1:5000/cadastro"

function verificar(){
    username = id_username.value
    senha = id_senha.value

    tudo_certo = true
    
    if (username == ''){
        alert("Preencha o username.")
        id_username.style.backgroundColor = "red"
        tudo_certo = false
    }

    if (senha == ''){
        alert("Preencha o senha.")
        id_senha.style.backgroundColor = "red"
        tudo_certo = false
    }

    if (tudo_certo){
        alert("Conta registrada com sucesso, logando...")
        cadastrar();
    }
}

async function cadastrar(){
    await fetch(API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username,
            senha: senha
        })
    })
}

function voltar(id){
    document.getElementById(id).style.backgroundColor = "white"
}

function desenhar(fen) {
    // TODO: transformar o FEN em matriz 8x8
    // TODO: laço duplo criando 64 divs dentro de #tabuleiro
}

async function mover(origem, destino) {
    // TODO: fetch POST pra /jogo/mover com {origem, destino} no body
    // TODO: se deu certo, redesenhar; se não, mostrar o erro
}