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


def create(com):
    id = com.get('id_commentaire')
    if Commentaire.query.get(id) is not None:
        abort(409, f'id {id} is already used')

    schema = ComSchema()
    new_com = schema.load(com, session=db.session)

    db.session.add(new_com)
    db.session.commit()

    return schema.dump(new_com), 201
    