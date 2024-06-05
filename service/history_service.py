from typing import Any

from dao.history_dao import HistoryDao

history_dao = HistoryDao()
class HistoryService:
    def get_medical_history(self, id: int)->Any:
        return history_dao.get_medical_history(id)

    def get_all_medical_history(self, patient_id: int)->Any:
        if patient_id!=-1:
            return history_dao.get_all_patient_medical_history(patient_id)
        else:
            return history_dao.get_all_medical_history()


    def create_medical_history(self, data: Any)->Any:
        return history_dao.create_medical_history(data)

    def update_medical_history(self, data: Any, id: int)->Any:
        return history_dao.update_medical_history(data, id)

    def delete_medical_history(self, id: int)->Any:
        return history_dao.delete_medical_history(id)

