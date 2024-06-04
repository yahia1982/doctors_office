from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class Appointment(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    Reason: Optional[str]
