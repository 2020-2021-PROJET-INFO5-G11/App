from flask import make_response, abort
from flask_login import current_user, login_user, logout_user, login_required

from config import db
from models import User
from models import UserSchema


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

@login_required
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



def get_previous_activities(user):
    return User.query.get('activites_finies')