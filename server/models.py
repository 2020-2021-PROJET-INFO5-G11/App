from sqlalchemy import true
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

from config import db, ma, login


class Commentaire(db.Model):
    __tablename__ = 'commentaire'
    id_commentaire = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_sortie = db.Column(db.Integer, db.ForeignKey('sorties.id_sortie'))
    contenu = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    prenom = db.Column(db.String(32))
    nom = db.Column(db.String(32))
    email = db.Column(db.String(32))
    photo = db.Column(db.String(32))
    dateNaissance = db.Column(db.String(32))
    ville = db.Column(db.String(32))
    preferences = db.Column(db.String(32))
    sexe = db.Column(db.String(32))
    bio = db.Column(db.String(1024))
    activites_a_venir = db.Column(db.String(32))
    activites_finies = db.Column(db.String(32))
    activites_organisees = db.Column(db.String(32))
    role = db.Column(db.String(32))
    feedbacks = db.Column(db.String(32))

    def __repr__(self):
        return '<User {}>'.format(self.pseudo)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    commentaire = db.relationship(
        'Commentaire',
        backref='auteur',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Commentaire.timestamp)'
    )

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True


class Sortie(db.Model):
    __tablename__ = 'sorties'
    id_sortie = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128), index=True)
    lieu = db.Column(db.String(64))
    date = db.Column(db.String(32))
    heure = db.Column(db.String(32))
    duree = db.Column(db.String(32))
    point_rdv = db.Column(db.String(128))
    capaciteMin = db.Column(db.Integer)
    capaciteMax = db.Column(db.Integer)
    privee = db.Column(db.Boolean)
    id_groupe = db.Column(db.Integer)
    typeSortie = db.Column(db.String(32))
    photo = db.Column(db.String(32))
    nbInscrits = db.Column(db.Integer)
    description = db.Column(db.String(1024))
    dateLimite = db.Column(db.String(32))
    commentaires = db.Column(db.String(128))

    commentaire = db.relationship(
        'Commentaire',
        backref='sortie',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Commentaire.timestamp)'
    )

    def __repr__(self):
        return '<Sortie {}>'.format(self.nom)


class SortieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sortie
        sqla_session = db.session
        load_instance = True



@login.user_loader
def load_user(id):
    return User.query.get(int(id))