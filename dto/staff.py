from typing import Optional

from pydantic import BaseModel, EmailStr, SecretStr


class Staff(BaseModel):
    staff_id: Optional[int] = None
    name: str
    email: EmailStr
    password: Optional[str] = None
    specialization_id: Optional[int] = None
    is_doctor: Optional[bool] = True

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None
        }