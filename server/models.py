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

groupeSortie = db.Table('groupeSortie',
    db.Column('id_groupe', db.Integer, db.ForeignKey('groupes.id_groupe'), primary_key=True),
    db.Column('id_sortie', db.Integer, db.ForeignKey('sorties.id_sortie'), primary_key=True)
)

groupeUser = db.Table('groupeUser',
    db.Column('id_groupe', db.Integer, db.ForeignKey('groupes.id_groupe'), primary_key=True),
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

demandeUser = db.Table('demandeUser',
    db.Column('id_demande', db.Integer, db.ForeignKey('demandes.id_demande'), primary_key=True),
    db.Column('id_user', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

demandeGroupe = db.Table('demandeGroupe',
    db.Column('id_demande', db.Integer, db.ForeignKey('demandes.id_demande'), primary_key=True),
    db.Column('id_groupe', db.Integer, db.ForeignKey('groupes.id_groupe'), primary_key=True)
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))
    prenom = db.Column(db.String(32), index=True)
    nom = db.Column(db.String(32), index=True)
    email = db.Column(db.String(64))
    photo = db.Column(db.String(32))        # A remplacer par un autre type
    dateNaissance = db.Column(db.String(32))
    ville = db.Column(db.String(32))
    preferences = db.Column(db.String(32))
    sexe = db.Column(db.String(32))
    bio = db.Column(db.String(1024))
    role = db.Column(db.String(32))
    feedbacks = db.Column(db.String(32))

    commentaires = db.relationship('Commentaire', backref='auteur', 
        order_by='desc(Commentaire.timestamp)')
    demandes = db.relationship('Demande', secondary=demandeUser, lazy='subquery')
    sorties_a_venir = db.relationship('Sortie', secondary=userSortie_a_venir, lazy='subquery',
        backref=db.backref('participants', lazy=False))
    sorties_finies = db.relationship('Sortie', secondary=userSortie_finies, lazy='subquery')


    def __repr__(self):
        return '<User {}>'.format(self.prenom)

    def set_password(self, password):           # Encode le mot de passe
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):         # Compare le mdp encodé à un string
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
    archivee = db.Column(db.Boolean)
    commentaires = db.relationship('Commentaire', backref='sortie', cascade='all, delete, delete-orphan',
        single_parent=True, order_by='asc(Commentaire.timestamp)'
    )

    def __repr__(self):
        return '{}'.format(self.prenom)


class Commentaire(db.Model):
    __tablename__ = 'commentaire'
    id_commentaire = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_sortie = db.Column(db.Integer, db.ForeignKey('sorties.id_sortie'))
    contenu = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Groupe(db.Model):
    __tablename__ = 'groupes'
    id_groupe = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(32))
    id_owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String, nullable=False)
    nbMembres = db.Column(db.Integer)
    photo = db.Column(db.String(32))
    demandes = db.relationship('Demande', secondary=demandeGroupe, lazy='subquery',
        backref=db.backref('groupe', lazy=False))
    sorties = db.relationship('Sortie', secondary=groupeSortie, lazy='subquery',
        backref=db.backref('groupe', lazy=False))
    membres = db.relationship('User', secondary=groupeUser, lazy='subquery',
        backref=db.backref('groupes', lazy=False))


class Demande(db.Model):                # Invitations aux groupes
    __tablename__ = 'demandes'
    id_demande = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_groupe = db.Column(db.Integer, db.ForeignKey('groupes.id_groupe'))
    id_owner = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


#--------------------------------------------------------------------------------
# Schemas servant a afficher les entités au format Json

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
    commentaires = fields.Nested('ComSchema', default=[], many=True, exclude=("auteur","sortie",), dump_only=True)
    sorties_a_venir = fields.Nested('SortieSchema', default=[], many=True, exclude=("participants","commentaires",), dump_only=True)
    sorties_finies = fields.Nested('SortieSchema', default=[], many=True, exclude=("participants","commentaires",), dump_only=True)
    groupes = fields.Nested('GroupeSchema', default=[], many=True, exclude=("membres","demandes",), dump_only=True)
    demandes = fields.Nested('DemandeSchema', default=[], many=True, dump_only=True)

class ComSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commentaire
        sqla_session = db.session
        include_fk = True
        load_instance = True
    auteur = fields.Nested('UserSchema', default=None, many=False, exclude=("commentaires","sorties_a_venir","sorties_finies","groupes","demandes",), dump_only=True)
    sortie = fields.Nested('SortieSchema', default=None, exclude=("commentaires","participants",), dump_only=True)

class GroupeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Groupe
        sqla_session = db.session
        include_fk = True
        load_instance = True
    owner = fields.Nested('UserSchema', default=None, many=False, exclude=("commentaires","sorties_a_venir","sorties_finies","groupes","demandes",), dump_only=True)
    membres = fields.Nested('UserSchema', default=[], many=True, exclude=("commentaires","sorties_a_venir","sorties_finies","groupes","demandes",), dump_only=True)
    demandes = fields.Nested('DemandeSchema', default=[], many=True, dump_only=True)

class SortieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sortie
        sqla_session = db.session
        load_instance = True
    commentaires = fields.Nested('ComSchema', default=[], many=True, exclude=("sortie","auteur",), dump_only=True)
    participants = fields.Nested('UserSchema', default=[], many=True, exclude=("commentaires","sorties_a_venir","sorties_finies","groupes","demandes",), dump_only=True)
    groupe = fields.Nested('GroupeSchema', default=None, exclude=("membres",), dump_only=True)


class DemandeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Demande
        sqla_session = db.session
        include_fk = True
        load_instance = True

@login.user_loader
def load_user(id):
    return User.query.get(int(id))