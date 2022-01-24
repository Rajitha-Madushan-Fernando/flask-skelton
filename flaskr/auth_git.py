# https://flask.palletsprojects.com/en/2.0.x/tutorial/views/ 
import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from requests_oauthlib import OAuth2Session
from flaskr.db import get_db
import json

bp = Blueprint('auth', __name__, url_prefix='/auth')

client_id = "db1098dc78a9605d294a"
client_secret = "d25295a0a103d8c7a640ec3a67c25f3942eaca5c"
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

# Login 
# https://flask.palletsprojects.com/en/2.0.x/tutorial/views/#id4
@bp.route('/login')
def login():
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)

@bp.route("/callback")
def callback():
    github = OAuth2Session(client_id, state=session['oauth_state'])
    #print(session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)
    print(token)
    result = github.get('https://api.github.com/user').json()
    print(result)
    if result is  not None:
        user = result
        return redirect(url_for('index'))
    else:
        error = "Something wrong!"
    
@bp.before_app_request
def load_logged_in_user():
    user = session.get('id')
    if user is None:
        user = None
    else:
        user = user


# https://flask.palletsprojects.com/en/2.0.x/tutorial/views/#id6
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# Require authentication in other views
# https://flask.palletsprojects.com/en/2.0.x/tutorial/views/#id7
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


