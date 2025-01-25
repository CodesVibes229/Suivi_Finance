### **`README.md`**

```markdown
# Suivi des Finances Personnelles

## Description
Ce projet permet de suivre les finances personnelles en enregistrant les transactions financières, telles que les revenus et les dépenses, et en affichant ces données sous forme de graphiques. L'utilisateur peut consulter un tableau de bord avec des visualisations détaillées de ses finances mensuelles. Le projet intègre également une gestion des devises en utilisant une API de taux de change.

## Fonctionnalités
- **Suivi des transactions** : Ajouter, modifier et supprimer des transactions financières (revenus et dépenses).
- **Tableau de bord** : Visualiser les transactions sous forme de graphiques interactifs (utilisant Chart.js et D3.js).
- **Gestion des devises** : Calculer les taux de change entre différentes devises en utilisant une API de taux de change.
- **Authentification** : Système de connexion et d'inscription pour les utilisateurs (en cours de développement).
- **Base de données** : Stockage des transactions dans une base de données MariaDB.

## Technologies utilisées
- **Backend** : Python avec Flask
- **Frontend** : JavaScript avec Chart.js, D3.js pour les graphiques
- **Base de données** : MariaDB
- **API de taux de change** : Utilisation d'une API pour obtenir les taux de change en temps réel
- **ORM** : SQLAlchemy pour la gestion de la base de données
- **Authentification** : Flask-Login pour la gestion des utilisateurs

## Installation

### Prérequis
- Python 3.x
- MariaDB
- Node.js (si nécessaire pour les graphiques frontend)

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/CodesVibes229/Suivi_Finance.git
   cd Suivi_Finance
   ```

2. **Créer et activer un environnement virtuel** :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Pour Linux/Mac
   venv\Scripts\activate     # Pour Windows
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données MariaDB** :
   - Crée une base de données dans MariaDB (par exemple `finances`).
   - Modifie le fichier `config.py` pour y ajouter les informations de connexion à MariaDB.

   Exemple de configuration dans `config.py` :
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/finances'
   ```
   Assurez vous de mettre vos informations concernant la base de données c'est à dire votre user, le mot de passe de votre user et surtout ne pas oublier de spécifier le nom de votre base de données

5. **Initialiser la base de données** :
   Si tu utilises **Flask-Migrate**, exécute les commandes suivantes pour initialiser et migrer la base de données :
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Lancer l'application Flask** :
   ```bash
   flask run
   ```

7. Accède à l'application via `http://127.0.0.1:5000`.

## Contributions

Les contributions sont les bienvenues ! Pour proposer une modification, veuillez ouvrir une **issue** ou une **pull request**.

## Auteurs

- **CodesVibes229** - Développeur principal


