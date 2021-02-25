import os
from config import db
from models import Sortie

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
        'capaciteMin': '',
        'capaciteMax': '',
        'privee': True,
        'id_groupe': '',
        'typeSortie': 'Sport',
        'photo': '',
        'nbInscrits': '',
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
        'capaciteMin': '',
        'capaciteMax': '',
        'privee': False,
        'id_groupe': '',
        'typeSortie': 'Cinéma',
        'photo': '',
        'nbInscrits': '',
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
        'capaciteMin': '',
        'capaciteMax': '',
        'privee': True,
        'id_groupe': '',
        'typeSortie': 'Autre',
        'photo': '',
        'nbInscrits': '',
        'description': '',
        'dateLimite': '',
        'commentaires': ''
    }
]

# Delete database file if it exists currently
if os.path.exists('entities.db'):
    os.remove('entities.db')

# Create the database
db.create_all()

# Iterate over the SORTIE structure and populate the database
for sort in SORTIES:
    s = Sortie(nom=sort['nom'], typeSortie=sort['typeSortie'])
    #s = sort.Sortie()
    db.session.add(s)

db.session.commit()