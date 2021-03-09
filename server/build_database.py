import os
from datetime import datetime

from config import db
from models import Sortie
from models import User
from models import Commentaire

# Data to initialize database with
SORTIES = [
    {
        'nom': 'Randonnée à Monteynard',
        'lieu': 'Monteynard',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'Polytech Grenoble',
        'capaciteMin': 3,
        'capaciteMax': 10,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'randonnée',
        'nbInscrits': 1,
        'description': 'Ça vous dit de monter les voir la passerelle himalayenne du lac de Monteynard ?',
        'dateLimite': '2021-03-11',
        'commentaires': [
            ("C ou Montenar??!", "2019-01-07 22:47:54"),
            ("Chepa gro", "2019-01-08 20:17:31"),
            ("Wsh vs etes cons c marqué que c en hymalaya dans la description", "2019-01-08 22:02:54"),
        ],
    },
    {
        'nom': 'Harry Potter and the Philosopher\'s Stone',
        'lieu': 'Pathé Chavant',
        'date': '2021-03-04',
        'heure': '14:25',
        'duree': '02:30',
        'point_rdv': 'Polytech',
        'capaciteMin': 3,
        'capaciteMax': 8,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Cinéma',
        'photo': 'cinema',
        'nbInscrits': 1,
        'description': 'J\'ai un tarif de groupe pour aller voir ce filme au cinéma.',
        'dateLimite': '2021-03-03',
        'commentaires': [
            ("coucou", "2019-01-07 22:47:54")
        ],
    },
    {
        'nom': 'Balade au PPM',
        'lieu': 'Parc Paul Mistral',
        'date': '2021-03-15',
        'heure': '16:00',
        'duree': '02:00',
        'point_rdv': 'Polytech',
        'capaciteMin': 1,
        'capaciteMax': 3,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Autre',
        'photo': 'parc',
        'nbInscrits': 1,
        'description': 'La balade du Frémont',
        'dateLimite': '2021-03-14',
        'commentaires': [
            ("Richard le S mets nous 20 stp", "2021-03-04 23:24:45")
        ],
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
        description=sort['description'], dateLimite=sort['dateLimite'])

    for com in sort.get("commentaires"):
        contenu, timestamp = com
        s.commentaires.append(
            Commentaire(
                contenu=contenu,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )

    db.session.add(s)

for user in USERS:
    u = User(pseudo=user['pseudo'], password_hash=user['password_hash'], prenom=user['prenom'], nom=user['nom'], \
        email=user['email'], photo=user['photo'], dateNaissance=user['dateNaissance'], ville=user['ville'], \
        preferences=user['preferences'], sexe=user['sexe'], bio=user['bio'], sorties_a_venir=user['sorties_a_venir'], \
        sorties_finies=user['sorties_finies'], role=user['role'], \
        feedbacks=user['feedbacks'])
    db.session.add(u)

db.session.commit()