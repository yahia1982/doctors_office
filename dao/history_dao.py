from typing import Any

from dao.patient_dao import PatientDao
from dao.staff_dao import StaffDao
from db.db import DBService
from db.queries import history_queries

patient_dao = PatientDao()
staff_dao = StaffDao()


class HistoryDao:

    def history_row_mapper(self, history):
        if history:
            return {
                "history_id": history[0],
                "patient_id": patient_dao.get_patient(history[1]),
                "doctor_id": staff_dao.get_doctor(history[2]),
                "Diagnosis": history[3],
                "Treatment": history[4],
                "Notes": history[5]
            }

    def get_medical_history(self, id: int) -> Any:
        sql = history_queries.select_one
        history = DBService.query_single(sql, {
            "HistoryID": id
        })
        if history:
            return self.history_row_mapper(history)

    def get_all_medical_history(self):
        sql = history_queries.select_all_patients
        history = DBService.query(sql, ())
        return [self.history_row_mapper(h) for h in history]

    def get_all_patient_medical_history(self, patient_id: int)->Any:
        sql = history_queries.select_all_for_patient
        history = DBService.query(sql, {"PatientID": patient_id})
        return [self.history_row_mapper(h) for h in history]

    def create_medical_history(self, data: Any) -> Any:
        sql = history_queries.create
        history_id = DBService.query_single(sql, {
            "PatientID": data.patient_id,
            "StaffID": data.staff_id,
            "Diagnosis": data.diagnosis,
            "Treatment": data.treatment,
            "Notes": data.notes
        })
        if history_id:
            return self.get_medical_history(history_id[0])

    def update_medical_history(self, data: Any, id: int) -> Any:
        sql = history_queries.update
        DBService.update(sql, {
            "PatientID": data.patient_id,
            "StaffID": data.staff_id,
            "Diagnosis": data.diagnosis,
            "Treatment": data.treatment,
            "Notes": data.notes,
            "HistoryID": id})
        return self.get_medical_history(id)

    def delete_medical_history(self, id: int) -> Any:
        sql = history_queries.delete
        history = self.get_medical_history(id)
        DBService.update(sql, {"HistoryID": id})
        return history
