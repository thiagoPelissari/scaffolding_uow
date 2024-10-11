from typing import Any

from sqlalchemy.orm import as_declarative


@as_declarative()
class BaseOrmModel:
    id: Any
    __name__: str
    __allow_unmapped__ = True
