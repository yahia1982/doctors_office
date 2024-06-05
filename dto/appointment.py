from datetime import date, time
from typing import Optional, Any

from pydantic import BaseModel, validator
from pydantic.main import Model


class Appointment(BaseModel):
    appointment_id: Optional[int] = None
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    reason: Optional[str] = None
    @validator('appointment_date')
    def validate(cls, value):
        if value < date.today():
            raise ValueError('Appointment date cannot be in the past')
        return value


    @validator('appointment_time')
    def validate(cls, value):
        if value < time(0, 0, 0):
            raise ValueError('Appointment time cannot be in the past')

        if value < time(8, 0, 0) or value < time(20, 0, 0):
            raise ValueError('Appointment time should be in working hours only (8 am to 8 pm)')

        return value
