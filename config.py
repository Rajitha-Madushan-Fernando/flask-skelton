# https://flask.palletsprojects.com/en/2.0.x/config/#builtin-configuration-values

import secrets
import os
from datetime import timedelta

from flask import Flask

from flask_oidc import OpenIDConnect
from okta import UsersClient

    

app = Flask(__name__)

class Config:
    SERVER_NAME = None
    APPLICATION_ROOT = '/'
    
    PREFERRED_URL_SCHEME = 'http'
    MAX_CONTENT_LENGHT = None

    # Session management
    SECRET_KEY = secrets.token_hex()
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SAMESITE = None
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    SESSION_REFRESH_EACH_REQUEST = True
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.path.join(app.instance_path, 'flaskr.sqlite')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.path.join(app.instance_path, 'flaskr.sqlite')



