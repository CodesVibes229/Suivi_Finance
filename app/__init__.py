from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

# Crée une instance de la base de données et de JWT
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    # Crée l'instance de l'application Flask
    app = Flask(__name__)

    # Charge la configuration à partir de config.py
    app.config.from_object(Config)

    # Initialise les extensions Flask
    db.init_app(app)
    jwt.init_app(app)

    # Importation et enregistrement des routes (routes.py)
    from .routes import bp
    app.register_blueprint(bp)

    return app
