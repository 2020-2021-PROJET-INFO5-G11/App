import os
from config import db
from models import Sortie
from models import User

# Data to initialize database with
SORTIES = [
    {
        'id_sortie': 1,
        'nom': 'Rando entre copains',
        'location': 'Monteynard',
        'date': '',
        'heure': '',
        'duree': '',
        'point_rdv': 'Polytech',
        'capaciteMin': 0,
        'capaciteMax': 10,
        'privee': True,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': '',
        'nbInscrits': 3,
        'description': '',
        'dateLimite': '',
        'commentaires': ''
    },
    {
        'id_sortie': 2,
        'nom': 'Harry Potter and the Philosopher\'s Stone',
        'location': 'Pathé Chavant',
        'date': '',
        'heure': '',
        'duree': '',
        'point_rdv': 'Polytech',
        'capaciteMin': 3,
        'capaciteMax': 5,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Cinéma',
        'photo': '',
        'nbInscrits': 2,
        'description': '',
        'dateLimite': '',
        'commentaires': ''

    },
    {
        'id_sortie': 3,
        'nom': 'Balade au PPM',
        'location': 'Parc Paul Mistral',
        'date': '',
        'heure': '',
        'duree': '',
        'point_rdv': 'Polytech',
        'capaciteMin': 1,
        'capaciteMax': 3,
        'privee': True,
        'id_groupe': None,
        'typeSortie': 'Autre',
        'photo': '',
        'nbInscrits': 1,
        'description': '',
        'dateLimite': '',
        'commentaires': ''
    }
]

USERS = []

# Delete database file if it exists currently
if os.path.exists('entities.db'):
    os.remove('entities.db')

# Create the database
db.create_all()

# Iterate over the SORTIE structure and populate the database
for sort in SORTIES:
    s = Sortie(id_sortie=sort['id_sortie'], nom=sort['nom'], location=sort['location'], date=sort['date'], \
        heure=sort['heure'], duree=sort['duree'], point_rdv=sort['point_rdv'], capaciteMin=sort['capaciteMin'], \
        capaciteMax=sort['capaciteMax'], privee=sort['privee'], id_groupe=sort['id_groupe'], \
        typeSortie=sort['typeSortie'], photo=sort['photo'], nbInscrits=sort['nbInscrits'], \
        description=sort['description'], dateLimite=sort['dateLimite'], commentaires=sort['commentaires'])
    db.session.add(s)

for user in USERS:
    u = User(id_user=user['id_user'], pseudo=user['pseudo'], prenom=user['prenom'], nom=user['nom'], \
        email=user['email'], photo=user['photo'], dateNaissance=user['dateNaissance'], ville=user['ville'], \
        preferences=user['preferences'], sexe=user['sexe'], bio=user['bio'], activites_a_venir=user['activites_a_venir'], \
        activites_finies=user['activites_finies'], activites_organisees=user['activites_organisees'], role=user['role'], \
        feedbacks=user['feedbacks'])
    db.session.add(u)

db.session.commit()