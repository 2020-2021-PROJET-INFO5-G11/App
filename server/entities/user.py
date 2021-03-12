from flask import make_response, abort, current_app, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime, timedelta
import jwt
from functools import wraps
from config import db
from models import User, UserSchema, Sortie, SortieSchema, Commentaire, ComSchema


def login(email, password):
    if current_user.is_authenticated:
         abort(400, 'Utilisateur deja connecte')
    user = User.query.filter_by(email=email).first()
    if user is None :# or not user.check_password(password):
        abort(400, 'Email ou mot de passe incorrect')
    login_user(user)#, remember=form.remember_me.data)
    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token }), 200

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

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

        return jsonify(user.to_dict()), 201

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


@login_required
@token_required
def get_previous_activities():

    sorties = current_user.sorties_finies
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)


@login_required
@token_required
def get_incoming_activities():
    
    sorties = current_user.sorties_a_venir
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)


@login_required
@token_required
def switch_to_previous(id_sortie):
    sortie_a_venir = Sortie.query.filter(
        Sortie.id_sortie == id_sortie).one_or_none()

    if sortie_a_venir is None:
        abort(404, f'Sortie not found for Id: {id}')
    
    current_user.sorties_a_venir.remove(sortie_a_venir)
    current_user.sorties_finies.append(sortie_a_venir)

    db.session.add(current_user)
    db.session.commit()

    return 200


@login_required
@token_required
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
@token_required
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