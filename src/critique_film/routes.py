#FADHLAOUI MOHAMED-AMINE

from flask import Blueprint, render_template
from .forms import InscriptionForm
from .database import db
from .models import Chambre, Reservation,Client
from flask import request, jsonify

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/api/chambres/disponibles', methods=['GET'])
def get_available_chambres():
    date_arrivee = request.args.get('date_arrivee')
    date_depart = request.args.get('date_depart')

    # Vérifier les chambres disponibles entre les dates spécifiées
    chambres_disponibles = Chambre.query.filter(~Chambre.reservations.any(
        (Reservation.date_arrivee <= date_depart) & (Reservation.date_depart >= date_arrivee)
    )).all()

    # Construire la réponse JSON
    response = []
    for chambre in chambres_disponibles:
        response.append({
            "id": chambre.id,
            "numero": chambre.numero,
            "type": chambre.type,
            "prix": chambre.prix
        })

    return jsonify(response)


@main.route('/api/reservations', methods=['POST'])
def create_reservation():
    id_client = request.json.get('id_client')
    id_chambre = request.json.get('id_chambre')
    date_arrivee = request.json.get('date_arrivee')
    date_depart = request.json.get('date_depart')
    statut = request.json.get('statut')

    # Vérifier la disponibilité de la chambre pour les dates demandées
    chambre = Chambre.query.get(id_chambre)
    if chambre is None:
        return jsonify({"success": False, "message": "Chambre introuvable."}), 404

    else :
        # Créer la réservation
        reservation = Reservation(
            id_client=id_client,
            id_chambre=id_chambre,
            date_arrivee=date_arrivee,
            date_depart=date_depart,
            statut=statut
        )
        db.session.add(reservation)
        db.session.commit()
        return jsonify({"success": True, "message": "Réservation créée avec succès."}), 201


@main.route('/api/reservations/<int:id>', methods=['DELETE'])
def cancel_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation is None:
        return jsonify({"success": False, "message": "Réservation introuvable."}), 404

    db.session.delete(reservation)
    db.session.commit()
    return jsonify({"success": True, "message": "Réservation annulée avec succès."})





#check
@main.route('/api/chambres', methods=['POST'])
def add_chambre():
    numero = request.json.get('numero')
    type = request.json.get('type')
    prix = request.json.get('prix')

    chambre = Chambre(numero=numero, type=type, prix=prix)
    db.session.add(chambre)
    db.session.commit()

    return jsonify({"success": True, "message": "Chambre ajoutée avec succès."}), 201


@main.route('/api/chambres/<int:id>', methods=['PUT'])
def update_chambre(id):
    chambre = Chambre.query.get(id)
    if chambre is None:
        return jsonify({"success": False, "message": "Chambre introuvable."}), 404

    numero = request.json.get('numero')
    type = request.json.get('type')
    prix = request.json.get('prix')

    chambre.numero = numero
    chambre.type = type
    chambre.prix = prix

    db.session.commit()
    return jsonify({"success": True, "message": "Chambre mise à jour avec succès."})


@main.route('/api/chambres/<int:id>', methods=['DELETE'])
def delete_chambre(id):
    chambre = Chambre.query.get(id)
    if chambre is None:
        return jsonify({"success": False, "message": "Chambre introuvable."}), 404

    db.session.delete(chambre)
    db.session.commit()
    return jsonify({"success": True, "message": "Chambre supprimée avec succès."})


