from abc import ABC, abstractmethod
from app.core.database.schemas.PricesSchemas import HistoricalPrice, HistoricalPriceCreate
from typing import List

class PricesRepository(ABC):

  @abstractmethod
  def addPrices(self, prices: List[HistoricalPriceCreate]) -> List[HistoricalPrice] | None:
    pass

  @abstractmethod
  def getPrices(self) -> List[HistoricalPrice]:
    pass

  @abstractmethod
  def getPricesByCoinName(self, coinName: str) -> List[HistoricalPrice] |None:
    pass

  @abstractmethod
  def getPriceById(self, id: str) -> HistoricalPrice | None:
    pass
