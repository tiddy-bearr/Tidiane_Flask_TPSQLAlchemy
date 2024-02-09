#FADHLAOUI MOHAMED-AMINE

from flask import Blueprint, render_template
from .forms import InscriptionForm
from .database import db
from .models import utilisateur, Film, Auteur, Livre

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     form = InscriptionForm()
#     # opérations pour enregistrer le formulaire
#     if form.validate_on_submit():

#         new_user = Utilisateur(
#             nom=form.nom.data,
#             email=form.email.data,
#         )

#         db.session.add(new_user)
#         db.session.commit()
#         return render_template('index.html')
#     return render_template('inscription.html', form=form)


# @main.route('/ajout-film')
# def add_film():
#     film =  Film(
#         titre="Tidiane",
#         realisateur="die hard",
#         annee_sortie=1990,
#         genre="action",
#         genres="actions"
#     )
#     db.session.add(film)
#     db.session.commit()
#     return render_template('index.html')


@main.route('/ajout-auteur')
def add_auteur():
    auteur = Auteur(
        nom="Tidiane",
        date_naissance="1990-01-01",
        nationalite="senegal"
    )
    db.session.add(auteur)
    db.session.commit()
    return render_template('index.html')

@main.route('/ajout-livre')
def add_livre():
    auteur = Auteur.query.filter_by(nom="Tidiane").first()
    livre = Livre(
        titre="Titre du livre",
        date_publication="2022-01-01",
        auteur=auteur   
    )
    db.session.add(livre)
    db.session.commit()
    return render_template('index.html')


@main.route('/ajout-utilisateurs')
def add_utilisateurs():
    utilisateurs = [
        utilisateur(nom="John Doe", email="john@example.com"),
        utilisateur(nom="Jane Smith", email="jane@example.com"),
        utilisateur(nom="Alice Johnson", email="alice@example.com")
    ]
    db.session.add_all(utilisateurs)
    db.session.commit()
    return render_template('index.html')








# trois insertions avec la fonction add_film
# add_film("Le Parrain", "Francis Ford Coppola", 1972, "Drame", "Drame, Policier")
# add_film("Le Parrain 2", "Francis Ford Coppola", 1974, "Drame", "Drame, Policier")
# add_film("Le Parrain 3", "Francis Ford Coppola", 1990, "Drame", "Drame, Policier")


