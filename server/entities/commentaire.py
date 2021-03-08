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


def create(id_sortie, contenu):

    sortie = Sortie.query.filter(Sortie.id_sortie == id_sortie).one_or_none()

    if sortie is None:
        abort(404, f'Sortie not found for id: {id_sortie}')

    """com = Commentaire(
        contenu = contenu, 
        timestamp = datetime.now().strftime(("%Y-%m-%d %H:%M:%S")),
    )
"""

    sortie.commentaires.append(
        Commentaire(
            contenu=contenu,
            #timestamp="2021-03-04 23:24:45"#datetime.now().strftime(("%Y-%m-%d %H:%M:%S")),
        )
    )


    """
    schema = ComSchema()
    new_com = schema.load(com, session=db.session)
    """
    #db.session.add(new_com)
    db.session.commit()

    #return schema.dump(new_com), 201
    
    return 201
    