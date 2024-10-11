from fastapi import Depends, Security
from fastapi.security.api_key import APIKeyHeader

from {{ cookiecutter.project_slug }}.entrypoints.http_api.exceptions import NotAuthorizedException
from {{ cookiecutter.project_slug }}.settings import Settings
from {{ cookiecutter.project_slug }}.factories import get_settings

api_key_header = APIKeyHeader(name='API_KEY', auto_error=False)


async def api_key_validate(settings: Settings = Depends(get_settings), api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise NotAuthorizedException()
