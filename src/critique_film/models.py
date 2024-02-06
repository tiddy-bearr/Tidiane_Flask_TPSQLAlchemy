# importer l'instanciation db de SQLAlchemy
from .database import db

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(120), nullable=False)
    # critiques= db.relationship('Critique')


# class Film(db.Model):
#     pass

# class Critique(db.Model):
#     pass