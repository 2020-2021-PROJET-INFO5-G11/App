import os
from config import db
from models import Sortie
from models import User

# Data to initialize database with
SORTIES = [
    {
        'nom': 'Rando entre copains',
        'lieu': 'Monteynard',
        'date': None,
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
        'nom': 'Harry Potter and the Philosopher\'s Stone',
        'lieu': 'Pathé Chavant',
        'date': None,
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
        'nom': 'Balade au PPM',
        'lieu': 'Parc Paul Mistral',
        'date': None,
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
    s = Sortie(nom=sort['nom'], lieu=sort['lieu'], date=sort['date'], \
        heure=sort['heure'], duree=sort['duree'], point_rdv=sort['point_rdv'], capaciteMin=sort['capaciteMin'], \
        capaciteMax=sort['capaciteMax'], privee=sort['privee'], id_groupe=sort['id_groupe'], \
        typeSortie=sort['typeSortie'], photo=sort['photo'], nbInscrits=sort['nbInscrits'], \
        description=sort['description'], dateLimite=sort['dateLimite'], commentaires=sort['commentaires'])
    db.session.add(s)

for user in USERS:
    u = User(pseudo=user['pseudo'], password_hash=user['password_hash'], prenom=user['prenom'], nom=user['nom'], \
        email=user['email'], photo=user['photo'], dateNaissance=user['dateNaissance'], ville=user['ville'], \
        preferences=user['preferences'], sexe=user['sexe'], bio=user['bio'], activites_a_venir=user['activites_a_venir'], \
        activites_finies=user['activites_finies'], activites_organisees=user['activites_organisees'], role=user['role'], \
        feedbacks=user['feedbacks'])
    db.session.add(u)

db.session.commit()