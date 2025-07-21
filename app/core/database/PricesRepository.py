from abc import ABC, abstractmethod
from typing import List
from app.core.database.schemas.PricesSchemas import HistoricalPrice

class PricesRepository(ABC):

  @abstractmethod
  def addPrice(self, price: HistoricalPrice) -> HistoricalPrice:
    pass

  @abstractmethod
  def getPricesByCoin(self, coin: str) -> List[HistoricalPrice]:
    pass

  @abstractmethod
  def clear(self) -> None:
    pass
