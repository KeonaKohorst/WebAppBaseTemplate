
import os
from urllib import response
import zipfile
import json
from backend.models import *
import bcrypt


from werkzeug.datastructures import FileStorage


#CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def test_sign_of_life(client, db_session):
    """
    GIVEN GET /api/flask/test
    """

    response = client.get(
        f'/api/flask/test'
    )

    assert response.status_code == 200
    assert "message" in response.json
