const IP = "http://45.77.150.143:4800";
const API_URL = `${IP}/cep/`;


// Alternar modo escuro
const toggleDarkModeButton = document.getElementById("toggle-dark-mode");
if (localStorage.getItem("dark-mode") === "enabled") {
    document.body.classList.add("dark-mode");
    toggleDarkModeButton.textContent = "☀️ Modo Claro";
}

toggleDarkModeButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const isDarkMode = document.body.classList.contains("dark-mode");

    toggleDarkModeButton.textContent = isDarkMode ? "☀️ Modo Claro" : "🌙 Modo Escuro";
    localStorage.setItem("dark-mode", isDarkMode ? "enabled" : "disabled");
});

// Buscar CEP
document.getElementById("cep-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const cep = document.getElementById("numero-cep").value.trim();
    const cepResult = document.getElementById("cep-result");

    if (!cep || cep.length !== 8 || isNaN(cep)) {
        showMessage("Digite um CEP válido!", "error");
        return;
    }

    try {
        const response = await fetch(`${API_URL}${cep}`);
        if (!response.ok) throw new Error("Erro ao buscar o CEP!");

        const data = await response.json();
        if (data.erro) {
            showMessage("CEP não encontrado!", "error");
        } else {
            cepResult.innerHTML = `
                <strong>CEP:</strong> ${data.cep} <br>
                <strong>Endereço:</strong> ${data.logradouro} <br>
                <strong>Bairro:</strong> ${data.bairro} <br>
                <strong>Cidade:</strong> ${data.localidade} - ${data.uf}
            `;
            cepResult.className = "success";
            cepResult.style.display = "block";
        }
    } catch (error) {
        showMessage("Erro ao buscar o CEP. Verifique a conexão.", "error");
    }
});

// Exibir mensagens de erro/sucesso
function showMessage(message, type) {
    const cepResult = document.getElementById("cep-result");
    cepResult.textContent = message;
    cepResult.className = type;
    cepResult.style.display = "block";
}
