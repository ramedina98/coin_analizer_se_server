from abc import ABC, abstractmethod
from app.core.database.schemas.PricesSchemas import HistoricalPrice
from typing import List

class PricesRepository(ABC):

  @abstractmethod
  def getPrices(self) -> List[HistoricalPrice]:
    pass

  @abstractmethod
  def getPricesByCoinName(self, coinName: str) -> List[HistoricalPrice] |None:
    pass

  @abstractmethod
  def getPriceById(self, id: str) -> HistoricalPrice | None:
    pass
