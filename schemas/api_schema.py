from pydantic import BaseModel
from typing import List

class Endpoint(BaseModel):
    path: str
    method: str

class APISchema(BaseModel):
    endpoints: List[Endpoint]