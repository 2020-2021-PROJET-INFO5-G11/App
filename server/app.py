import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

SORTIES = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Rando entre copains',
        'type': 'Sport',
        'priv': True,
    },
    {
        'id': uuid.uuid4().hex,
        'nom': 'Harry Potter and the Philosopher\'s Stone',
        'type': 'Cinéma',
        'priv': False,
    },
    {
        'id': uuid.uuid4().hex,
        'nom': 'Balade au PPM',
        'type': 'Autre',
        'priv': True,
    }
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def remove_sortie(sortie_id):
    for sortie in SORTIES:
        if sortie['id'] == sortie_id:
            SORTIES.remove(sortie)
            return True
    return False


@app.route('/sorties', methods=['GET', 'POST'])
def all_sorties():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        SORTIES.append({
            'id': uuid.uuid4().hex,
            'nom': post_data.get('nom'),
            'type': post_data.get('type'),
            'priv': post_data.get('priv')
        })
        response_object['message'] = 'Sortie ajoutée!'
    else:
        response_object['sorties'] = SORTIES
    return jsonify(response_object)


@app.route('/sorties/<sortie_id>', methods=['PUT', 'DELETE'])
def single_sortie(sortie_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_sortie(sortie_id)
        SORTIES.append({
            'id': uuid.uuid4().hex,
            'nom': post_data.get('nom'),
            'type': post_data.get('type'),
            'priv': post_data.get('priv')
        })
        response_object['message'] = 'Sortie updated!'
    if request.method == 'DELETE':
        remove_sortie(sortie_id)
        response_object['message'] = 'Sortie removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
