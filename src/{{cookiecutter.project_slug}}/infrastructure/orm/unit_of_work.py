from typing import override

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.project_slug }}.business.interfaces import IUnitOfWork, ICache
from {{ cookiecutter.project_slug }}.infrastructure.orm.repository import SqlAlchemyRepository


class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, db_session_maker: sessionmaker, cache: ICache):
        self.db_session_maker = db_session_maker
        self.cache = cache

    @override
    async def __aenter__(self) -> IUnitOfWork:
        self.db_session: AsyncSession = self.db_session_maker()
        self.repository = SqlAlchemyRepository(db_session=self.db_session, cache=self.cache)
        return self

    @override
    async def commit(self):
        await self.db_session.commit()

    @override
    async def rollback(self):
        await self.db_session.rollback()
