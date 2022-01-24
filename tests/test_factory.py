# https://flask.palletsprojects.com/en/2.0.x/tutorial/tests/#id3

from flaskr import create_app


def test_config():
    assert create_app().testing

