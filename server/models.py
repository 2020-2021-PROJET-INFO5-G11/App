from datetime import datetime
from sqlalchemy import true
from config import db, ma

class User(db.Model):
    __tablename__ = 'users'
    #id_user = db.Column(db.Integer, primary_key=True)
    #userName = db.Column(db.String(32), index=True)
    firstName = db.Column(db.String(32), primary_key=True)
    lastName = db.Column(db.String(32))
    """email = db.Column(db.String(32))
    photo = db.Column(db.String(32))
    dateNaissance = db.Column(db.String(32))
    ville = db.Column(db.String(32))
    preferences = db.Column(db.String(32))
    sexe = db.Column(db.String(32))
    bio = db.Column(db.String(32))
    activites_a_venir = db.Column(db.String(32))
    activites_finies = db.Column(db.String(32))
    activites_organisees = db.Column(db.String(32))
    role = db.Column(db.String(32))
    feedbacks = db.Column(db.String(32))"""

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

class Sortie(db.Model):
    __tablename__ = 'sorties'
    id_sortie = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(32), index=True)
    location = db.Column(db.String(32))
    date = db.Column(db.String(32))
    heure = db.Column(db.String(32))
    duree = db.Column(db.String(32))
    point_rdv = db.Column(db.String(32))
    capaciteMin = db.Column(db.Integer)
    capacaiteMax = db.Column(db.Integer)
    privee = db.Column(db.Boolean)
    id_groupe = db.Column(db.Integer)
    typeSortie = db.Column(db.String(32))
    photo = db.Column(db.String(32))
    nbInscrits = db.Column(db.Integer)
    description = db.Column(db.String(1024))
    dateLimite = db.Column(db.String(32))
    commentaires = db.Column(db.String(32))





    # timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SortieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sortie
        sqla_session = db.session
        load_instance = True