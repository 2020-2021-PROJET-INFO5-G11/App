from flask import make_response, abort
from datetime import datetime
from flask_login import current_user, login_required

from config import db
from models import Groupe, Sortie, User, GroupeSchema


def get_all():
    """
    requête associée:
        /groupe
    """

    # Query the database for all the notes
    groupes = Groupe.query.all()

    # Serialize the list of notes from our data
    groupe_schema = GroupeSchema(many=True)
    return groupe_schema.dump(groupes)


def get_user_groupes(id):
    """
    requête associée:
        /user/{id}/groupe
    paramètres :
        id_user : id de l'utilisateur dont on récupère les groupes
    """

    groupes = Groupe.query.filter(Groupe.id_user == id).all()

    groupe_schema = GroupeSchema(many=True)
    return groupe_schema.dump(groupes)


@login_required
def create(groupe):
    """
    requête associée:
        /groupe
    paramètres :
        user : données du groupe à créer (format JSON)
    """

    id_groupe = groupe.get('id_groupe')
    if Groupe.query.get(id_groupe) is not None:
        abort(409, f'id {id_groupe} is already used for another group')

    nom = groupe.get('nom')
    description = groupe.get('description')

    existing_groupe = Groupe.query \
        .filter(Groupe.nom == nom) \
        .filter(Groupe.description == description) \
        .one_or_none()

    if existing_groupe is not None:
        abort(409, f'Group {nom} exists already')
    
    schema = GroupeSchema()

    new_groupe = schema.load(groupe, session=db.session)
    new_groupe.nbMembres += 1
    new_groupe.id_owner = current_user.id
    new_groupe.owner = current_user
    current_user.groupes.append(new_groupe)
    db.session.add(new_groupe)
    db.session.commit()

    return schema.dump(new_groupe), 201


def update(id_groupe, groupe):
    """
    requête associée:
        /groupe/{id_groupe}
    paramètres :
        id_groupe : id du groupe à modifier
        groupe : nouvelles valeurs du groupe une fois modifié (format JSON)
    """

    update_groupe = Groupe.query.filter(
        Groupe.id_groupe == id_groupe
    ).one_or_none()

    if update_groupe is None:
        abort(404, f'Group not found for id: {id_groupe}')
    else:
        schema = GroupeSchema()
        update = schema.load(groupe, session=db.session)

        update.id_groupe = update_groupe.id_groupe

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_groupe)
        return data, 201


def delete(id_groupe):
    """
    requête associée:
        /groupe/{id}
    paramètres :
        id_groupe : id du groupe à supprimer
    """

    groupe = Groupe.query.filter(Groupe.id_groupe == id_groupe).one_or_none()

    if groupe is not None:
        db.session.delete(groupe)
        db.session.commit()
        return make_response(
            "Groupe {id_groupe} deleted", 204)
    else:
        abort(404, f'Group not found for id: {id_groupe}')


def get_groupes_by_search(search):
    """
    requête associée:
        /search_groupe/{search}
    paramètres :
        search : nom ou partie du nom des groupes à renvoyer
    """

    groupes = Groupe.query.filter(Groupe.nom.contains(search) | Groupe.description.contains(search) | Groupe.id_groupe.contains(search))

    groupe_schema = GroupeSchema(many=True)
    return groupe_schema.dump(groupes)