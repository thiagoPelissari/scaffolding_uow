from pydantic import BaseModel

class DocumentEntity(BaseModel):
    id: int
    name: str
    description: str
    