from flask import Flask, render_template
import sys
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config
from app.models import db, User
from app.routes import routes  # Importer le Blueprint principal

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Initialiser l'application Flask avec la fonction create_app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialisation de la base de données et de la migration
    db.init_app(app)
    Migrate(app, db)

    # Initialiser le gestionnaire de sessions pour les utilisateurs (Flask-Login)
    login_manager = LoginManager(app)
    login_manager.login_view = 'routes.login'  # Spécifier le Blueprint pour la route de connexion

    # Charger l'utilisateur courant dans Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Enregistrer le Blueprint avec le préfixe d'URL
    app.register_blueprint(routes)

    return app

# Créer l'application Flask
app = create_app()

#Ici les routes seront définies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Récupérer toutes les transactions pour le tableau de bord
    transactions = Transaction.query.all()
    return render_template('dashboard.html', transactions=transactions)

# Pour gérer la connexion (et l'inscription si nécessaire)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Ici tu dois ajouter la logique de connexion
    return render_template('login.html')

# Créer la base de données si elle n'existe pas encore
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
