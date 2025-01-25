from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask import render_template
from .config import Config
from .models import db, Transaction
from .routes import app

# Initialiser l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Initialiser les extensions
db.init_app(app)
migrate = Migrate(app, db)

# Initialiser le gestionnaire de sessions pour les utilisateurs (Flask-Login)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Si un utilisateur non connecté tente d'accéder à une page protégée

# Charger l'utilisateur courant dans Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Cette fonction doit renvoyer l'utilisateur à partir de l'ID
    # Par exemple, ici c'est un modèle User à définir dans ton application
    return User.query.get(int(user_id))

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

if __name__ == '__main__':
    app.run(debug=True)
