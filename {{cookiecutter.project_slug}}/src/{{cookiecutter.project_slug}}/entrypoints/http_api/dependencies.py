from fastapi import Depends
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.project_slug }} import factories
from {{ cookiecutter.project_slug }}.business.interfaces import IUnitOfWorkMaker, ICache
from {{ cookiecutter.project_slug }}.settings import Settings


async def get_db_session_maker(*, settings: Settings = Depends(factories.get_settings)) -> sessionmaker:
    return await factories.get_db_session_maker(settings=settings)


async def get_cache(*, settings: Settings = Depends(factories.get_settings)) -> ICache:
    return await factories.get_cache(settings=settings)


async def get_unit_of_work_maker(
    db_session_maker: sessionmaker = Depends(get_db_session_maker),
    cache: ICache = Depends(get_cache),
) -> IUnitOfWorkMaker:
    return await factories.get_unit_of_work_maker(db_session_maker=db_session_maker, cache=cache)
