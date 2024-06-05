from typing import Any

from dao.patient_dao import PatientDao
from tools.hash import hash_password

patient_dao = PatientDao()
class PatientService:
    def get_all_patients(self):
        return patient_dao.get_all_patients()

    def get_patient(self, id: int):
        return patient_dao.get_patient(id)

    def update_patient(self, data: Any, id: int):
        return patient_dao.update_patient(data, id)

    def delete_patient(self, id: int):
        return patient_dao.delete_patient(id)

    def create_patient(self, data):
        data.password = hash_password(data.password)
        return patient_dao.create_patient(data)