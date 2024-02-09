from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class InscriptionForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mot_de_passe = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Inscription')


class createMovieForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])
    realisateur = StringField('Realisateur', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    submit = SubmitField('Ajouter')