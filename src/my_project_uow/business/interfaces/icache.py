from typing import Any

class ICache:
    async def get_cache(self, *, key: str) -> Any:
        raise NotImplementedError()

    async def set_cache(self, *, key: str, data, expiration: int | None = None):
        raise NotImplementedError()