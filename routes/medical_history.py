from flask import Blueprint, request, jsonify
from flask_pydantic import validate

from dto.history import MedicalHistory
from service.history_service import HistoryService

medical_history_bp = Blueprint("medical_history_bp", __name__)

history_service = HistoryService()


@medical_history_bp.route('/', methods=['GET'])
def get_all_medical_history():
    patient_id = request.args.get('patient_id', -1)
    medical_history = history_service.get_all_medical_history(patient_id)
    return jsonify({"results": medical_history})


@medical_history_bp.route('/<id>', methods=['GET'])
@validate()
def get_medical_history(id: int):
    medical_history = history_service.get_medical_history(id)
    return jsonify({"results": medical_history})


@medical_history_bp.route('/', methods=['POST'])
@validate(body=MedicalHistory)
def create_medical_history():
    data = request.body_params
    medical_history = history_service.create_medical_history(data)
    return jsonify({"results": medical_history})


@medical_history_bp.route('/<id>', methods=['PUT'])
@validate(body=MedicalHistory)
def update_medical_history(id: int):
    data = request.body_params
    medical_history = history_service.update_medical_history(data, id)
    return jsonify({"results": medical_history})


@medical_history_bp.route('/<id>', methods=['DELETE'])
@validate()
def delete_medical_history(id: int):
    medical_history = history_service.delete_medical_history(id)
    return jsonify({"results": medical_history})
