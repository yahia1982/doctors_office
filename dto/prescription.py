from datetime import date
from typing import Optional

from pydantic import BaseModel


class Prescription(BaseModel):
    prescription_id: Optional[int] = None
    patient_id: int
    staff_id: int
    medication_id: int
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    start_date: Optional[date]
    end_date: Optional[date]
