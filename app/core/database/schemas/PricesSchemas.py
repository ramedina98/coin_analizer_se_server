from pydantic import BaseModel

class HistoricalPriceBase(BaseModel):
  coinName: str
  date: str
  price: float
  volume: float

class HistoricalPriceCreate(HistoricalPriceBase):
  pass

class HistoricalPrice(HistoricalPriceBase):
  id: str

  class Config:
    from_attributes = True
