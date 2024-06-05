from flask import Blueprint, request, jsonify
from flask_login import login_required, logout_user
from flask_pydantic import validate

from dto.login import UserLogin
from service.users_service import UserService

users_bp = Blueprint('user_bp', __name__)

user_service = UserService()


@users_bp.route('/login', methods=['POST'])
@validate(body=UserLogin)
def login():
    data = request.body_params
    response, status = user_service.login(data)
    return jsonify(response), status


@users_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'You have been logged out.'}), 200
