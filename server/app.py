import uuid
from flask import Flask, jsonify, request

from config import app
from models import Sortie, SortieSchema

"""
GROUPES = [
    {
        'id': uuid.uuid4().hex,
        'nom': 'Popo',
        'membres': '',
        'créateur': '',
        'activités': [
            {
        'id': uuid.uuid4().hex,
        'nom': 'Balade au PPM',
        'lieu': 'Parc Paul Mistral',
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
        ],
        'description': 'test',
    },
]

COMMENTAIRES = [
    {
        'utilisateur': 'Rim',
        'contenu': 'Ceci est un commentaire',
        'date': '',
        'réponses': '',
    },
]

UTILISATEURS = [
    {
        'id': uuid.uuid4().hex,
        'pseudo': 'pseudoExemple',
        'prénom': 'Rim',
        'nom': 'El Jraidi',
        'email': 'exemple@gmail.com',
        'photo': '',
        'dateNaissance': '',
        'ville': 'Grenoble',
        'préférences': '',
        'sexe': 'Femme',
        'bio': 'cc haha lol',
        'activitésAVenir': '',
        'activitésFaites': 'Autre',
        'activitésOrganisées': '',
        'role': '',
        'feedbacks': '',
    },
]
"""

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

def remove_utilisateur(utilisateur_id):
    for utilisateur in UTILISATEURS:
        if utilisateur['id'] == utilisateur_id:
            UTILISATEURS.remove(utilisateur)
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
            'lieu': post_data.get('lieu'),
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

@app.route('/utilisateurs', methods=['GET', 'POST'])
def all_utilisateurs():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        UTILISATEURS.append({
            'id': uuid.uuid4().hex,
            'pseudo': post_data.get('pseudo'),
            'prénom': post_data.get('prénom'),
            'nom': post_data.get('nom'),
            'email': post_data.get('email'),
            'photo': post_data.get('photo'),
            'dateNaissance': post_data.get('dateNaissance'),
            'ville': post_data.get('ville'),
            'préférences': post_data.get('préférences'),
            'sexe': post_data.get('sexe'),
            'bio': post_data.get('bio'),
            'activitésAVenir': post_data.get('activitésAVenir'),
            'activitésFaites': post_data.get('activitésFaites'),
            'activitésOrganisées': post_data.get('activitésOrganisées'),
            'role': post_data.get('role'),
            'feedbacks': post_data.get('feedbacks'),
        })
        response_object['message'] = 'Utilisateur ajouté!'
    else:
        response_object['utilisateurs'] = UTILISATEURS
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
            'lieu': post_data.get('lieu'),
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

@app.route('/utilisateurs/<utilisateur_id>', methods=['PUT', 'DELETE'])
def single_utilisateur(utilisateur_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_utilisateur(utilisateur_id)
        UTILISATEURS.append({
            'id': uuid.uuid4().hex,
            'pseudo': post_data.get('pseudo'),
            'prénom': post_data.get('prénom'),
            'nom': post_data.get('nom'),
            'email': post_data.get('email'),
            'photo': post_data.get('photo'),
            'dateNaissance': post_data.get('dateNaissance'),
            'ville': post_data.get('ville'),
            'préférences': post_data.get('préférences'),
            'sexe': post_data.get('sexe'),
            'bio': post_data.get('bio'),
            'activitésAVenir': post_data.get('activitésAVenir'),
            'activitésFaites': post_data.get('activitésFaites'),
            'activitésOrganisées': post_data.get('activitésOrganisées'),
            'role': post_data.get('role'),
            'feedbacks': post_data.get('feedbacks'),
        })
        response_object['message'] = 'Utilisateur mise à jour!'
    if request.method == 'DELETE':
        remove_utilisateur(utilisateur_id)
        response_object['message'] = 'Utilisateur supprimé!'
    return jsonify(response_object)
"""

if __name__ == '__main__':
    app.run(host='localhost')
