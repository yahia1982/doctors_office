from flask import Blueprint, request
from flask_pydantic import validate

from dto.appointment import Appointment

appointments_bp = Blueprint('appointments_bp', __name__)

@appointments_bp.route('/', methods=['GET'])
def index():
    return 'Appointments page'

@appointments_bp.route('/', methods=['POST'])
@validate(body=Appointment)
def create():
    data = request.body_params
    print(data)
    return 'Create appointment page'

@appointments_bp.route('/', methods=['PUT'])
@validate()
def update():
    return 'Create appointment page'

