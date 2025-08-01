from pydantic import BaseModel

class HistoricalPrice(BaseModel):
    id: str
    coinName: str
    date: str
    price: float
    volume: float
