from pydantic import BaseModel
from typing import List

class Page(BaseModel):
    name: str
    components: List[str]

class UISchema(BaseModel):
    pages: List[Page]