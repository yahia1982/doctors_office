from typing import Optional

from pydantic import BaseModel


class MedicalHistory(BaseModel):
    history_id: Optional[int] = None
    patient_id: int
    staff_id: int
    diagnosis: str
    treatment: str
    notes: Optional[str] = None
