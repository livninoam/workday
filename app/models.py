# app/models.py

from sqlalchemy import Column, String, Integer, Enum, DateTime, func
from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base
import enum

class EnvType(str, enum.Enum):
    dev = "dev"
    stage = "stage"

class DevEnv(Base):
    __tablename__ = "dev_envs"
# Basic Fields that require to create all envs
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    group = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    env_type = Column(Enum(EnvType), nullable=False)
# Extended Fields for Timestamps so we will know when it was created/modified
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
