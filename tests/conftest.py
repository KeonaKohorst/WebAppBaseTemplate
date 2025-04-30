import functools
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pytest 
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.models.db import db, ma
from backend.models import *
from backend import create_app


#change the environment database url to a temp memmory one
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
os.environ['NEXT_PUBLIC_API_URL'] = 'http://localhost:4000'

#os.environ['NEXT_PUBLIC_API_URL'] = 'http://http://4.206.215.51/:4000'

#this function does initialization
@pytest.fixture(scope = 'session')
def app():
    #hopefully setting the environ database url works
    app = create_app()
    app.config['TESTING'] = True
    print(F"{app.config['SQLALCHEMY_DATABASE_URI']}")
    with app.app_context():
        db.create_all()

        #send the db session
        yield app

        #drop the db after 
        db.drop_all()

#this function return a testing app
@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

# this returns a db.session
@pytest.fixture(scope='function')
def db_session(app):
    with app.app_context():
        session = db.session
        session.begin()
        yield db.session
        session.rollback()