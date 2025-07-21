from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class HistoricalPrice(BaseModel):
  id: str
  coinName: str
  date: datetime
  price: float
  volume: float

  class Config:
    from_attributes = True
