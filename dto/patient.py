from datetime import date
from typing import Optional

from pydantic import EmailStr, BaseModel


class Patient(BaseModel):
    patient_id: Optional[int]=None
    name: str
    email: EmailStr
    password: Optional[str]=None
    date_of_birth: date
    address: str
