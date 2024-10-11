from typing import cast

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.project_slug }}.settings import Settings

maker: sessionmaker | None = None
async_engine: AsyncEngine | None = None


async def get_async_session_maker(*, settings: Settings) -> sessionmaker:
    global maker
    global async_engine

    if maker:
        return maker

    if not async_engine:  # pragma: no branch
        database_url = settings.DATABASE_URL
        engine_kwargs = {
            'echo': settings.ECHO_SQL,
        }
        if 'sqlite' not in database_url:  # pragma: no cover
            engine_kwargs.update(  # type: ignore[call-overload]
                isolation_level='READ COMMITTED',
                pool_size=settings.DATABASE_POOL_SIZE,
                pool_recycle=-1,
            )

        async_engine = create_async_engine(database_url, **engine_kwargs)

    maker = sessionmaker(  # type: ignore[call-overload]
        bind=async_engine,
        class_=AsyncSession,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
    return cast(sessionmaker, maker)
