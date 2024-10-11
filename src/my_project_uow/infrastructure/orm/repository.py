import json
from datetime import timedelta, UTC
from itertools import pairwise
from logging import getLogger
from typing import override, AsyncGenerator, cast

from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, Select

from my_project_uow.business.entities import DocumentEntity, UserEntity
from my_project_uow.business.exceptions import ObjectNotFound, DuplicateObject
from my_project_uow.business.interfaces import IRepository, ICache
from my_project_uow.infrastructure.orm.models import (UserModel, DocumentModel)

logger = getLogger(__name__)


class SqlAlchemyRepository(IRepository):
    def __init__(self, *, db_session: AsyncSession, cache: ICache):
        self.db_session = db_session
        self.cache = cache

    async def get_user(self, *, hash: str) -> UserEntity:
        # Primeiro, verifique se o usuário está no cache
        
        cached_user = await self.cache.get_cache(key=hash)
        if cached_user:
            return UserEntity(**json.loads(cached_user))

        # Caso não esteja no cache, busque no banco de dados
        statement = select(UserModel).where(UserModel.hash == hash)
        result = await self.db_session.execute(statement)
        user = result.scalars().one_or_none()

        if user:
            
            # Converter o modelo do usuário para a entidade
            user_entity = await self._user_model_to_entity(user)

            # Salvar o resultado no cache
            await self.cache.set_cache(key=hash, data=user_entity.json())


            return user_entity

        return None

            
            
            
    async def _user_model_to_entity(self, user_model: UserModel) -> UserEntity:
        return UserEntity(
            id=user_model.id,
            hash=user_model.hash,
            name=user_model.name,
            age=user_model.age,
            password=user_model.password,
            last_name=user_model.last_name,
            email=user_model.email,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
            is_active=user_model.is_active,
        )


    