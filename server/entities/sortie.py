from flask import make_response, abort
from datetime import datetime

from config import db
from models import Sortie, SortieSchema, User, Commentaire


def read_all_sorties():
    """
    requête associée:
        /sortie
    """

    sorties = (
        Sortie.query
        .outerjoin(Commentaire).outerjoin(User)
        .all()
    )
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)


def read_one_sortie_by_id(id_sortie):
    """
    requête associée:
        /sortie/{id_sortie}
    paramètres :
        id_sortie : id de la sortie à lire
    """

    sortie = (
        Sortie.query.filter(Sortie.id_sortie == id_sortie)
        .outerjoin(Commentaire).outerjoin(User)
        .one_or_none()
    )

    if sortie is not None:
        sortie_schema = SortieSchema()
        return sortie_schema.dump(sortie)
    else:
        abort(404, f'Sortie not found for id: {id_sortie}')


def create(sortie):
    """
    requête associée:
        /sortie
    paramètres :
        sortie : id de la sortie à créer (format JSON)
    """

    id = sortie.get('id_sortie')
    if Sortie.query.get(id) is not None:
        abort(409, f'id {id} is already used')

    nom = sortie.get('nom')
    typeSortie = sortie.get('typeSortie')

    existing_sortie = Sortie.query \
        .filter(Sortie.nom == nom) \
        .filter(Sortie.typeSortie == typeSortie) \
        .one_or_none()

    if existing_sortie is None:
        schema = SortieSchema()
        new_sortie = schema.load(sortie, session=db.session)

        db.session.add(new_sortie)
        db.session.commit()

        return schema.dump(new_sortie), 201

    else:
        abort(409, f'Sortie {nom} ({typeSortie}) exists already')


def update(id_sortie, sortie):
    """
    requête associée:
        /sortie/{id_sortie}
    paramètres :
        id_sortie : id de la sortie à modifier
        sortie : nouvelles valeurs de la sortie une fois modifiée (format JSON)
    """

    update_sortie = Sortie.query.filter(
        Sortie.id_sortie == id_sortie
    ).one_or_none()

    if update_sortie is None:
        abort(404, f'Sortie not found for Id: {id_sortie}')

    else:
        schema = SortieSchema()
        update = schema.load(sortie, session=db.session)

        update.id_sortie = update_sortie.id_sortie

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_sortie)

        return data, 201


def delete(id_sortie):
    """
    requête associée:
        /sortie/{id_sortie}
    paramètres :
        id_sortie : id de la sortie à supprimer
    """

    sortie = Sortie.query.filter(Sortie.id_sortie == id_sortie).one_or_none()

    if sortie is not None:
        db.session.delete(sortie)
        db.session.commit()
        return make_response(
            "Sortie {id_sortie} deleted".format(id_sortie=id_sortie), 204
        )
    else:
        abort(404, "Sortie not found for Id: {id_sortie}".format(id_sortie=id_sortie))


def get_sorties_by_search(search):
    """
    requête associée:
        /search/{search}
    paramètres :
        search : nom ou partie du nom des sorties à renvoyer
    """

    sorties = Sortie.query.filter(Sortie.nom.contains(search) | Sortie.typeSortie.contains(search) | Sortie.id_sortie.contains(search))
    
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties), 200

def get_sorties_by_type(type_sortie):
    """
    requête associée:
        /filter/{type_sortie}
        paramètres :
        type_sortie : type ou partie du type de sortie à renvoyer
    """

    sorties = Sortie.query.filter(Sortie.typeSortie.contains(type_sortie))

    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties), 200