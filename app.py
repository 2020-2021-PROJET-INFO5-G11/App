import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/home', methods=['GET'])
def home():
    return jsonify('pong!')

SORTIES = [
    {
        'name': 'Avenger',
        'type': 'Cinema',
        'priv': True
    },
    {
        'name': 'test',
        'type': 'Rando',
        'priv': False
    },
    {
        'name': 'Basket',
        'type': 'Sport',
        'priv': True
    }
]

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
            'name': post_data.get('name'),
            'type': post_data.get('type'),
            'priv': post_data.get('priv')
        })
        response_object['message'] = 'Sortie added!'
    else:
        response_object['sortie'] = SORTIES
    return jsonify(response_object)

    @app.route('/sorties/<sortie_id>', methods=['PUT', 'DELETE'])
def single_sortie(sortie_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_sortie(sortie_id)
        SORTIES.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
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