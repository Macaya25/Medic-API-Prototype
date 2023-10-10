from pydantic import BaseModel

class CenterCreateSchema(BaseModel):
    name: str
    location: str