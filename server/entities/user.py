from flask import make_response, abort
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Message

from config import db, mail
from models import User, UserSchema, Sortie, SortieSchema, Commentaire, ComSchema, Groupe, GroupeSchema, Demande, DemandeSchema, InfoSortie, InfoSortieSchema


def get_all_users():
    """
    requête associée:
        /user
    """
    
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return user_schema.dump(users)


def create(user):
    """
    requête associée:
        /user
    paramètres :
        user : données de l'utilisateur à créer (format JSON)
    """

    id = user.get('id')
    if User.query.get(id) is not None:
        abort(409, f'id {id} is already used')

    nom = user.get('nom')
    prenom = user.get('prenom')
    pwd = user.get('password_hash')

    existing_user = User.query \
        .filter(User.nom == nom) \
        .filter(User.prenom == prenom) \
        .one_or_none()

    if existing_user is not None:
        abort(409, f'User {prenom} {nom} exists already')
    
    schema = UserSchema()

    new_user = schema.load(user, session=db.session)
    new_user.set_password(pwd)

    db.session.add(new_user)
    db.session.commit()

    return schema.dump(new_user), 201


def update(id, user):
    """
    requête associée:
        /user/{id}
    paramètres :
        id : id de l'utilisateur à modifier
        user : nouvelles valeurs de l'utilisateur une fois modifié (format JSON)
    """

    update_user = User.query.filter(
        User.id == id
    ).one_or_none()

    if update_user is None:
        abort(404, f'User not found for id: {id}')
    else:
        schema = UserSchema()
        update = schema.load(user, session=db.session)

        update.id = update_user.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_user)
        return data, 201


def delete(id):
    """
    requête associée:
        /user/{id}
    paramètres :
        id : id de l'utilisateur à supprimer
    """

    user = User.query.filter(User.id == id).one_or_none()

    if user is not None:
        if user == current_user:
            logout()
        db.session.delete(user)
        db.session.commit()
        return make_response(
            "User {id} deleted".format(id=id), 204)
    else:
        abort(404, f'User not found for id: {id}')


def read_one_user_by_id(id):                    # Récupère le User dont l'id est donné
    """
    requête associée:
        /user/{id}
    paramètres :
        id : id de l'utilisateur
    """

    user = User.query.get(id)

    if user is None:
        abort(404, f'User not found for id: {id}')
    user_schema = UserSchema()
    return user_schema.dump(user)



def send_mail(id, content):
    """
    requête associée:
        /user/{id}/send_mail
    paramètres :
        id : id de l'utilisateur à qui envoyer le mail
        content : contenu du mail
    """

    user = User.query.get(id)
    if user is None:
        abort(404, f'User not found for id: {id}')

    msg = Message("Hello",
                  recipients=[user.email])
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send_mail(msg)
    return 200


### Fonctions s'appliquant au current_user


def login(email, password):
    """
    requête associée:
        /user/login
    paramètres :
        email : email de l'utilisateur voulant se connecter
        password : mot de passe crypté de l'utilisateur voulant se connecter
    """

    if current_user.is_authenticated:
         abort(400, 'Utilisateur deja connecte')
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        abort(400, 'Pseudo ou mot de passe incorrect')
    login_user(user)#, remember=form.remember_me.data)
    return 200


def logout():
    """
    requête associée:
        /user/logout
    """
    
    logout_user()
    return


@login_required
def change_password(new_pwd):
    """
    requête associée:
        
    paramètres :
        new_pwd : nouveau mot de passe
    """

    user = current_user
    user.set_password(new_pwd)
    db.session.add(user)
    db.session.commit()
    schema = UserSchema()

    return schema.dump(user), 200


def get_current():
    """
    requête associée:
        /user/current
    """
    
    user_schema = UserSchema()
    return user_schema.dump(User.query.get(1)) ## TEST : HERE I USE FIRST USER INSTEAD OF CURRENT USER


@login_required
def update_current(user):                       # Modifie les infos de l'utilisateur courant
    """
    requête associée:
        
    paramètres :
        user : nouvelles valeurs de l'utilisateur courant une fois modifié
    """

    update_user = current_user
    
    schema = UserSchema()
    update = schema.load(user, session=db.session)

    update.id = update_user.id

    db.session.merge(update)
    db.session.commit()

    data = schema.dump(update_user)
    return data, 201


@login_required
def get_incoming_activities():
    """
    requête associée:
        /user/current/a_venir
    """

    sorties = current_user.sorties_a_venir
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)


@login_required
def get_previous_activities():
    """
    requête associée:
        /user/current/finies
    """
    
    sorties = current_user.sorties_finies
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)


#@login_required
def switch_to_previous(id_sortie):              # Une sortie à venir devient une sortie finie
    """
    requête associée:
        /user/current/{id_sortie}/switch
    parametres :
        id_sortie : id de la sortie à changer de catégorie
    """

    info = InfoSortie.query \
        .filter(InfoSortie.id_sortie == id_sortie) \
        .filter(InfoSortie.id_user == current_user.id) \
        .first()

    if info is None:
        abort(404, f'{current_user} is not registered to Sortie {id_sortie}')
    
    current_user.sorties_finies.append(info)
    current_user.sorties_a_venir.remove(info)

    db.session.add(current_user)
    db.session.commit()

    return 200


@login_required
def register(id_sortie, organisateur, nb_inscrits):                        # Inscription à une sortie
    """
    requête associée:
        /sortie/{id_sortie}/register
    parametres :
        id_sortie : id de la sortie à laquelle s'inscrire
        orgnisateur : l'utilisateur est organisateur ou non (booléen)
        nb_inscrits : nombre de places réservées par l'utilisaeur
    """

    sortie_a_venir = Sortie.query.filter(
        Sortie.id_sortie == id_sortie).one_or_none()

    if sortie_a_venir is None:
        abort(404, f'Sortie not found for Id: {id_sortie}')
    
    existing_info = InfoSortie.query \
        .filter(InfoSortie.id_sortie == id_sortie) \
        .filter(InfoSortie.id_user == current_user.id) \
        .one_or_none()

    if existing_info is not None:
        abort(401, f'{current_user} is already registered to Sortie {id_sortie}')

    info = InfoSortie(
        id_sortie = id_sortie,
        organisateur = organisateur,
        nb_inscrits = nb_inscrits,
    )

    """i = {
        'id_user': current_user.id,
        'id_sortie': id_sortie,
        'organisateur': organisateur,
        'nb_inscrits': nb_inscrits
    }

    schema = InfoSortieSchema()
    info = schema.load(i, session=db.session)
"""
    
    current_user.sorties_a_venir.append(info)    
    info.sortie.nbInscrits += nb_inscrits
    db.session.commit()

    return 201


@login_required
def cancel_registration(id_sortie):             # Désinscription d'une sortie
    """
    requête associée:
        /sortie/{id_sortie}/register
    parametres :
        id_sortie : id de la sortie à laquelle se désinscrire
    """
    
    info = InfoSortie.query \
        .filter(InfoSortie.id_sortie == id_sortie) \
        .filter(InfoSortie.id_user == current_user.id) \
        .first()

    if info is None:
        abort(404, f'{current_user} is not registered to Sortie {id_sortie}')
    
    info.sorties.nbInscrits -= info.nb_inscrits
    db.session.delete(info)
    db.session.add(current_user)
    db.session.commit()

    return 201


@login_required
def quit_groupe(id_groupe):             # Quitter un groupe
    """
    requête associée:
        /groupe/{id_groupe}/membres
    parametres :
        id_groupe : id du groupe que l'utilisateur veut quitter
    """

    groupe = Groupe.query.filter(
        Groupe.id_groupe == id_groupe).one_or_none()

    if groupe is None:
        abort(404, f'Groupe not found for Id: {id_groupe}')
    
    groupe.nbMembres -= 1
    current_user.groupes.remove(groupe)
    db.session.add(current_user)
    db.session.commit()

    return 201


def remove_from_groupe(id_groupe, id):             # Suppresion d'un membre d'un groupe
    """
    requête associée:
        /groupe/{id_groupe}/membre/{id}
    parametres :
        id_groupe : id du groupe où l'on veut supprimer un utilisateur
        id : id de l'utilisateur à supprimer
    """

    groupe = Groupe.query.filter(
        Groupe.id_groupe == id_groupe).one_or_none()

    if groupe is None:
        abort(404, f'Groupe not found for Id: {id_groupe}')

    old_member = User.query.filter(
        User.id == id).one_or_none()
    
    groupe.nbMembres -= 1
    old_member.groupes.remove(groupe)
    db.session.add(old_member)
    db.session.commit()

    return 201
