select_all= """
        SELECT Name, Email, DateOfBirth, Address FROM Patient;
        """

select_one= """
        SELECT Name, Email, DateOfBirth, Address FROM Patient WHERE PatientID = :PatientID;
        """


create="""
    INSERT INTO Patient (Name, Email, Password, DateOfBirth, Address, IsActive) 
    VALUES(:Name, :Email, :Password, :DateOfBirth, :Address, TRUE)
    RETURNING PatientID;
"""

update = """
    UPDATE Patient 
    SET 
        Name=:Name, 
        Email=:Email, 
        DateOfBirth=:DateOfBirth, 
        Address=:Address       
    WHERE 
        PatientID=:PatientID;
"""

delete="""
     UPDATE Patient 
    SET         
        IsActive=:IsActive 
    WHERE 
        PatientID=:PatientID;
"""
