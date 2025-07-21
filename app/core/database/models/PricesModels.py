from datetime import datetime
from pydantic import BaseModel

class HistoricalPrice(BaseModel):
    id: str
    coinName: str
    date: datetime
    price: float
    volume: float
