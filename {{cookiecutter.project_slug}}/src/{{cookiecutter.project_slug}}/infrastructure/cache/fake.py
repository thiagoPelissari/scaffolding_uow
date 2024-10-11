from typing import Any, override

from {{ cookiecutter.project_slug }}.business.interfaces import ICache


class FakeCache(ICache):
    @override
    async def get_cache(self, *, key: str) -> Any:
        return

    @override
    async def set_cache(self, *, key: str, data, expiration: int | None = None):
        pass
