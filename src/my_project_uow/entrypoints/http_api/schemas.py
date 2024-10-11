from __future__ import annotations

import time
from datetime import datetime
from pydantic import BaseModel, Field

from my_project_uow.business.entities import UserEntity


class UserInput(BaseModel):
    hash: str


class UserOutput(BaseModel):
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

    @classmethod
    def from_entity(cls, user: UserEntity) -> UserOutput:
        return UserOutput(
            id=user.id,
            hash=user.hash,
            name=user.name,
            age=user.age,
            password=user.password,
            last_name=user.last_name,
            email=user.email,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

