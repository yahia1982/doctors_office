from flask import Blueprint, request, jsonify
from flask_pydantic import validate

from dto.appointment import Appointment
from service.appointment_service import AppointmentService

appointments_bp = Blueprint('appointments_bp', __name__)

appointment_service = AppointmentService()


@appointments_bp.route('/doctor/<doctor_id>', methods=['GET'])
# @login_required
# @role_required(roles=[PersonalType.DOCTOR, PersonalType.ADMINISTRATION_STAFF])
@validate()
def get_all_doctor_appointments(doctor_id: int):
    appointments = appointment_service.get_doctor_appointments(doctor_id)
    return jsonify({"results": appointments})


@appointments_bp.route('/patient/<patient_id>', methods=['GET'])
# @login_required
# @role_required(roles=[PersonalType.PATIENT])
@validate()
def get_all_patient_appointments(patient_id: int):
    appointments = appointment_service.get_patient_appointments(patient_id)
    return jsonify({"results": appointments})


@appointments_bp.route('/', methods=['POST'])
# @login_required
# @role_required(roles=[PersonalType.DOCTOR])
@validate(body=Appointment)
def create():
    data = request.body_params
    appointment = appointment_service.create_appointment(data)
    return jsonify({"results": appointment}), 201


@appointments_bp.route('/<id>', methods=['PUT'])
# @login_required
# @role_required(roles=[PersonalType.DOCTOR])
@validate(body=Appointment)
def update(id: int):
    data = request.body_params
    appointment = appointment_service.update_appointment(data, id)
    return jsonify({"results": appointment})


@appointments_bp.route('/<id>', methods=['DELETE'])
# @login_required
# @role_required(roles=[PersonalType.DOCTOR])
@validate()
def delete(id: int):
    appointment = appointment_service.delete_appointment(id)
    return jsonify({"results": appointment})
