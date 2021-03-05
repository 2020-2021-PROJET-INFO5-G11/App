from flask import make_response, abort
from datetime import datetime

from config import db
from models import Commentaire, Sortie, User, ComSchema


def get_all():
    # Query the database for all the notes
    coms = Commentaire.query.order_by(db.desc(Commentaire.timestamp)).all()

    # Serialize the list of notes from our data
    com_schema = ComSchema(many=True)
    return com_schema.dump(coms)

def get_activity_comments(id_sortie):
    coms = Commentaire.query.filter(Commentaire.id_sortie == id_sortie).order_by(db.desc(Commentaire.timestamp)).all()

    com_schema = ComSchema(many=True)
    return com_schema.dump(coms)


def create(com):
    id = com.get('id_commentaire')
    if Commentaire.query.get(id) is not None:
        abort(409, f'id {id} is already used')

    schema = ComSchema()
    new_com = schema.load(com, session=db.session)

    db.session.add(new_com)
    db.session.commit()

    return schema.dump(new_com), 201


def update(id_commentaire, commentaire):
    update_commentaire = Commentaire.query.filter(
        Commentaire.id_commentaire == id_commentaire
    ).one_or_none()

    if update_commentaire is None:
        abort(
            404,
            f'Commentaire not found for Id: {id_commentaire}',
        )

    else:

        schema = ComSchema()
        update = schema.load(commentaire, session=db.session)

        update.id_commentaire = update_commentaire.id_commentaire

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_commentaire)

        return data, 200


def delete(id_commentaire):
    commentaire = Commentaire.query.filter(Commentaire.id_commentaire == id_commentaire).one_or_none()

    if commentaire is not None:
        db.session.delete(commentaire)
        db.session.commit()
        return make_response(
            "Commentaire {id_commentaire} deleted".format(id_commentaire=id_commentaire), 200
        )

    else:
        abort(
            404,
            "Commentaire not found for Id: {id_commentaire}".format(id_commentaire=id_commentaire),
        )
