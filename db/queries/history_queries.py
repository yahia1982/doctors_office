select_one = """
   SELECT HistoryID, PatientID, StaffID, Diagnosis, Treatment, Notes 
   FROM MedicalHistory
   WHERE HistoryID=:HistoryID;
"""

select_all_patients = """
   SELECT HistoryID, PatientID, StaffID, Diagnosis, Treatment, Notes 
   FROM MedicalHistory
"""

select_all_for_patient = """
   SELECT HistoryID, PatientID, StaffID, Diagnosis, Treatment, Notes 
   FROM MedicalHistory
   WHERE PatientID=:PatientID;
"""


create = """
   INSERT INTO MedicalHistory (PatientID, StaffID, Diagnosis, Treatment, Notes)
   VALUES (:PatientID, :StaffID, :Diagnosis, :Treatment, :Notes)
   RETURNING HistoryID;
"""

update = """
   UPDATE MedicalHistory
   SET 
      PatientID=:PatientID, 
      StaffID=:StaffID, 
      Diagnosis=:Diagnosis, 
      Treatment=:Treatment,    
      Notes=:Notes
    WHERE
         HistoryID=:HistoryID;
"""

delete = """
    DELETE FROM 
        MedicalHistory   
    WHERE
         HistoryID=:HistoryID;
"""
