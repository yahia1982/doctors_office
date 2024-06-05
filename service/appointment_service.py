from typing import Any

from dao.appointment_dao import AppointmentDao

appointment_dao = AppointmentDao()
class AppointmentService:
    def create_appointment(self, data: Any) -> Any:
        #TODO: Check doctr availability
        return appointment_dao.create_appointment(data)

    def update_appointment(self, data: Any, id: int) -> Any:
        # TODO: Check doctr availability
        return appointment_dao.update_appointment(data, id)

    def delete_appointment(self, id: int) -> Any:
        return appointment_dao.delete_appointment(id)

    def get_doctor_appointments(self, id: int) -> Any:
        return appointment_dao.get_all_doctor_appointments(id)

    def get_patient_appointments(self, patient_id: int) -> Any:
        return appointment_dao.get_all_patient_appointments(patient_id)
