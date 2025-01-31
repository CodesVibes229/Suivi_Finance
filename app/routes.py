from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from app.models import db, Transaction, User
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Création du Blueprint
routes = Blueprint('routes', __name__)

# Blueprint pour les routes principales
main_bp = Blueprint('main', __name__)

# Blueprint pour l'authentification
auth_bp = Blueprint('auth', __name__)

# Blueprint pour les transactions
transaction_bp = Blueprint('transaction', __name__)

# Page d'accueil (main_bp)
@main_bp.route('/')
def index():
    return render_template('index.html')

# Tableau de bord des finances (main_bp)
@main_bp.route('/dashboard')
@login_required
def dashboard():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()  # Utilisation de Transaction
    return render_template('dashboard.html', transactions=transactions)
# Ajouter une transaction (transaction_bp)
@routes.route('/add_transaction', methods=['GET', 'POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        transaction_type = request.form['transaction_type']
        currency = request.form['currency']
        date = request.form['date']

        if not name or not amount or not transaction_type or not currency or not date:
            flash('Tous les champs sont obligatoires.', 'error')
            return redirect(url_for('routes.add_transaction'))

        try:
            transaction = Transaction(
                name=name,
                amount=amount,
                transaction_type=transaction_type,
                currency=currency,
                date=datetime.strptime(date, '%Y-%m-%d')
            )
            db.session.add(transaction)
            db.session.commit()
            flash('Transaction ajoutée avec succès.', 'success')
        except Exception as e:
            flash(f"Erreur lors de l'ajout de la transaction : {e}", 'error')
            db.session.rollback()

        return redirect(url_for('routes.dashboard'))

    return render_template('add_transaction.html')

# Connexion utilisateur (auth_bp)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Connexion réussie.', 'success')
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Email ou mot de passe incorrect.', 'error')

    return render_template('login.html')

# Déconnexion utilisateur (auth_bp)
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous vous êtes déconnecté.', 'success')
    return redirect(url_for('routes.index'))

# Inscription utilisateur (auth_bp)
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Les mots de passe ne correspondent pas.', 'error')
            return redirect(url_for('routes.register'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Un utilisateur avec cet email existe déjà.', 'error')
            return redirect(url_for('routes.register'))

        try:
            password_hash = generate_password_hash(password)
            new_user = User(email=email, password_hash=password_hash)
            db.session.add(new_user)
            db.session.commit()
            flash('Inscription réussie. Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('routes.login'))
        except Exception as e:
            flash(f"Erreur lors de l'inscription : {e}", 'error')
            db.session.rollback()

    return render_template('register.html')