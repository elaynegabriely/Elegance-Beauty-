// Aguarda o carregamento da página
document.addEventListener('DOMContentLoaded', () => {
    const botao = document.getElementById('meu-botao');
    const mensagem = document.getElementById('mensagem');

    // Adiciona um evento ao botão
    botao.addEventListener('click', () => {
        mensagem.textContent = 'Você clicou no botão!';
        botao.style.backgroundColor = '#4CAF50'; // Muda a cor do botão
    });
});
