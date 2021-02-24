import os
from config import db
from models import Sortie

# Data to initialize database with
SORTIE = [
    {'nomSortie': 'Doug', 'typeSortie': 'Farrell'},
    {'nomSortie': 'Kent', 'typeSortie': 'Brockman'},
    {'nomSortie': 'Bunny','typeSortie': 'Easter'}
]

# Delete database file if it exists currently
if os.path.exists('entities.db'):
    os.remove('entities.db')

# Create the database
db.create_all()

# Iterate over the SORTIE structure and populate the database
for sort in SORTIE:
    s = Sortie(nomSortie=sort['nomSortie'], typeSortie=sort['typeSortie'])
    db.session.add(s)

db.session.commit()