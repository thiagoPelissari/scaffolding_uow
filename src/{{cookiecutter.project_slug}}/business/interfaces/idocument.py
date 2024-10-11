from __future__ import annotations

from typing import Any, AsyncGenerator
from {{ cookiecutter.project_slug }}.business.entities import DocumentEntity


class IDocument:
    async def get_document(self, *, hash: str) -> DocumentEntity:
        raise NotImplementedError

    async def insert_document(self, *, document: DocumentEntity):
        raise NotImplementedError

    async def update_document(self, *, document: DocumentEntity):
        raise NotImplementedError
    
    async def delete_document(self, *, hash: str):
        raise NotImplementedError
    





