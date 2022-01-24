# https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/
import os
import secrets

from flask import Flask
from . import auth, db, blog


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.DevConfig')


    #### Database configuration:
    # ensure the instance folder exists (for the Sqlite database file)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Registering the database with the application
    # https://flask.palletsprojects.com/en/2.0.x/tutorial/database/#id5
    db.init_app(app)
    ####

    # The application's blueprints
    # https://flask.palletsprojects.com/en/2.0.x/tutorial/views/#id2
    app.register_blueprint(auth.bp)

    # https://flask.palletsprojects.com/en/2.0.x/tutorial/blog/#id2
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
 

    return app

