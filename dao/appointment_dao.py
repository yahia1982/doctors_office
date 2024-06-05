from typing import Any

from dao.patient_dao import PatientDao
from dao.staff_dao import StaffDao
from db.db import DBService
from db.queries import appointment_queries

patient_dao = PatientDao()
staff_dao = StaffDao()


class AppointmentDao:

    def appointment_row_mapper(self, appointment) -> Any:
        return {
            "appointment_id": appointment[0],
            "doctor": staff_dao.get_doctor(appointment[1]),
            "patient": patient_dao.get_patient(appointment[2]),
            "appointment_date": appointment[3],
            "appointment_time": appointment[4],
            "Reason": appointment[5]
        }

    def doctor_appointment_row_mapper(self, appointment) -> Any:
        return {
            "appointment_id": appointment[0],
            "patient": patient_dao.get_patient(appointment[1]),
            "appointment_date": appointment[2],
            "appointment_time": appointment[3],
            "Reason": appointment[4]
        }

    def patient_appointment_row_mapper(self, appointment) -> Any:
        return {
            "appointment_id": appointment[0],
            "doctor": staff_dao.get_active_doctor(appointment[1]),
            "appointment_date": appointment[2],
            "appointment_time": appointment[3],
            "Reason": appointment[4]
        }

    def get_all_doctor_appointments(self, doctor_id: int) -> Any:
        sql = appointment_queries.select_all_by_doctor
        appointments = DBService.query(sql, {"StaffID": doctor_id})
        return [self.doctor_appointment_row_mapper(appointment) for appointment in appointments]

    def get_all_patient_appointments(self, patient_id: int) -> Any:
        sql = appointment_queries.select_all_by_patient
        appointments = DBService.query(sql, {"PatientID": patient_id})
        return [self.patient_appointment_row_mapper(appointment) for appointment in appointments]

    def get_doctor_appointment(self, doctor_id: int, appointment_id: int) -> Any:
        sql = appointment_queries.select_one_by_doctor
        appointment = DBService.query_single(sql, {"StaffID": doctor_id, "AppointmentID": appointment_id})
        if appointment:
            return self.doctor_appointment_row_mapper(appointment)

    def get_appointment(self, appointment_id: int) -> Any:
        sql = appointment_queries.select_one
        appointment = DBService.query_single(sql, {"AppointmentID": appointment_id})
        if appointment:
            return self.appointment_row_mapper(appointment)

    def get_patient_appointment(self, patient_id: int, appointment_id: int) -> Any:
        sql = appointment_queries.select_one_by_patient
        appointment = DBService.query_single(sql, {"PatientID": patient_id, "AppointmentID": appointment_id})
        if appointment:
            return self.patient_appointment_row_mapper(appointment)

    def create_appointment(self, data: Any) -> Any:
        sql = appointment_queries.create
        appointment_id = DBService.query_single(sql, {
            "PatientID": data.patient_id,
            "StaffID": data.doctor_id,
            "AppointmentDate": data.appointment_date,
            "AppointmentTime": str(data.appointment_time),
            "Reason": data.reason
        })
        if appointment_id:
            return self.get_doctor_appointment(data.doctor_id, appointment_id[0])

    def update_appointment(self, data: Any, id: int) -> Any:
        sql = appointment_queries.update
        DBService.update(sql, {
            "PatientID": data.patient_id,
            "StaffID": data.doctor_id,
            "AppointmentDate": data.appointment_date,
            "AppointmentTime": str(data.appointment_time),
            "Reason": data.reason,
            "AppointmentID": id
        })
        return self.get_doctor_appointment(data.doctor_id, id)

    def delete_appointment(self, id: int) -> Any:
        sql = appointment_queries.delete
        appointment = self.get_appointment(id)
        DBService.update(sql, {
            "AppointmentID": id,
            "IsCancelled": True
        })
        return appointment
