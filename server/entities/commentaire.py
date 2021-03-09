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

def get_activity_single_comment(id_sortie, id_com):
    coms = Commentaire.query.filter(Commentaire.id_sortie == id_sortie, Commentaire.id_commentaire == id_com).order_by(db.desc(Commentaire.timestamp)).all()

    com_schema = ComSchema(many=True)
    return com_schema.dump(coms)


def comment(id_sortie, com):
    c = Commentaire(
        contenu=com,
        id_sortie=id_sortie
    )

    db.session.add(c)
    db.session.commit()

    return 201


def update(id_sortie, id_com, com):
    update_commentaire = Commentaire.query.filter(
        Commentaire.id_sortie == id_sortie, Commentaire.id_commentaire == id_com
    ).one_or_none()

    if update_commentaire is None:
        abort(
            404,
            f'Commentaire not found for Id: {id_com}',
        )

    else:

        c = Commentaire(
        contenu=com,
        id_commentaire=id_com,
        id_sortie=id_sortie
        )   

        db.session.merge(c)
        db.session.commit()

        return 200


def delete(id_sortie, id_com):
    commentaire = Commentaire.query.filter(Commentaire.id_sortie == id_sortie, Commentaire.id_commentaire == id_com).one_or_none()

    if commentaire is not None:
        db.session.delete(commentaire)
        db.session.commit()
        return make_response(
            "Commentaire {id_commentaire} deleted".format(id_commentaire=id_com), 200
        )

    else:
        abort(
            404,
            "Commentaire not found for Id: {id_commentaire}".format(id_commentaire=id_com),
        )
