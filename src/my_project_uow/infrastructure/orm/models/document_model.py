# mypy: ignore-errors
from datetime import datetime, UTC
from sqlalchemy.orm import relationship  

from .base_model import BaseOrmModel
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

class DocumentModel(BaseOrmModel):
    __tablename__ = 'document'

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    name: str = Column(String(50), nullable=False)
    description: str = Column(Text, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(UTC))
    updated_at: datetime = Column(DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))
    
    user_id: int = Column(BigInteger, ForeignKey('user.id'), nullable=False)
    user = relationship("UserModel", back_populates="documents")
