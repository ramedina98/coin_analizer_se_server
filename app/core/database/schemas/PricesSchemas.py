from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class HistoricalPriceBase(BaseModel):
  coinName: str
  date: datetime
  price: float
  volume: float

class HistoricalPriceCreate(HistoricalPriceBase):
  pass

class HistoricalPrice(HistoricalPriceBase):
  id: str

  class Config:
    from_attributes = True
