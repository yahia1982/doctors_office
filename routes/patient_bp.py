from flask import Blueprint, jsonify, request
from flask_pydantic import validate

from dto.patient import Patient
from service.patient_service import PatientService

patient_bp = Blueprint('patient_bp', __name__)

patient_service = PatientService()


@patient_bp.route('/', methods=['GET'])
def get_patients():
    patients = patient_service.get_all_patients()
    return jsonify({"results": patients})


@patient_bp.route('/<id>', methods=['GET'])
@validate()
def get_patient(id: int):
    patient = patient_service.get_patient(id)
    return jsonify({"results": patient})


@patient_bp.route('/', methods=['POST'])
@validate(body=Patient)
def create_patient():
    data = request.body_params
    if not data.password:
        return jsonify({"error": "password is required."}), 400

    patient = patient_service.create_patient(data)
    return jsonify({"results": patient}), 201


@patient_bp.route('/<id>', methods=['PUT'])
@validate(body=Patient)
def update_patient(id: int):
    data = request.body_params
    patient = patient_service.update_patient(data, id)
    return jsonify({"results": patient})


@patient_bp.route('/<id>', methods=['DELETE'])
@validate()
def delete_patient(id: int):
    patient = patient_service.delete_patient(id)
    return jsonify({"results": patient})
