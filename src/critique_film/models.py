# importer l'instanciation db de SQLAlchemy
from .database import db
from datetime import datetime

# class Utilisateur(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nom = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     mot_de_passe_hash = db.Column(db.String(120), nullable=False)
#     mot_de_passe = db.Column(db.String(120), nullable=False)
#     critiques= db.relationship('Critique', backref='utilisateur', lazy='dynamic')

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    realisateur = db.Column(db.String(100))
    annee_sortie = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    genres = db.Column(db.String(100))
    id_critique = db.Column(db.Integer, db.ForeignKey('critique.id'))
    critiques = db.relationship('Critique', backref='film')



class Critique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenu = db.Column(db.Text, nullable=False)
    date_post = db.Column(db.DateTime, default=datetime.utcnow)
    date_posts = db.Column(db.DateTime, default=datetime.utcnow)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))


class Auteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.Date)
    nationalite = db.Column(db.String(100))

class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre= db.Column(db.String(100), nullable=False)
    date_publication = db.Column(db.Date)
    auteur = db.relationship('Auteur', backref='livre')
    id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id'))


# class Livre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     titre= db.Column(db.String(100), nullable=False)
#     date_publication = db.Column(db.Date)
#     genre= db.Column(db.String(100))
#     id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id'))
#     auteur = db.relationship('Auteur', backref='livre')


class utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)


class Emprunt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_emprunt = db.Column(db.Date)
    date_retour = db.Column(db.Date)
    id_livre = db.Column(db.Integer, db.ForeignKey('livre.id'))
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    date_emprunts = db.Column(db.Date)
    date_retours = db.Column(db.Date)

# class Emprunt(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_emprunt = db.Column(db.Date)
#     date_retour = db.Column(db.Date)
#     id_livre = db.Column(db.Integer, db.ForeignKey('livre.id'))
#     id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
#     date_emprunts = db.Column(db.Date)
#     date_retours = db.Column(db.Date)



