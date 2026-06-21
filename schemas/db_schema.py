from pydantic import BaseModel
from typing import List

class Table(BaseModel):
    name: str
    columns: List[str]

class DBSchema(BaseModel):
    tables: List[Table]