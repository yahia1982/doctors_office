select_all = """
            SELECT StaffID, d.Name, Email, s.Name   
            FROM Staff d
                INNER JOIN Specialization s on d.SpecializationID =s.SpecializationID
            WHERE d.IsDoctor and d.IsActive 
            """


select_one = """
            SELECT StaffID, d.Name, Email, s.Name   
            FROM Staff d
                INNER JOIN Specialization s on d.SpecializationID =s.SpecializationID
            WHERE d.IsDoctor and d.IsActive and d.StaffID = :StaffID
            """

select_one2 = """
            SELECT StaffID, d.Name, Email, s.Name   
            FROM Staff d
                INNER JOIN Specialization s on d.SpecializationID =s.SpecializationID
            WHERE d.IsDoctor and d.StaffID = :StaffID
            """

insert = """
        INSERT INTO Staff (Name, Email, Password, SpecializationID, IsDoctor, IsActive) 
        VALUES(:Name, :Email, :Password, :SpecializationID, TRUE, TRUE) 
        RETURNING StaffID
        """

update = """
        UPDATE Staff 
        SET             
            Name=:Name, 
            Email=:Email,            
            SpecializationID=:SpecializationID
        WHERE 
            StaffID=:StaffID;
        """

delete = """
        UPDATE Staff 
        SET             
            IsActive=:IsActive
        WHERE 
            StaffID=:StaffID;
        """