from dao.staff_dao import StaffDao
from tools.hash import hash_password

staff_dao = StaffDao()
class StaffService:
    def get_active_doctors(self):
        return staff_dao.get_active_doctors()

    def get_active_doctor(self, id: int):
        return staff_dao.get_active_doctor(id)

    def create_doctor(self, data):
        data.password = hash_password(data.password)
        doctor_id = staff_dao.create_doctor(data)
        return staff_dao.get_active_doctor(doctor_id)

    def update_doctor(self, data, id):
        staff_dao.update_doctor(data, id)
        return staff_dao.get_active_doctor(id)

    def delete_doctor(self, id):
        doctor = staff_dao.get_active_doctor(id)
        staff_dao.delete_doctor(id)
        return doctor
