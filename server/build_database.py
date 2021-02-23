import os
from config import db
from models import Activity

# Data to initialize database with
ACTIVITY = [
    {'nameActivity': 'Doug', 'typeActivity': 'Farrell'},
    {'nameActivity': 'Kent', 'typeActivity': 'Brockman'},
    {'nameActivity': 'Bunny','typeActivity': 'Easter'}
]

# Delete database file if it exists currently
if os.path.exists('entities.db'):
    os.remove('entities.db')

# Create the database
db.create_all()

# Iterate over the SORTIE structure and populate the database
for act in ACTIVITY:
    a = Activity(nameActivity=act['nameActivity'], typeActivity=act['typeActivity'])
    db.session.add(a)

db.session.commit()