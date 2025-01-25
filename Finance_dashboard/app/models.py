from datetime import datetime
from . import db

# Modèle pour la table 'transactions'
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)  # Montant de la transaction
    transaction_type = db.Column(db.String(10), nullable=False)  # Type de la transaction (revenu ou dépense)
    currency = db.Column(db.String(3), nullable=False)  # Devise de la transaction (ex. USD, EUR)
    date = db.Column(db.Date, nullable=False)  # Date de la transaction

    def __init__(self, name, amount, transaction_type, currency, date):
        self.name = name
        self.amount = amount
        self.transaction_type = transaction_type
        self.currency = currency
        self.date = date

    # Méthode pour convertir un objet Transaction en dictionnaire pour l'API
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'amount': str(self.amount),  # Convertir le montant en chaîne pour JSON
            'transaction_type': self.transaction_type,
            'currency': self.currency,
            'date': self.date.strftime('%Y-%m-%d')  # Formater la date en string
        }

# Créer la base de données si elle n'existe pas encore
def create_db():
    db.create_all()
