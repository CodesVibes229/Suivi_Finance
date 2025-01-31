from flask import Flask
from app.config import Config
from app.routes import main_bp, auth_bp, transaction_bp, routes  # Importation des Blueprints
from app.extensions import db, migrate, login_manager  # Importe les extensions depuis extensions.py

def create_app():
    # Crée l'instance de l'application Flask
    app = Flask(__name__)

    # Charge la configuration à partir de config.py
    app.config.from_object(Config)

    # Initialisation de la base de données et de la migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialisation du gestionnaire de sessions pour les utilisateurs (Flask-Login)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'  # Spécifiez ici le Blueprint pour la connexion

    # Importation et enregistrement des routes en utilisant des Blueprints
    app.register_blueprint(routes)
    app.register_blueprint(main_bp)  # Routes générales
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Routes d'authentification
    app.register_blueprint(transaction_bp, url_prefix='/transactions')  # Routes des transactions

    return app