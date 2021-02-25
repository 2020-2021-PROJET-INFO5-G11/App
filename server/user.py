from flask import make_response, abort

from config import db
from models import User
from models import UserSchema



def get_all_users():
    users = User.query.all()

    user_schema = UserSchema(many=True)
    return user_schema.dump(users)


def create(user):
    """
    This function creates a new user
    based on the passed-in user data

    :param user:    user to create
    :return:        201 on success, 406 on user exists
    """

    id = user.get('id_user')
    if User.query.get(id) is not None:
        abort(409, f'id {id} is already used')

    prenom = user.get('prenom')
    nom = user.get('nom')

    existing_user = User.query \
        .filter(User.prenom == prenom) \
        .filter(User.nom == nom) \
        .one_or_none()

    if existing_user is None:
        schema = UserSchema()
        new_user = schema.load(user, session=db.session)

        db.session.add(new_user)
        db.session.commit()

        return schema.dump(new_user), 201

    else:
        abort(409, f'User {prenom} {nom} exists already')