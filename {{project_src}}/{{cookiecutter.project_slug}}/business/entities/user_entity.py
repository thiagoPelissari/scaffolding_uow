from pydantic import BaseModel
from datetime import datetime

class UserEntity(BaseModel):
    id: int
    hash: str
    name: str
    age: int
    password: str
    last_name: str
    email: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    