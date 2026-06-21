from pydantic import BaseModel
from typing import List

class SystemDesign(BaseModel):
    entities: List[str]
    pages: List[str]
    roles: List[str]