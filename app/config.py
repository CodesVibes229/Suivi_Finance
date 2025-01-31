import os


class Config:
    """Configuration de base pour l'application Flask."""

    # Clé secrète pour les sessions et JWT
    SECRET_KEY = os.environ.get('SECRET_KEY', 'une_clé_secrète_que_tu_devrais_changer')

    # Configuration de la base de données (ici SQLite ou MySQL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Pour éviter des avertissements inutiles
    SQLALCHEMY_DATABASE_URI = 'mariadb+pymysql://root:ghost229@localhost/finances'
    # Configuration de l'API de taux de change (exemple avec 'exchangeratesapi.io')
    EXCHANGE_API_URL = "https://api.exchangeratesapi.io/latest"
    EXCHANGE_API_KEY = os.environ.get('EXCHANGE_API_KEY', 'ta_clé_api')

    # Configurations de JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'une_autre_clé_secrète_pour_jwt')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 heure

    # Optionnel : pour l'activation du mode debug
    DEBUG = True if os.environ.get('FLASK_ENV') == 'development' else False

    #Flask-login
    LOGIN_DISABLED = False