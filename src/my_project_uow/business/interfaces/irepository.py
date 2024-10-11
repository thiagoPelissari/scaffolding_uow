from __future__ import annotations

from .idocument import IDocument
from .iuser import IUser
from .icache import ICache

class IRepository:
    user: IUser
    document: IDocument
    cache: ICache


class IUnitOfWork:
    repository: IRepository
    
    async def __aenter__(self) -> IUnitOfWork:
        raise NotImplementedError()

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        await self.rollback()

        if exc_value:  # pragma: no cover
            raise exc_value

    async def commit(self):
        raise NotImplementedError()

    async def rollback(self):
        raise NotImplementedError()


class IUnitOfWorkMaker:
    async def __call__(self) -> IUnitOfWork:
        raise NotImplementedError()