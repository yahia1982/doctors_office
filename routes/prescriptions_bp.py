from flask import Blueprint, jsonify, request
from flask_pydantic import validate

from dto.prescription import Prescription
from service.prescriptions_service import PrescriptionsService

prescriptions_bp = Blueprint("prescriptions_bp", __name__)

prescriptions_service = PrescriptionsService()


@prescriptions_bp.route('/doctor/<doctor_id>', methods=['GET'])
@validate()
def get_all_doctor_prescriptions(doctor_id: int):
    prescriptions = prescriptions_service.get_all_doctor_prescriptions(doctor_id)
    return jsonify({"results": prescriptions})


@prescriptions_bp.route('<prescription_id>/doctor/<doctor_id>', methods=['GET'])
@validate()
def get_doctor_prescription(prescription_id: int, doctor_id: int):
    prescription = prescriptions_service.get_doctor_prescription(prescription_id, doctor_id)
    return jsonify({"results": prescription})


@prescriptions_bp.route('/patient/<patient_id>', methods=['GET'])
@validate()
def get_all_patient_prescriptions(patient_id: int):
    prescriptions = prescriptions_service.get_all_patient_prescriptions(patient_id)
    return jsonify({"results": prescriptions})


@prescriptions_bp.route('<prescription_id>/patient/<patient_id>', methods=['GET'])
@validate()
def get_patient_prescriptions(prescription_id: int, patient_id: int):
    prescription = prescriptions_service.get_patient_prescription(prescription_id, patient_id)
    return jsonify({"results": prescription})


@prescriptions_bp.route('/', methods=['POST'])
@validate(body=Prescription)
def create():
    data = request.body_params
    prescription = prescriptions_service.create_prescription(data)
    return jsonify({"results": prescription}), 201


@prescriptions_bp.route('/<id>', methods=['PUT'])
@validate(body=Prescription)
def update(id: int):
    data = request.body_params
    prescription = prescriptions_service.update_prescription(data, id)
    return jsonify({"results": prescription})


@prescriptions_bp.route('/<id>', methods=['DELETE'])
@validate()
def delete(id: int):
    prescription = prescriptions_service.delete_prescription(id)
    return jsonify({"results": prescription})
