from pydantic import BaseModel
from typing import Optional

class Soldier(BaseModel):
    ID: int
    first_name:str
    last_name: str
    phone_number: int
    rank: str


class SoldierModelPatch(BaseModel):
    """Model for patching soldier information."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[int] = None
    rank: Optional[str] = None
    
    
