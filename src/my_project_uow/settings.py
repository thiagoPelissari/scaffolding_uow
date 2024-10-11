from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    LOG_LEVEL_ROOT: str = 'INFO'
    LOG_LEVEL_UVICORN: str = 'INFO'
    LOG_LEVEL_PROJECT: str = 'INFO'

    # Database
    DATABASE_URL: str
    ECHO_SQL: bool = False
    DATABASE_POOL_SIZE: int = 10

    # Cron scheduling
    SCHEDULER_CONDITION_: str = 'every 20 seconds'

    # HTTP API
    API_KEY: str = ''

    # Cache
    REDIS_URL: str = ''  # format: redis://<host>:<port>
    CACHE_DEFAULT_EXPIRATION: int = 2 * 60 # 2 minutes
    CACHE_KEY_PREFIX: str = 'my_project_uow'
