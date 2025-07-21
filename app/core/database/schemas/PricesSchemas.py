from pydantic import BaseModel
from datetime import datetime

class HistoricalPriceBase(BaseModel):
  coin: str
  date: datetime
  price: float
  volume: float

class HistoricalPriceCreate(HistoricalPriceBase):
  pass

class HistoricalPrice(HistoricalPriceBase):
  id: int

  class Config:
    from_attributes = True
