# app/schemas.py

from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID
from typing import Optional

class EnvType(str, Enum):
    dev = "dev"
    stage = "stage"

class DevEnvBase(BaseModel):
    name: str
    owner: str
    group: str
    duration: int  # Duration in hours or seconds

    env_type: EnvType

class DevEnvCreate(DevEnvBase):
    pass

class DevEnvUpdate(BaseModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    group: Optional[str] = None
    duration: Optional[int] = None
    env_type: Optional[EnvType] = None

class DevEnvResponse(DevEnvBase):
    id: UUID

