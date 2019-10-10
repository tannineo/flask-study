"""user controller"""
from flask import Blueprint, jsonify, request

from app.service import user

bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('/register', methods=['POST'])
def register_user():
    req_body = request.json
    """validate req data"""
    error = None

    if not req_body['username']:
        error = 'Username is required.'
    elif not req_body['password']:
        error = 'Password is required.'
    elif not req_body['email']:
        error = 'Email is required.'

    if error is None:
        """service logic"""
        error = user.create_user(username=req_body['username'],
                                 password=req_body['password'],
                                 email=req_body['email'])

    return jsonify({'error': error})
