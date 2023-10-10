from pydantic import BaseModel

class DoctorCreateSchema(BaseModel):
    name: str
    genderMale: bool
    specialty_id: int