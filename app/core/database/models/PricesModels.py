from datetime import datetime
from pydantic import BaseModel

class HistoricalPrice(BaseModel):
    id: int
    coin: str
    date: datetime
    price: float
    volume: float
