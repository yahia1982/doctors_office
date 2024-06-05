from typing import Any

from db.db import DBService
from db.queries import patient_queries


class PatientDao:

    def patient_row_mapper(self, patient):
        return {
            "name": patient[0],
            "email": patient[1],
            "date_of_birth": patient[2],
            "address": patient[3]
        }
    def get_all_patients(self):
        sql=patient_queries.select_all
        patients = DBService.query(sql, ())
        return [self.patient_row_mapper(patient) for patient in patients]

    def get_patient(self, id: int):
        sql=patient_queries.select_one
        patient = DBService.query_single(sql, {"PatientID": id})
        if patient:
            return self.patient_row_mapper(patient)

    def create_patient(self, data):
        sql=patient_queries.create
        patient_id = DBService.query_single(sql, {"Name": data.name,
                                                            "Email": data.email,
                                                            "Password": data.password,
                                                            "DateOfBirth": data.date_of_birth,
                                                            "Address": data.address})

        if patient_id:
            return self.get_patient(patient_id[0])

    def delete_patient(self, id: int):
        sql=patient_queries.delete
        patient = self.get_patient(id)
        DBService.update(sql, {"IsActive": False, "PatientID": id})
        if patient:
            return patient

    def update_patient(self, data: Any, id: int):
        sql = patient_queries.update
        DBService.query_single(sql, {   "Name": data.name,
                                                  "Email": data.email,
                                                  "DateOfBirth": data.date_of_birth,
                                                  "Address": data.address,
                                                  "PatientID": id})
        return self.get_patient(id)

    def get_patient_by_email(self, email):
        sql = patient_queries.select_one_by_email
        patient = DBService.query_single(sql, {"Email": email})
        if patient:
            return {"PatientID": patient[0], "Email": patient[1], "Password": patient[2]}

