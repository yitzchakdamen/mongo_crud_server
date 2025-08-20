from pydantic import BaseModel
from typing import Optional

class Soldier:
    
    def __init__(self, id:int, first_name:str, last_name:str, phone_number:int, rank:str) -> None:
        self._id:int = id 
        self.first_name:str = first_name
        self.last_name:str = last_name
        self.phone_number:int = phone_number
        self.rank:str = rank


class SoldierModelPatch(BaseModel):
    """Model for patching soldier information."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[int] = None
    rank: Optional[str] = None
    
class SoldierModelPost(BaseModel):
    """Model for creating a new soldier."""
    id: int
    first_name:str
    last_name: str
    phone_number: int
    rank: str