from models import User
from models import UserSchema


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed-in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    firstName = person.get('firstName')
    lastname = person.get('lastname')

    existing_user = User.query \
        .filter(User.firstName == firstName) \
        .filter(User.lastName == lastName) \
        .one_or_none()

    # Can we insert this person?
    if existing_user is None:

        # Create a person instance using the schema and the passed-in person
        schema = UserSchema()
        new_user = schema.load(user, session=db.session).data

        # Add the person to the database
        db.session.add(new_user)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return schema.dump(new_user).data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f'User {fname} {lname} exists already')