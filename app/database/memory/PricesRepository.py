from typing import List
from app.core.database.PricesRepository import PricesRepository
from app.core.database.schemas.PricesSchemas import HistoricalPrice

class MemoryPricesRepository(PricesRepository):

  def __init__(self):
    self._prices: List[HistoricalPrice] = []

  def addPrice(self, price: HistoricalPrice) -> HistoricalPrice:
    self._prices.append(price)

  def getPricesByCoin(self, coin: str) -> List[HistoricalPrice]:
    return [price for price in self._prices if price.coin == coin]

  def clear(self) -> None:
    self._prices.clear()
