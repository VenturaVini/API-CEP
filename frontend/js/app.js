const API_URL = 'https://viacep.com.br/ws'; // Exemplo de API de CEP

document.getElementById('cep-form')?.addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o recarregamento da página
    
    const cepInput = document.getElementById('numero-cep');
    const CEP = cepInput.value.trim();

    if (!CEP) {
        showMessage('Por favor, digite um CEP válido.', 'error');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/${CEP}/json`);

        if (!response.ok) {
            throw new Error('Erro ao buscar CEP.');
        }

        const data = await response.json();
        showMessage(`CEP encontrado: ${data.logradouro}, ${data.localidade} - ${data.uf}`, 'success');

    } catch (error) {
        showMessage(error.message, 'error');
    }
});

function showMessage(message, type) {
    alert(`${type.toUpperCase()}: ${message}`);
}


document.getElementById('toggle-dark-mode').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode'); // Alterna entre claro e escuro

    // Salvar a preferência no localStorage para manter o estado ao recarregar a página
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
});

// Verificar e aplicar a preferência do usuário ao carregar a página
window.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }
});
