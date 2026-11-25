from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class MonitorCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    url: HttpUrl
    interval_seconds: int = Field(default=60, ge=30, le=86400)


class MonitorRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    url: str
    interval_seconds: int
    is_active: bool
    created_at: datetime