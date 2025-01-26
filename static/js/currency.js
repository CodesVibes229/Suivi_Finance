// currency.js
document.addEventListener('DOMContentLoaded', function() {
    // Gérer la conversion des devises au chargement de la page
    handleCurrencyExchange();
});

// Fonction pour récupérer le taux de change depuis l'API
function handleCurrencyExchange() {
    const exchangeButton = document.getElementById('exchange-button');

    exchangeButton.addEventListener('click', function() {
        const baseCurrency = document.getElementById('base-currency').value;
        const targetCurrency = document.getElementById('target-currency').value;

        // Récupérer le taux de change via l'API
        fetch(`/api/exchange_rate?base=${baseCurrency}&target=${targetCurrency}`)
            .then(response => response.json())
            .then(data => {
                if (data.rate) {
                    const rate = data.rate;
                    // Afficher le taux de change
                    const rateElement = document.getElementById('exchange-rate');
                    rateElement.textContent = `Taux de change (${baseCurrency} -> ${targetCurrency}): ${rate}`;
                } else {
                    console.error('Taux de change introuvable');
                }
            })
            .catch(error => {
                console.error('Erreur lors de la récupération du taux de change:', error);
            });
    });
}
