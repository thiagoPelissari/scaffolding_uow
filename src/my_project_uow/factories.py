from __future__ import annotations

from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

from my_project_uow.business.interfaces import IUnitOfWorkMaker
from my_project_uow.infrastructure.orm.unit_of_work import SqlAlchemyUnitOfWork
from my_project_uow.infrastructure.orm.session_maker import get_async_session_maker
from my_project_uow.settings import Settings
from my_project_uow.business.interfaces import ICache
from my_project_uow.infrastructure.cache.fake import FakeCache
from my_project_uow.infrastructure.cache.redis import RedisCache

_settings: Settings | None = None
_cache: ICache | None = None
_uow_maker: IUnitOfWorkMaker | None = None


def get_settings() -> Settings:
    global _settings

    if not _settings:
        _settings = Settings()

    return _settings


async def get_cache(*, settings: Settings) -> ICache:
    global _cache

    if not _cache:
        if settings.REDIS_URL:
            _cache = RedisCache(settings=settings, keys_prefix=settings.CACHE_KEY_PREFIX)
        else:
            _cache = FakeCache()

    return _cache


async def get_db_session_maker(*, settings: Settings) -> sessionmaker:
    return await get_async_session_maker(settings=settings)


async def get_unit_of_work_maker(
    *,
    db_session_maker: sessionmaker,
    cache: ICache,
) -> IUnitOfWorkMaker:
    global _uow_maker

    if not _uow_maker:

        class UOWMaker(IUnitOfWorkMaker):
            async def __call__(self):
                return SqlAlchemyUnitOfWork(db_session_maker=db_session_maker, cache=cache)

        _uow_maker = UOWMaker()

    return _uow_maker
