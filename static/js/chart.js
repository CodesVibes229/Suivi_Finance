// chart.js
function renderFinanceChart(transactions) {
    // On suppose que `transactions` est un tableau d'objets avec les propriétés: date, amount, type (revenu ou dépense), et currency.
    const labels = [];
    const incomeData = [];
    const expenseData = [];

    // Tri et traitement des données des transactions
    transactions.forEach(transaction => {
        const month = new Date(transaction.date).toLocaleString('default', { month: 'long' });

        if (!labels.includes(month)) {
            labels.push(month);
            incomeData.push(0);  // Initialiser à 0 pour chaque mois
            expenseData.push(0); // Initialiser à 0 pour chaque mois
        }

        const monthIndex = labels.indexOf(month);

        if (transaction.type === 'income') {
            incomeData[monthIndex] += transaction.amount;
        } else if (transaction.type === 'expense') {
            expenseData[monthIndex] += transaction.amount;
        }
    });

    const ctx = document.getElementById('finance-chart').getContext('2d');

    // Créer un graphique en barres avec les données des transactions
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Revenus',
                    data: incomeData,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Dépenses',
                    data: expenseData,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        },
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
