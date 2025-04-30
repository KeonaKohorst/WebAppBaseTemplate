from flask import Flask, request, jsonify, make_response, Blueprint
import bcrypt
from datetime import datetime, timezone
import pytz
import sys
import re


from ..models import Default

#from backend import db, ma, app

bp = Blueprint('test', __name__)

#=====  ROUTES FOR TEST ============

@bp.route('/api/flask/test', methods=['GET'])
def sign_of_life():
  print("reached the api", flush=True)
  try:
    return jsonify({'message': 'Hello World'}), 200
  except Exception as e:
    return make_response(jsonify({'message': 'Error', 'error': str(e)}), 500)
  
