// Aguarda até que o DOM esteja totalmente carregado
document.addEventListener('DOMContentLoaded', () => {
    console.log("O arquivo scripts.js foi carregado com sucesso!");

    // Exemplo: Alterar o texto de um elemento ao clicar em um botão
    const botao = document.getElementById('botao-exemplo');
    const mensagem = document.getElementById('mensagem-exemplo');

    if (botao && mensagem) {
        botao.addEventListener('click', () => {
            mensagem.textContent = "Você clicou no botão!";
            botao.style.backgroundColor = '#4CAF50'; // Muda a cor do botão
        });
    }
});
