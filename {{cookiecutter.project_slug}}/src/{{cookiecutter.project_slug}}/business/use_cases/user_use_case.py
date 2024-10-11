from contextlib import suppress
from logging import getLogger

from {{ cookiecutter.project_slug }}.business.exceptions import ObjectNotFound
from {{ cookiecutter.project_slug }}.business.interfaces import IUnitOfWorkMaker

logger = getLogger(__name__)


class UserUseCase:
    def __init__(self, *, uow_maker: IUnitOfWorkMaker):
        self.uow_maker = uow_maker

    async def get_user(self, *, hash: str) -> dict | None:
        async with await self.uow_maker() as unit_of_work:
            user = await unit_of_work.repository.get_user(hash=hash)
            if user:
                return user
            
            raise ObjectNotFound(f'User not found in the database hash: {hash}')

        return None
