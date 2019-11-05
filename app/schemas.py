from typing import Dict

from pydantic import BaseModel

class APIResponseSchema(BaseModel):
    id: int
    timestamp_start: float
    timestamp_end: float
    ip_address: str
    api_response: Dict

    class Config:
        orm_mode = True
