from flask import make_response, abort
from flask_login import current_user, login_user, logout_user, login_required

from config import db
from models import User, UserSchema, Sortie, SortieSchema, Commentaire, ComSchema


def login(username, password):
    if current_user.is_authenticated:
         abort(400, 'Utilisateur deja connecte')
    user = User.query.filter_by(pseudo=username).first()
    if user is None :# or not user.check_password(password):
        abort(400, 'Pseudo ou mot de passe incorrect')
    login_user(user)#, remember=form.remember_me.data)
    return 200

def logout():
    logout_user()
    return

def get_current():
    user_schema = UserSchema()
    return user_schema.dump(current_user)


def get_all_users():
    users = (
        User.query
        .outerjoin(Commentaire)#.outerjoin(Sortie).select_from('sorties_a_venir')
        .all()
    )

    user_schema = UserSchema(many=True)
    return user_schema.dump(users)


def create(user):
    id = user.get('id')
    if User.query.get(id) is not None:
        abort(409, f'id {id} is already used')

    pseudo = user.get('pseudo')

    existing_user = User.query \
        .filter(User.pseudo == pseudo) \
        .one_or_none()

    if existing_user is None:
        schema = UserSchema()

        #user.password_hash = user.set_password(self, user.password_hash)
        new_user = schema.load(user, session=db.session)

        db.session.add(new_user)
        db.session.commit()

        return schema.dump(new_user), 201

    else:
        abort(409, f'User {pseudo} exists already')


def update(id, user):
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
        return data, 200


def delete(id):
    user = User.query.filter(User.id == id).one_or_none()

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(
            "User {id} deleted".format(id=id), 200)
    else:
        abort(404, f'User not found for id: {id}')


def read_one_user_by_id(id):
    user = (
        User.query
        .outerjoin(Sortie).outerjoin(Commentaire)
        .get(id)
    )

    if user is not None:
        user_schema = UserSchema()
        return user_schema.dump(user)
    else:
        abort(404, f'User not found for id: {id}')


def get_previous_activities(id):
    user = User.query.get(id)
    
    if user is not None:
        sorties = user.sorties_finies
        sortie_schema = SortieSchema(many=True)
        return sortie_schema.dump(sorties)
    else:
        abort(404, f'User not found for id: {id}')


def get_incoming_activities(id):
    user = User.query.get(id)
    
    if user is not None:
        sorties = user.sorties_a_venir
        sortie_schema = SortieSchema(many=True)
        return sortie_schema.dump(sorties)
    else:
        abort(404, f'User not found for id: {id}')


def switch_to_previous(id_sortie, id):
    sortie_a_venir = Sortie.query.filter(
        Sortie.id_sortie == id_sortie).one_or_none()

    user = User.query.filter(User.id == id).one_or_none()
    if sortie_a_venir is None:
        abort(404, f'Sortie not found for Id: {id}')
    if user is None:
        abort(404, f'User not found for Id: {id}')
    
    user.sorties_a_venir.remove(sortie_a_venir)
    user.sorties_finies.append(sortie_a_venir)

    db.session.add(user)
    db.session.commit()

    return 200


@login_required
def register(id_sortie):
    sortie_a_venir = Sortie.query.filter(
        Sortie.id_sortie == id_sortie).one_or_none()

    if sortie_a_venir is None:
        abort(404, f'Sortie not found for Id: {id}')
    
    sortie_a_venir.nbInscrits += 1
    current_user.sorties_a_venir.append(sortie_a_venir)
    db.session.add(current_user)
    db.session.commit()

    return 201


@login_required
def cancel_registration(id_sortie):
    sortie_a_venir = Sortie.query.filter(
        Sortie.id_sortie == id_sortie).one_or_none()

    if sortie_a_venir is None:
        abort(404, f'Sortie not found for Id: {id}')
    
    sortie_a_venir.nbInscrits -= 1
    current_user.sorties_a_venir.remove(sortie_a_venir)
    db.session.add(current_user)
    db.session.commit()

    return 201