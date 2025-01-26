from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config
from flask_migrate import Migrate

# Crée une instance de la base de données et de JWT
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    # Crée l'instance de l'application Flask
    app = Flask(__name__)

    # Charge la configuration à partir de config.py
    app.config.from_object(Config)

    # Initialise les extensions Flask
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Importation et enregistrement des routes (routes.py)
    from . import routes
    from .routes import bp
    app.register_blueprint(bp)

    return app
