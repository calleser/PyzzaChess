// parte do chess

async function carregar() {

    const resposta = await fetch("http://127.0.0.1:5000/jogo")
    const dados = await resposta.json()
    console.log(dados.fen)

}

carregar()

function desenhar(fen) {
    // TODO: transformar o FEN em matriz 8x8
    // TODO: laço duplo criando 64 divs dentro de #tabuleiro
}

async function mover(origem, destino) {
    // TODO: fetch POST pra /jogo/mover com {origem, destino} no body
    // TODO: se deu certo, redesenhar; se não, mostrar o erro
} d