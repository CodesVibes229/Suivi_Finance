from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from . import app
from .forms import TransactionForm
from .models import db, Transaction
from .utils import get_exchange_rate

app = Flask(__name__)


# Route pour obtenir toutes les transactions (API GET)
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions])


# Route pour obtenir le taux de change (API GET)
@app.route('/api/exchange_rate', methods=['GET'])
def exchange_rate():
    base_currency = request.args.get('base', 'USD')
    target_currency = request.args.get('target', 'EUR')
    rate = get_exchange_rate(base_currency, target_currency)
    return jsonify({'rate': rate})


# Route pour ajouter une transaction (Formulaire POST)
@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()

    if form.validate_on_submit():
        # Récupérer les données du formulaire
        name = form.name.data
        amount = form.amount.data
        transaction_type = form.transaction_type.data
        currency = form.currency.data
        date = form.date.data

        # Créer la nouvelle transaction
        new_transaction = Transaction(
            name=name,
            amount=amount,
            transaction_type=transaction_type,
            currency=currency,
            date=date
        )

        # Ajouter la transaction à la base de données
        db.session.add(new_transaction)
        db.session.commit()

        flash('Transaction ajoutée avec succès!', 'success')
        return redirect(url_for('add_transaction'))  # Redirige vers la page de création (ou index)

    return render_template('add_transaction.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
