from sqlalchemy import true
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from marshmallow_sqlalchemy import fields

from config import db, ma, login


userSortie_a_venir = db.Table('userSortie_a_venir',
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('id_sortie', db.Integer, db.ForeignKey('sorties.id_sortie'), primary_key=True)
)

userSortie_finies = db.Table('userSortie_finies',
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('id_sortie', db.Integer, db.ForeignKey('sorties.id_sortie'), primary_key=True)
)

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
    role = db.Column(db.String(32))
    feedbacks = db.Column(db.String(32))
    commentaires = db.relationship(
        'Commentaire',
        backref='auteur',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Commentaire.timestamp)'
    )
    sorties_a_venir = db.relationship('Sortie', secondary=userSortie_a_venir, lazy='subquery',
        backref=db.backref('participants', lazy=False))


    def __repr__(self):
        return '<User {}>'.format(self.pseudo)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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
    commentaires = db.relationship(
        'Commentaire',
        backref='sortie',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='asc(Commentaire.timestamp)'
    )

    def __repr__(self):
        return '<Sortie {}>'.format(self.nom)


class Commentaire(db.Model):
    __tablename__ = 'commentaire'
    id_commentaire = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_sortie = db.Column(db.Integer, db.ForeignKey('sorties.id_sortie'))
    contenu = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


#--------------------------------------------------------------------------------

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
    commentaires = fields.Nested('UserComSchema', default=[], many=True)
    sorties_a_venir = fields.Nested('UserSortieSchema', default=[], many=True)

class UserComSchema(ma.SQLAlchemyAutoSchema):
    #This class exists to get around a recursion issue
    class Meta:
        model = Commentaire

class UserSortieSchema(ma.SQLAlchemyAutoSchema):
    #This class exists to get around a recursion issue
    class Meta:
        model = Sortie


class ComSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commentaire
        sqla_session = db.session
    user = fields.Nested('ComUserSchema', default=None)
    sortie = fields.Nested('ComSortieSchema', default=None)

class ComUserSchema(ma.SQLAlchemyAutoSchema):
    #This class exists to get around a recursion issue
    class Meta:
        odel = User

class ComSortieSchema(ma.SQLAlchemyAutoSchema):
    #This class exists to get around a recursion issue
    class Meta:
        model = Sortie


class SortieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sortie
        sqla_session = db.session
        load_instance = True
    commentaires = fields.Nested('SortieComSchema', default=[], many=True)
    participants = fields.Nested('SortieUserSchema', default=[], many=True)

class SortieUserSchema(ma.SQLAlchemyAutoSchema):
    #This class exists to get around a recursion issue
    class Meta:
        model = User
    commentaires = fields.Nested('SortieComSchema', default=[], many=True)

class SortieComSchema(ma.SQLAlchemyAutoSchema):
    #This class exists to get around a recursion issue
    class Meta:
        model = Commentaire
    """id_commentaire = fields.fields.Int()
    id_user = fields.fields.Int()
    id_sortie = fields.fields.Int()
    contenu = fields.fields.Str()
    timestamp = fields.fields.Str()"""


@login.user_loader
def load_user(id):
    return User.query.get(int(id))