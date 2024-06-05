select_all_by_doctor = """
    SELECT AppointmentID, PatientID, AppointmentDate, AppointmentTime, Reason 
    FROM Appointment
    where StaffID =:StaffID  
    """

select_all_by_patient = """
    SELECT AppointmentID, StaffID, AppointmentDate, AppointmentTime, Reason 
    FROM Appointment
    where PatientID =:PatientID 
    """

select_one_by_doctor = """
    SELECT AppointmentID, PatientID, AppointmentDate, AppointmentTime, Reason 
    FROM Appointment
    where StaffID =:StaffID  and  AppointmentID=:AppointmentID
    """

select_one_by_patient = """
    SELECT AppointmentID, StaffID, AppointmentDate, AppointmentTime, Reason 
    FROM Appointment
    where PatientID =:PatientID and  AppointmentID=:AppointmentID
    """

select_one = """
    SELECT AppointmentID, StaffID, PatientID, AppointmentDate, AppointmentTime, Reason 
    FROM Appointment
    where AppointmentID=:AppointmentID
    """


create = """
    INSERT INTO Appointment (PatientID, StaffID, AppointmentDate, AppointmentTime, Reason) 
    VALUES(:PatientID, :StaffID, :AppointmentDate, :AppointmentTime, :Reason) 
    RETURNING AppointmentID
    """

delete = """
    UPDATE Appointment SET IsCancelled=:IsCancelled WHERE AppointmentID = :AppointmentID 
    RETURNING AppointmentID"""

update = """
    UPDATE Appointment SET PatientID = :PatientID, StaffID = :StaffID, AppointmentDate = :AppointmentDate, AppointmentTime = :AppointmentTime, Reason = :Reason
    WHERE AppointmentID = :AppointmentID    
    """


