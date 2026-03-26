from pydantic import BaseModel
from typing import List

class state(BaseModel):
    ticket: str
    status: str
    history: List[str]
    customer_mood: str
    order_status: str
    time_left: int
