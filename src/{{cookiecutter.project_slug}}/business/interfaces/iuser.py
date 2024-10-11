from __future__ import annotations

from typing import Any, AsyncGenerator
from {{ cookiecutter.project_slug }}.business.entities import UserEntity


class IUser:
    async def get_user(self, *, hash: str) -> UserEntity:
        raise NotImplementedError

    async def insert_user(self, *, user: UserEntity):
        raise NotImplementedError

    async def update_user(self, *, user: UserEntity):
        raise NotImplementedError
    
    async def delete_user(self, *, hash: str):
        raise NotImplementedError
    





