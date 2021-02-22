import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


SORTIES = [
    {
        'id': uuid.uuid4().hex,
        'nom': 'Rando entre copains',
        'location': 'Monteynard',
        'date': '',
        'heure': '',
        'durée': '',
        'rdv': 'Polytech',
        'capacityMin': '',
        'capacaityMax': '',
        'privée': True,
        'groupID': '',
        'type': 'Sport',
        'photo': '',
        'inscrits': '',
        'nbInscrits': '',
        'organisateurs': '',
        'description': '',
        'dateLimite': '',
        'commentaires': ''
    },
    {
        'id': uuid.uuid4().hex,
        'nom': 'Harry Potter and the Philosopher\'s Stone',
        'location': 'Pathé Chavant',
        'date': '',
        'heure': '',
        'durée': '',
        'rdv': 'Polytech',
        'capacityMin': '',
        'capacaityMax': '',
        'privée': False,
        'groupID': '',
        'type': 'Cinéma',
        'photo': '',
        'inscrits': '',
        'nbInscrits': '',
        'organisateurs': '',
        'description': '',
        'dateLimite': '',
        'commentaires': ''

    },
    {
        'id': uuid.uuid4().hex,
        'nom': 'Balade au PPM',
        'location': 'Parc Paul Mistral',
        'date': '',
        'heure': '',
        'durée': '',
        'rdv': 'Polytech',
        'capacityMin': '',
        'capacaityMax': '',
        'privée': True,
        'groupID': '',
        'type': 'Autre',
        'photo': '',
        'registered': '',
        'nbRegistered': '',
        'organisateurs': '',
        'description': '',
        'dateLimite': '',
        'commentaires': ''
    }
]

GROUPES = [
    {
        'id': uuid.uuid4().hex,
        'nom': 'Popo',
        'membres': '',
        'créateur': '',
        'activités': '',
        'description': 'test',
    },
]

COMMENTAIRES = [
    {
        'id': uuid.uuid4().hex,
        'utilisateur': 'Rim',
        'contenu': 'Ceci est un commentaire',
        'date': '',
        'réponses': '',
    },
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_sortie(sortie_id):
    for sortie in SORTIES:
        if sortie['id'] == sortie_id:
            SORTIES.remove(sortie)
            return True
    return False


def remove_groupe(groupe_id):
    for groupe in GROUPES:
        if groupe['id'] == groupe_id:
            GROUPES.remove(groupe)
            return True
    return False


def remove_commentaire(commentaire_id):
    for commentaire in COMMENTAIRES:
        if commentaire['id'] == commentaire_id:
            COMMENTAIRES.remove(commentaire)
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
            'location': post_data.get('location'),
            'date': post_data.get('date'),
            'heure': post_data.get('heure'),
            'durée': post_data.get('durée'),
            'rdv': post_data.get('rdv'),
            'capacityMin': post_data.get('capacityMin'),
            'capacaityMax': post_data.get('capacaityMax'),
            'privée': post_data.get('privée'),
            'groupID': post_data.get('groupID'),
            'type': post_data.get('type'),
            'photo': post_data.get('photo'),
            'inscrits': post_data.get('inscrits'),
            'nbInscrits': post_data.get('nbInscrits'),
            'organisateurs': post_data.get('organisateurs'),
            'description': post_data.get('description'),
            'dateLimite': post_data.get('dateLimite'),
            'commentaires': post_data.get('commentaires'),
        })
        response_object['message'] = 'Sortie ajoutée!'
    else:
        response_object['sorties'] = SORTIES
    return jsonify(response_object)


@app.route('/groupes', methods=['GET', 'POST'])
def all_groupes():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        GROUPES.append({
            'id': uuid.uuid4().hex,
            'nom': post_data.get('nom'),
            'membress': post_data.get('membres'),
            'créateur': post_data.get('créateur'),
            'activités': post_data.get('activités'),
            'description': post_data.get('description'),
        })
        response_object['message'] = 'Groupe créé!'
    else:
        response_object['groupes'] = GROUPES
    return jsonify(response_object)


@app.route('/commentaires', methods=['GET', 'POST'])
def all_commentaires():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        COMMENTAIRES.append({
            'id': uuid.uuid4().hex,
            'utilisateur': post_data.get('utilisateur'),
            'contenu': post_data.get('contenu'),
            'date': post_data.get('date'),
            'réponses': post_data.get('réponses'),
        })
        response_object['message'] = 'Commentaire ajouté!'
    else:
        response_object['commentaires'] = COMMENTAIRES
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
            'location': post_data.get('location'),
            'date': post_data.get('date'),
            'heure': post_data.get('heure'),
            'durée': post_data.get('durée'),
            'rdv': post_data.get('rdv'),
            'capacityMin': post_data.get('capacityMin'),
            'capacaityMax': post_data.get('capacaityMax'),
            'privée': post_data.get('privée'),
            'groupID': post_data.get('groupID'),
            'type': post_data.get('type'),
            'photo': post_data.get('photo'),
            'inscrits': post_data.get('inscrits'),
            'nbInscrits': post_data.get('nbInscrits'),
            'organisateurs': post_data.get('organisateurs'),
            'description': post_data.get('description'),
            'dateLimite': post_data.get('dateLimite'),
            'commentaires': post_data.get('commentaires'),
        })
        response_object['message'] = 'Sortie mise à jour!'
    if request.method == 'DELETE':
        remove_sortie(sortie_id)
        response_object['message'] = 'Sortie supprimée!'
    return jsonify(response_object)

@app.route('/groupes/<groupe_id>', methods=['PUT', 'DELETE'])
def single_groupe(groupe_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_groupe(groupe_id)
        GROUPES.append({
            'id': uuid.uuid4().hex,
            'nom': post_data.get('nom'),
            'membress': post_data.get('membres'),
            'créateur': post_data.get('créateur'),
            'activités': post_data.get('activités'),
            'description': post_data.get('description'),
        })
        response_object['message'] = 'Groupe mise à jour!'
    if request.method == 'DELETE':
        remove_groupe(groupe_id)
        response_object['message'] = 'Groupe supprimé!'
    return jsonify(response_object)


@app.route('/commentaires/<commentaire_id>', methods=['PUT', 'DELETE'])
def single_commentaire(commentaire_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_commentaire(commentaire_id)
        COMMENTAIRES.append({
            'id': uuid.uuid4().hex,
            'nom': post_data.get('nom'),
            'membress': post_data.get('membres'),
            'créateur': post_data.get('créateur'),
            'activités': post_data.get('activités'),
            'description': post_data.get('description'),
        })
        response_object['message'] = 'Commentaire mise à jour!'
    if request.method == 'DELETE':
        remove_commentaire(commentaire_id)
        response_object['message'] = 'Commentaire supprimé!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
