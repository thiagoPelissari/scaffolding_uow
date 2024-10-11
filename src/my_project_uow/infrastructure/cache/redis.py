import json
import logging
from typing import Any, override

from redis import asyncio as aioredis

from my_project_uow.business.interfaces import ICache
from my_project_uow.settings import Settings

_redis = None
logger = logging.getLogger(__name__)


class RedisCache(ICache):
    def __init__(self, *, settings: Settings, keys_prefix: str):
        self.keys_prefix = keys_prefix
        self.redis_url = settings.REDIS_URL
        self.default_expiration = settings.CACHE_DEFAULT_EXPIRATION

    async def _get_client(self):  # pragma: no cover
        global _redis
        if not _redis:
            _redis = aioredis.from_url(url=self.redis_url)
        return _redis

    async def _get_key(self, *, key: str) -> str:  # pragma: no cover
        return f'{self.keys_prefix}:{key}'

    @override
    async def get_cache(self, *, key: str) -> Any:  # pragma: no cover
        key = await self._get_key(key=key)
        client = await self._get_client()
        try:
            if data := await client.get(key):
                logger.debug('Cache hit', extra={'key': key})
                return json.loads(data)
        except Exception as ex:
            logger.error('Error getting cache', extra={'error': ex})
            return

    @override
    async def set_cache(self, *, key: str, data, expiration: int | None = None):  # pragma: no cover
        
        if not expiration:
            expiration = self.default_expiration

        key = await self._get_key(key=key)
        client = await self._get_client()
        try:
            await client.set(key, json.dumps(data), ex=expiration)
            logger.debug('Cache set', extra={'key': key})
        except Exception as ex:
            logger.error('Error setting cache', extra={'error': ex})
