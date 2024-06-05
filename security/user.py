from flask_login import UserMixin, LoginManager

from db.db import DBService
from security.personal_type import PersonalType

login_manager = LoginManager()
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role


@login_manager.user_loader
def load_user(user_id, role):
    if role == PersonalType.PATIENT:
        user = DBService.query_single('SELECT PatientID, Email, ? FROM Patient WHERE PatientID = ?', (PersonalType.PATIENT ,user_id,))
    else:
        user = DBService.query_single('SELECT StaffID, Email, ? FROM Patient WHERE StaffID = ?',
                                      (role, user_id,))

    if user:
        return User(*user)


