# mypy: ignore-errors
from datetime import datetime, UTC
from .base_model import BaseOrmModel
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship  

class UserModel(BaseOrmModel):
    __tablename__ = 'user'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    hash: str = Column(String(60), nullable=False)
    name: str = Column(String(50), nullable=False)
    age: int = Column(Integer, nullable=False)
    password: str = Column(String(60), nullable=False)
    last_name: str = Column(String(50), nullable=False)
    email: str = Column(String(50), nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(UTC))
    updated_at: datetime = Column(DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))
    is_active: bool = Column(Boolean, default=True)

    # Relacionamento inverso, lista de documentos relacionados
    documents = relationship('DocumentModel', back_populates='user')
