import sqlite3

from db.db import DBService
from db.queries import staff_queries


class StaffDao:
    def doctor_row_mapper(self, doctor):
        return {
            "doctor_id": doctor[0],
            "name": doctor[1],
            "email": doctor[2],
            "specialization": doctor[3],
        }
    def get_active_doctors(self):
        sql=staff_queries.select_all
        doctors = DBService.query(sql, ())
        return [self.doctor_row_mapper(doctor) for doctor in doctors]

    def get_active_doctor(self, id: int):
        sql=staff_queries.select_one
        doctor = DBService.query_single(sql, {"StaffID": id})
        if doctor:
            return self.doctor_row_mapper(doctor)

    def create_doctor(self, data):
        sql=staff_queries.insert
        result = DBService.query_single(sql, {
                                                        "Name": data.name,
                                                        "Email": data.email,
                                                        "Password": data.password,
                                                        "SpecializationID": data.specialization_id
                                                    })
        return result[0]


    def update_doctor(self, data, id):
        sql = staff_queries.update
        DBService.update(sql, {
            "Name": data.name,
            "Email": data.email,
            "StaffID": id,
            "SpecializationID": data.specialization_id
        })

    def delete_doctor(self, id):
        sql = staff_queries.delete
        DBService.update(sql, {
            "IsActive": False,
            "StaffID": id
        })


