from typing import Any

from dao.patient_dao import PatientDao
from dao.staff_dao import StaffDao
from db.db import DBService
from db.queries import prescription_queries

patient_dao = PatientDao()
staff_dao = StaffDao()


class PrescriptionsDao:

    def prescription_row_mapper(self, prescription: int) -> Any:
        if prescription:
            return {
                "prescription_id": prescription[0],
                "patient_id": patient_dao.get_patient(prescription[1]),
                "staff_id": staff_dao.get_doctor(prescription[2]),
                "medication_id": prescription[3],
                "dosage": prescription[4],
                "frequency": prescription[5],
                "start_date": prescription[6],
                "end_date": prescription[7],
            }

    def get_prescription(self, prescription_id: int) -> Any:
        sql = prescription_queries.select_one
        prescription = DBService.query_single(sql, {"PrescriptionID": prescription_id})
        if prescription:
            return self.prescription_row_mapper(prescription)

    def create_appointment(self, data: Any) -> Any:
        sql = prescription_queries.create
        prescription_id = DBService.query_single(sql, {
            "PatientID": data.patient_id,
            "StaffID": data.staff_id,
            "MedicationID": data.medication_id,
            "Dosage": data.dosage,
            "Frequency": data.frequency,
            "StartDate": data.start_date,
            "EndDate": data.end_date
        })
        if prescription_id:
            print(prescription_id)
            return self.get_prescription(prescription_id[0])

    def updates_prescription(self, data: Any, id: int) -> Any:
        sql = prescription_queries.update
        DBService.update(sql, {
            "PatientID": data.patient_id,
            "StaffID": data.staff_id,
            "MedicationID": data.medication_id,
            "Dosage": data.dosage,
            "Frequency": data.frequency,
            "StartDate": data.start_date,
            "EndDate": data.end_date,
            "PrescriptionID": id})
        return self.get_prescription(id)

    def delete_prescription(self, id: int) -> Any:
        sql = prescription_queries.delete
        prescription = self.get_prescription(id)
        if prescription:
            DBService.update(sql, {
                "PrescriptionID": id,
                "IsCancelled": True
            })
            return prescription

    def get_patient_prescription(self, prescription_id: int, patient_id: int) -> Any:
        sql = prescription_queries.select_patient_prescription
        prescription = DBService.query_single(sql, {
            "PrescriptionID": prescription_id,
            "PatientID": patient_id
        })

        return self.prescription_row_mapper(prescription)

    def get_doctor_prescription(self, prescription_id: int, doctor_id: int) -> Any:
        sql = prescription_queries.select_doctor_prescription
        prescription = DBService.query_single(sql, {
            "PrescriptionID": prescription_id,
            "StaffID": doctor_id
        })
        return self.prescription_row_mapper(prescription)

    def get_all_patient_prescriptions(self, patient_id: int) -> Any:
        sql = prescription_queries.select_all_patient_prescription
        prescriptions = DBService.query(sql, {
            "PatientID": patient_id
        })

        return [self.prescription_row_mapper(prescription) for prescription in prescriptions]

    def get_all_doctor_prescriptions(self, doctor_id: int) -> Any:
        sql = prescription_queries.select_all_doctor_prescription
        prescriptions = DBService.query(sql, {
            "StaffID": doctor_id
        })
        return [self.prescription_row_mapper(prescription) for prescription in prescriptions]
