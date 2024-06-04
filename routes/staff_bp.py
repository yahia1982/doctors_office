from flask import Blueprint, request, jsonify
from flask_pydantic import validate
from dto.staff import Staff
from service.staff_service import StaffService

staff_bp = Blueprint('doctors_bp', __name__)

staff_service = StaffService()


@staff_bp.route('/', methods=['GET'])
def get_doctors():
    doctors = staff_service.get_active_doctors()
    return jsonify({"results": doctors})


@staff_bp.route('/<id>', methods=['GET'])
@validate()
def get_doctor(id: int):
    doctor = staff_service.get_active_doctor(id)
    return jsonify({"results": doctor})


@staff_bp.route('/', methods=['POST'])
@validate(body=Staff)
def create_doctor():
    data = request.body_params
    if not data.password:
        return jsonify({"error": "password is required."}), 400
    doctor = staff_service.create_doctor(data)
    return jsonify({"results": doctor})


@staff_bp.route('/<id>', methods=['PUT'])
@validate(body=Staff)
def update_doctor(id: int):
    data = request.body_params
    doctor = staff_service.update_doctor(data, id)
    return jsonify({"results": doctor})


@staff_bp.route('/<id>', methods=['DELETE'])
@validate()
def delete_doctor(id: int):
    doctor = staff_service.delete_doctor(id)
    return jsonify({"results": doctor})
