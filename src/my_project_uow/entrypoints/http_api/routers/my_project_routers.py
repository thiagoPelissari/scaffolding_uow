from fastapi import APIRouter, Depends, HTTPException

from my_project_uow.auth import api_key_validate
from my_project_uow.business.interfaces.irepository import IUnitOfWorkMaker
from my_project_uow.entrypoints.http_api.dependencies import get_unit_of_work_maker
from my_project_uow.entrypoints.http_api.exceptions import HttpResponseException
from my_project_uow.entrypoints.http_api.schemas import UserInput, UserOutput
from my_project_uow.business.use_cases.user_use_case import UserUseCase

my_project_router = APIRouter(
    tags=['my_project'],
    dependencies=[Depends(api_key_validate)],
)


@my_project_router.get(
    '/get_user/',
    summary='Get user by Hash',
)
async def get_user(
    hash: str,
    uow_maker: IUnitOfWorkMaker = Depends(get_unit_of_work_maker),
):
    try:
        use_case = UserUseCase(uow_maker=uow_maker)
        user = await use_case.get_user(hash=hash)
        
        return UserOutput.from_entity(user)
        
        #TODO  Delete DB and implement CheckDB in makefile | Fix Logs | 
        
        
    except Exception as e:
        return HttpResponseException(e).get_response()


