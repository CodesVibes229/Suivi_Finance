from flask import Flask
import sys
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask import render_template
from app.config import Config
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app.models import db, Transaction  # Assurez-vous que le chemin d'importation est correct
from routes import *

# Initialiser l'application Flask avec la fonction create_app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialisation de la base de données et de la migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialiser le gestionnaire de sessions pour les utilisateurs (Flask-Login)
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'  # Si un utilisateur non connecté tente d'accéder à une page protégée

    # Charger l'utilisateur courant dans Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Assurez-vous que le modèle User est défini

    return app

# Créer l'application Flask
app = create_app()

# Créer la base de données si elle n'existe pas encore
with app.app_context():
    db.create_all()

# Routes de l'application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    transactions = Transaction.query.all()
    return render_template('dashboard.html', transactions=transactions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
