// parte do chess

async function carregar() {

    const resposta = await fetch("http://127.0.0.1:5000/jogo")
    const dados = await resposta.json
    console.log(dados.fen)

}

carregar()