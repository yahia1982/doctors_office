from dao.prescriptions_dao import PrescriptionsDao

prescriptions_dao = PrescriptionsDao()


class PrescriptionsService:
    def create_prescription(self, data):
        return prescriptions_dao.create_appointment(data)

    def delete_prescription(self, id):
        return prescriptions_dao.delete_prescription(id)

    def update_prescription(self, data, id):
        return prescriptions_dao.updates_prescription(data, id)

    def get_patient_prescription(self, prescription_id, patient_id):
        return prescriptions_dao.get_patient_prescription(prescription_id, patient_id)

    def get_all_patient_prescriptions(self, patient_id):
        return prescriptions_dao.get_all_patient_prescriptions(patient_id)

    def get_doctor_prescription(self, prescription_id, doctor_id):
        return prescriptions_dao.get_doctor_prescription(prescription_id, doctor_id)

    def get_all_doctor_prescriptions(self, doctor_id):
        return prescriptions_dao.get_all_doctor_prescriptions(doctor_id)
