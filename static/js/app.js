document.addEventListener('DOMContentLoaded', function() {
    // Récupérer et afficher les transactions
    fetchTransactions();

    // Afficher les graphiques de transactions
    displayCharts();

    // Gestion des taux de change
    handleCurrencyExchange();
});

// Fonction pour récupérer les transactions depuis l'API
function fetchTransactions() {
    fetch('/api/transactions')
        .then(response => response.json())
        .then(data => {
            // Afficher les transactions dans une liste ou un tableau
            const transactionList = document.getElementById('transaction-list');
            data.forEach(transaction => {
                const transactionElement = document.createElement('li');
                transactionElement.textContent = `${transaction.name}: ${transaction.amount} ${transaction.currency} (${transaction.date})`;
                transactionList.appendChild(transactionElement);
            });
        })
        .catch(error => console.error('Erreur lors de la récupération des transactions:', error));
}

// Fonction pour afficher les graphiques (revenus vs dépenses) avec Chart.js
function displayCharts() {
    const ctx = document.getElementById('finance-chart').getContext('2d');

    // Données simulées pour les graphiques (à remplacer par les données récupérées depuis l'API)
    const data = {
        labels: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai'], // Mois
        datasets: [{
            label: 'Revenus',
            data: [5000, 6000, 7000, 8000, 8500], // Données des revenus mensuels
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }, {
            label: 'Dépenses',
            data: [4000, 4200, 4500, 4600, 4800], // Données des dépenses mensuelles
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    // Créer un graphique de type bar
    new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Fonction pour gérer les taux de change
function handleCurrencyExchange() {
    const exchangeButton = document.getElementById('exchange-button');
    exchangeButton.addEventListener('click', function() {
        const baseCurrency = document.getElementById('base-currency').value;
        const targetCurrency = document.getElementById('target-currency').value;

        fetch(`/api/exchange_rate?base=${baseCurrency}&target=${targetCurrency}`)
            .then(response => response.json())
            .then(data => {
                const rate = data.rate;
                const rateElement = document.getElementById('exchange-rate');
                rateElement.textContent = `Taux de change (${baseCurrency} -> ${targetCurrency}): ${rate}`;
            })
            .catch(error => console.error('Erreur lors de la récupération du taux de change:', error));
    });
}
