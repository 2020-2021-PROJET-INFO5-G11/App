from datetime import datetime
from config import db, ma

class User(db.Model):
    __tablename__ = 'users'
    #id_user = db.Column(db.Integer, primary_key=True)
    #userName = db.Column(db.String(32), index=True)
    firstName = db.Column(db.String(32), primary_key=True)
    lastName = db.Column(db.String(32))
    """email = db.Column(db.String(32))
    photo = db.Column(db.String(32))
    birthDate = db.Column(db.String(32))
    city = db.Column(db.String(32))
    preferences = db.Column(db.String(32))
    gender = db.Column(db.String(32))
    bio = db.Column(db.String(32))
    activitiesIncoming = db.Column(db.String(32))
    activitiesDone = db.Column(db.String(32))
    activitiesOrganized = db.Column(db.String(32))
    role = db.Column(db.String(32))
    feedbacks = db.Column(db.String(32))"""

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class Sortie(db.Model):
    __tablename__ = 'sorties'
    id_sortie = db.Column(db.Integer, primary_key=True)
    nomSortie = db.Column(db.String(32), index=True)
    typeSortie = db.Column(db.String(32))
    # timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SortieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sortie
        load_instance = True