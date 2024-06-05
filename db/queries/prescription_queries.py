select_one="""
    SELECT PrescriptionID, PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate
    FROM Prescription
    WHERE PrescriptionID=:PrescriptionID AND NOT IsCancelled;
"""

select_patient_prescription="""
    SELECT PrescriptionID, PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate
    FROM Prescription
    WHERE PrescriptionID=:PrescriptionID AND PatientID=:PatientID AND NOT IsCancelled;
"""

select_all_patient_prescription="""
    SELECT PrescriptionID, PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate
    FROM Prescription
    WHERE PatientID=:PatientID AND NOT IsCancelled;
"""


select_doctor_prescription="""
    SELECT PrescriptionID, PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate
    FROM Prescription
    WHERE PrescriptionID=:PrescriptionID AND StaffID=:StaffID AND NOT IsCancelled;
"""

select_all_doctor_prescription="""
    SELECT PrescriptionID, PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate
    FROM Prescription
    WHERE StaffID=:StaffID AND NOT IsCancelled;
"""

select_all="""
    SELECT PrescriptionID, PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate
    FROM Prescription;
"""

create="""
    INSERT INTO Prescription (PatientID, StaffID, MedicationID, Dosage, Frequency, StartDate, EndDate) 
    VALUES(:PatientID, :StaffID, :MedicationID, :Dosage, :Frequency, :StartDate, :EndDate)
    RETURNING PrescriptionID;
"""


update="""
    UPDATE Prescription
    SET 
        PatientID=:PatientID, 
        StaffID=:StaffID, 
        MedicationID=:MedicationID, 
        Dosage=:Dosage, 
        Frequency=:Frequency, 
        StartDate=:StartDate, 
        EndDate=:EndDate
    WHERE 
        PrescriptionID=:PrescriptionID;
"""

delete="""
    UPDATE Prescription
    SET 
        IsCancelled=:IsCancelled
    WHERE 
        PrescriptionID=:PrescriptionID;
"""


