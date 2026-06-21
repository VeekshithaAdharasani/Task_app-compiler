from pydantic import BaseModel
from typing import List

class AppIntent(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]