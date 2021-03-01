from flask import make_response, abort

from config import db
from datetime import datetime
from models import Sortie
from models import SortieSchema

"""
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
"""

def read_all_sorties():
    sorties = Sortie.query.all()

    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)


def read_one_sortie_by_id(id_sortie):
    sortie = Sortie.query.get(id_sortie)

    if sortie is not None:
        sortie_schema = SortieSchema()
        return sortie_schema.dump(sortie)
    else:
        abort(404, f'Sortie not found for id: {id_sortie}')

def create(sortie):
    """
    This function creates a new sortie
    based on the passed-in sortie data

    :param sortie:    sortie to create
    :return:        201 on success, 406 on sortie exists
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
        abort(409, f'Sortie {nom} {typeSortie} exists already')

def update(id_sortie, sortie):
    update_sortie = Sortie.query.filter(
        Sortie.id_sortie == id_sortie
    ).one_or_none()

    if update_sortie is None:
        abort(
            404,
            "Sortie not found for Id: {sortie_id}".format(sortie_id=sortie_id),
        )

    else:

        schema = SortieSchema()
        update = schema.load(sortie, session=db.session)

        update.id_sortie = update_sortie.id_sortie

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_sortie)

        return data, 200


def delete(id_sortie):
    sortie = Sortie.query.filter(Sortie.id_sortie == id_sortie).one_or_none()

    if sortie is not None:
        db.session.delete(sortie)
        db.session.commit()
        return make_response(
            "Sortie {id_sortie} deleted".format(id_sortie=id_sortie), 200
        )

    else:
        abort(
            404,
            "Sortie not found for Id: {id_sortie}".format(id_sortie=id_sortie),
        )


def get_sorties_by_search(search):
    sorties = Sortie.query.filter(Sortie.nom.contains(search) | Sortie.typeSortie.contains(search) | Sortie.id_sortie.contains(search))

    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)