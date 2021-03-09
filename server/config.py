import os
import connexion
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app

# Configure the SQLAlchemy part of the app instance
app.app.config['SQLALCHEMY_ECHO'] = True
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'entities.db')
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# enable CORS
CORS(app.app, resources={r'/*': {'origins': '*'}})

# enable login
login = LoginManager(app.app)
app.app.secret_key = 'secret key'

# Create the SQLAlchemy db instance
db = SQLAlchemy(app.app)

# Initialize Marshmallow
ma = Marshmallow(app.app)

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')