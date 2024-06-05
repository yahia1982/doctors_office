from flask_login import login_user

from dao.patient_dao import PatientDao
from dao.staff_dao import StaffDao
from security.personal_type import PersonalType
from tools.passwords import check_password
from security.user import User

patient_dao = PatientDao()
staff_dao = StaffDao()

class UserService:
    def login(self, data):
        staff = staff_dao.get_staff_by_email(data.email)
        if staff and check_password(staff.get("Password"), data.password):
            login_user(User(staff.get("StaffID"),
                            staff.get("Email"),
                            PersonalType.DOCTOR if staff.get("IsDoctor") else PersonalType.ADMINISTRATION_STAFF))
            return {'message': 'Logged in successfully!'}, 200

        patient = patient_dao.get_patient_by_email(data.email)
        if patient and check_password(staff.get("Password"), data.password):
            login_user(User(staff.get("PatientID"),
                            staff.get("Email"),
                            PersonalType.PATIENT))
            return {'message': 'Logged in successfully!'}, 200

        return {'message': 'Login failed. Check your credentials.'}, 401
