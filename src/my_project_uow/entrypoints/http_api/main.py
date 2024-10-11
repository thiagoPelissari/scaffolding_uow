from fastapi import FastAPI

from my_project_uow.entrypoints.http_api.routers.healthz import health_check_router
from my_project_uow.entrypoints.http_api.routers.my_project_routers import my_project_router
from my_project_uow.factories import get_settings
from my_project_uow.utils.logging_utils import configure_logging

settings = get_settings()
configure_logging(
    root_level=settings.LOG_LEVEL_ROOT,
    uvicorn_level=settings.LOG_LEVEL_UVICORN,
    project_level=settings.LOG_LEVEL_PROJECT,
)

app = FastAPI(title='my_project', debug=settings.DEBUG)
app.include_router(health_check_router)
app.include_router(my_project_router)
