from fastapi import Depends, Security
from fastapi.security.api_key import APIKeyHeader

from my_project_uow.entrypoints.http_api.exceptions import NotAuthorizedException
from my_project_uow.settings import Settings
from my_project_uow.factories import get_settings

api_key_header = APIKeyHeader(name='API_KEY', auto_error=False)


async def api_key_validate(settings: Settings = Depends(get_settings), api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise NotAuthorizedException()
