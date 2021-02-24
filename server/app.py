from flask import Flask, jsonify, request

from config import *
from models import Sortie, SortieSchema

SORTIES = [
    {
        'name': 'Rando entre copains',
        'type': 'Sport',
        'priv': True,
    },
    {
        'nom': 'Harry Potter and the Philosopher\'s Stone',
        'type': 'Cinéma',
        'priv': False,
    },
    {
        'nom': 'Balade au PPM',
        'type': 'Autre',
        'priv': True,
    }
]

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


"""
# home
@app.route('/')
def home():
    return 'Ceci est la racine'

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
"""

if __name__ == '__main__':
    app.run(host='localhost')
