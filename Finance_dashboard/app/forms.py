from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField
from wtforms.validators import DataRequired, NumberRange, Length


class TransactionForm(FlaskForm):
    """Formulaire pour ajouter une transaction (revenu ou dépense)."""

    name = StringField('Nom de la transaction', validators=[DataRequired(), Length(min=3, max=100)])
    amount = DecimalField('Montant', validators=[DataRequired(), NumberRange(min=0.01)], places=2)
    transaction_type = SelectField('Type de transaction', choices=[('income', 'Revenu'), ('expense', 'Dépense')],
                                   validators=[DataRequired()])
    currency = SelectField('Devise', choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('JPY', 'JPY')],
                           default='USD')
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')

