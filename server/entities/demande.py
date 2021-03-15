from flask import make_response, abort
from datetime import datetime
from flask_login import current_user, login_required

from config import db
from models import Demande, User, Groupe, DemandeSchema


def get_all():
    """
    requête associée:
        /demandes
    """

    # Query the database for all the notes
    demandes = Demande.query.order_by(db.desc(Demande.timestamp)).all()

    # Serialize the list of notes from our data
    demande_schema = DemandeSchema(many=True)
    return demande_schema.dump(demandes)


def get_groupe_demandes(id_groupe):
    """
    requête associée:
        /groupe/{id_groupe}/demandes
    paramètres :
        id_groupe : id du groupe dont on récupère les demandes d'ajout
    """

    demandes = Demande.query.filter(Demande.id_groupe == id_groupe).order_by(db.desc(Demande.timestamp)).all()

    demande_schema = DemandeSchema(many=True)
    return demande_schema.dump(demandes)

def get_groupe_single_demande(id_groupe, id_demande):
    """
    requête associée:
        /groupe/{id_groupe}/demandes/{id_demande}
    paramètres :
        id_groupe : id du groupe dont on récupère la demande d'ajout
        id_demane : id de la demande d'ajout à récupérer
    """

    demandes = Demande.query.filter(Demande.id_groupe == id_groupe, Demande.id_demande == id_demande).order_by(db.desc(Demande.timestamp)).all()

    demande_schema = DemandeSchema(many=True)
    return demande_schema.dump(demandes)

@login_required
def add_to_groupe(id_groupe, id):                        # Demande d'ajout d'un membre à un groupe
    """
    requête associée:
        /groupe/{id_groupe}/demandes
    parametres :
        id_groupe : id du groupe où l'on veut ajouter l'utilisateur
        id : id de l'utilisateur à ajouter
    """

    groupe = Groupe.query.filter(
        Groupe.id_groupe == id_groupe).one_or_none()

    if groupe is None:
        abort(404, f'Groupe not found for Id: {id_groupe}')

    new_member = User.query.filter(
        User.id == id).one_or_none()

    if new_member is None:
        abort(404, f'User not found for Id: {id}')

    d = {
        'id_user': id,
        'id_groupe': id_groupe,
        'id_owner': current_user.id
    }

    schema = DemandeSchema()
    new_demande = schema.load(d, session=db.session)


    new_member.demandes.append(new_demande)
    groupe.demandes.append(new_demande)
    
    db.session.add(new_demande)
    db.session.commit()
    return schema.dump(new_demande), 201


@login_required
def accept(id_groupe):                        # Accepter ajout à un groupe
    """
    requête associée:
        /groupe/{id_groupe}/membres
    parametres :
        id_groupe : id du groupe
    """

    groupe = Groupe.query.filter(
        Groupe.id_groupe == id_groupe).one_or_none()

    if groupe is None:
        abort(404, f'Groupe not found for Id: {id_groupe}')

    demande = Demande.query.filter(Demande.id_groupe == id_groupe).filter(
        Demande.id_user == current_user.id).one_or_none()

    if demande is None:
        abort(404, f'Demande not found')
    
    groupe.nbMembres += 1
    groupe.demandes.remove(demande)
    current_user.demandes.remove(demande)
    current_user.groupes.append(groupe)
    db.session.add(current_user)
    db.session.delete(demande)
    db.session.commit()

    return 201

@login_required
def refuse(id_groupe):                        # Refuser ajout à un groupe
    """
    requête associée:
        /groupe/{id_groupe}/demandes
    parametres :
        id_groupe : id du groupe où l'on veut ajouter l'utilisateur
    """

    demande = Demande.query.filter(Demande.id_groupe == id_groupe).filter(
        Demande.id_user == current_user.id).one_or_none()

    if demande is None:
        abort(404, f'Demande not found')
    
    db.session.delete(demande)
    db.session.commit()

    return 201