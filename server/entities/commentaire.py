from flask import make_response, abort
from datetime import datetime
from flask_login import current_user, login_required

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


@login_required
def comment(id_sortie, com):

    sortie = Sortie.query.filter(Sortie.id_sortie == id_sortie).one_or_none()

    if sortie is None:
        abort(404, f'Sortie not found for id: {id_sortie}')

    c = {
        'contenu': com,
        'id_sortie': id_sortie,
        'id_user': current_user.id
    }
    
    schema = ComSchema()
    new_com = schema.load(c, session=db.session)
    
    db.session.add(new_com)
    db.session.commit()
    return schema.dump(new_com), 201


def update(id_sortie, id_com, com):
    update_com = (
        Commentaire.query
        .filter(Commentaire.id_sortie == id_sortie)
        .filter(Commentaire.id_commentaire == id_com)
        .one_or_none()
    )

    if update_com is None:
        abort(404, f'Commentaire not found in sortie {id_sortie} for Id: {id_com}')

    c = {
        'contenu': com
    }

    schema = ComSchema()
    update=schema.load(c, session=db.session)

    update.id_commentaire = update_com.id_commentaire
    update.id_user = update_com.id_user
    update.id_sortie = update_com.id_sortie
    update.timestamp = update_com.timestamp

    db.session.merge(update)
    db.session.commit()
    return schema.dump(update_com), 201


def delete(id_sortie, id_com):
    commentaire = Commentaire.query.filter(Commentaire.id_sortie == id_sortie, Commentaire.id_commentaire == id_com).one_or_none()

    if commentaire is not None:
        db.session.delete(commentaire)
        db.session.commit()
        return make_response(f'Commentaire {id_com} deleted', 200)
    else:
        abort(404, f'Commentaire not found in sortie {id_sortie} for Id: {id_com}')
