import os
from datetime import datetime

from config import db
from models import Sortie
from models import User
from models import Commentaire
from models import Groupe
from models import Demande


# Data to initialize database with
USERS = [
    {
        'password_hash': 'string',
        'prenom': 'Rim',
        'nom': 'El Jraidi',
        'email': 'rimeljraidi@uga.fr',
        'photo': 'string',
        'dateNaissance': '12-03-1998',
        'ville': 'Grenoble',
        'preferences': '',
        'sexe': 'Femme',
        'bio': 'J\'aime aller au ciné, et vous ?',
        'photo': '',
        'sorties_a_venir': [],
        'sorties_finies': [],
        'role': '',
        'feedbacks': '',
        'commentaires': [
            ("C'est quel genre de film ?", "2019-01-07 22:47:54"),
            ("test commentaire", "2019-01-08 20:17:31"),
            ("coucou", "2019-01-08 22:02:54"),
        ],
        'demandes': [],
    },
]

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
        'nbInscrits': 0,
        'description': 'Ça vous dit de monter les voir la passerelle himalayenne du lac de Monteynard ?',
        'dateLimite': '2021-03-11',
        'commentaires': [
            ("C'est ou Monteynard ?", "2019-01-07 22:47:54"),
            ("Je sais pas ", "2019-01-08 20:17:31"),
            ("C'est marqué dans la description", "2019-01-08 22:02:54"),
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
        'nbInscrits': 0,
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
        'nbInscrits': 0,
        'description': 'La balade du Frémont',
        'dateLimite': '2021-03-14',
        'commentaires': [
            ("Trop bien !", "2021-03-04 23:24:45")
        ],
    },
    {
        'nom': 'FootUS',
        'lieu': 'Terrain Nord du campus',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'Parking de Condillac',
        'capaciteMin': 3,
        'capaciteMax': 10,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'foot-us',
        'nbInscrits': 0,
        'description': 'Petit match ?',
        'dateLimite': '2021-03-11',
        'commentaires': [
            ("C'est ou le rendez-vous ?", "2019-01-07 22:47:54"),
            ("C'est marqué dans la description", "2019-01-08 22:02:54"),
        ],
    },
    {
        'nom': 'Cours de natation 18 à 25 ans',
        'lieu': 'Piscine CSU',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'Parking CSU',
        'capaciteMin': 3,
        'capaciteMax': 10,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'piscine',
        'nbInscrits': 0,
        'description': 'Tarif : 10e / heure',
        'dateLimite': '2021-03-11',
        'commentaires': [],
    },
    {
        'nom': 'Inscription UGA ETC gymnastique',
        'lieu': 'CSU',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'CSU',
        'capaciteMin': 10,
        'capaciteMax': 20,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'gymnastique',
        'nbInscrits': 0,
        'description': 'Inscription semestre 4',
        'dateLimite': '2021-03-11',
        'commentaires': [
            ("C'est résérvé aux licences ?", "2019-01-07 22:47:54"),
            ("Non on peut s'inscrire en Master ", "2019-01-08 20:17:31"),
            ("Tant que vous êtes étudiants de l'UGA c'est ouvert pour vous", "2019-01-08 22:02:54"),
        ],
    },
    {
        'nom': 'Escalade sur glace',
        'lieu': 'Chartreuse',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'Polytech Grenoble',
        'capaciteMin': 3,
        'capaciteMax': 10,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'escalade-sur-glace',
        'nbInscrits': 0,
        'description': 'Niveau confirmé minimum',
        'dateLimite': '2021-03-11',
        'commentaires': [
            ("On nous prète du materiel ?", "2019-01-07 22:47:54"),
            ("Non il faut venir avec le siens", "2019-01-08 20:17:31"),
        ],
    },
    {
        'nom': 'Tournoi de foot',
        'lieu': 'Grenoble',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'Condillac université',
        'capaciteMin': 30,
        'capaciteMax': 50,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'football',
        'nbInscrits': 0,
        'description': '4 équipes minimum',
        'dateLimite': '2021-03-11',
        'commentaires': [],
    },
    {
        'nom': 'Marathon Harry Potter',
        'lieu': 'Chavant',
        'date': '2021-03-12',
        'heure': '09:00',
        'duree': '04:30',
        'point_rdv': 'Polytech Grenoble',
        'capaciteMin': 3,
        'capaciteMax': 10,
        'privee': False,
        'id_groupe': None,
        'typeSortie': 'Sport',
        'photo': 'cinema',
        'nbInscrits': 0,
        'description': 'Ça vous dit d\'aller voir le marathon HP avec moi mercredi ?',
        'dateLimite': '2021-03-11',
        'commentaires': [],
    }
]

GROUPES = [
    {
        'id_groupe' : 1,
        'nom': 'Polytech',
        'description': 'Rando entre popos',
        'nbMembres': 0,
        'membres': [],
        'sorties': [],
        'demandes': [],
        'photo': 'randonnée',
    },
    {
        'id_groupe': 7,
        'nom': 'Equipe 7',
        'description': 'L\'équipe de naruto',
        'nbMembres': 0,
        'membres': [],
        'sorties': [],
        'demandes': [],
        'photo': 'naruto',
    }
]


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

for groupe in GROUPES:
    g = Groupe(nom=groupe['nom'], description=groupe['description'], photo=groupe['photo'], nbMembres=groupe['nbMembres'], membres=groupe['membres'], sorties=groupe['sorties'])

    db.session.add(g)

for user in USERS:
    u = User(password_hash=user['password_hash'], prenom=user['prenom'], nom=user['nom'], \
        email=user['email'], photo=user['photo'], dateNaissance=user['dateNaissance'], ville=user['ville'], \
        preferences=user['preferences'], sexe=user['sexe'], bio=user['bio'], sorties_a_venir=user['sorties_a_venir'], \
        sorties_finies=user['sorties_finies'], role=user['role'], \
        feedbacks=user['feedbacks'])
        
    for com in user.get("commentaires"):
        contenu, timestamp = com
        u.commentaires.append(
            Commentaire(
                contenu=contenu,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )

    db.session.add(u)

db.session.commit()