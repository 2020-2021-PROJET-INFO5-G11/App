from flask import make_response, abort
from flask_login import current_user, login_user, logout_user, login_required

from config import db
from models import User, UserSchema, Sortie


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

# @login_required
def get_all_users():
    users = User.query.all()

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
            "User {id} deleted".format(id=id), 200
        )
    else:
        abort(404, f'User not found for id: {id}')

def read_one_user_by_id(id):
    user = User.query.get(id)

    if user is not None:
        user_schema = UserSchema()
        return user_schema.dump(user)
    else:
        abort(404, f'User not found for id: {id}')

@login_required
def join_sortie(id_sortie):
    sort = Sortie.query.filter(Sortie.id_sortie == id_sortie).one_or_none()
    if sort is not None:
        
        #if(Sortie.query.filter(User.id == current_user.id).one_or_none() is None)
        current_user.sorties_a_venir.append(sort)
        sort.nbInscrits = sort.nbInscrits+1
        return 200
        #else:
        #    abort(404, f'User {current_user.pseudo} already joined this sortie')
    else:
        abort(404, f'Sortie not found for id: {id_sortie}')

def get_previous_activities(user):
    return User.query.all_sorties