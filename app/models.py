from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Instantiation de la base de données
db = SQLAlchemy()


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

    # Méthode pour convertir un objet Transaction en dictionnaire pour le graphique
    def to_chart_data(self):
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'amount': float(self.amount),  # Conversion pour s'assurer que c'est un float
            'type': self.transaction_type,
            'currency': self.currency
        }


# Modèle pour la table 'users' (pour gérer la connexion avec Flask-Login)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# N'oublie pas d'importer cette classe dans le fichier run.py si tu l'utilises pour gérer la connexion

