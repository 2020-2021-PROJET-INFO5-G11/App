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


def read_one_sortie_by_id(id):
    sortie = Sortie.query.get(id)

    if sortie is not None:
        sortie_schema = SortieSchema()
        return sortie_schema.dump(sortie)
    else:
        abort(404, 'Sortie not found for id: {id}'.format(id=id))