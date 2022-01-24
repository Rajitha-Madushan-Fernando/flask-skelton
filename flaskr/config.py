import secrets
from flask import Flask
from flask.json import jsonify
from flask_oidc import OpenIDConnect
from okta import UsersClient
import os

app = Flask(__name__)


class Config:
    SECRET_KEY = secrets.token_hex()
    DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    #os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

