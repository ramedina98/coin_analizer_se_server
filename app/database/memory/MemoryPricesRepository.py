import json
import os
import uuid

from typing import List
from datetime import datetime
from app.core.database.PricesRepository import PricesRepository
from app.core.database.schemas.PricesSchemas import HistoricalPrice, HistoricalPriceCreate

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_DIR, '../../../data/historicalPrices.json'))

class MemoryPricesRepository(PricesRepository):
  filePath: str

  def __init__(self):
    self.filePath = FILE_PATH
    self._prices: List[HistoricalPrice] = []

    self.__readJSONFile()

  def addPrices(self, prices: List[HistoricalPriceCreate]) -> List[HistoricalPrice] | None:
    newPrices = [
      HistoricalPrice(
        id=str(uuid.uuid4()),
        coinName=price.coinName,
        date=price.date,
        price=price.price,
        volume=price.volume
      )
      for price in prices
    ]

    self._prices.extend(newPrices)
    return newPrices

  def getPrices(self) -> List[HistoricalPrice]:
    return self._prices

  def getPricesByCoinName(self, coinName: str) -> List[HistoricalPrice] | None:
    coinList = [price for price in self._prices if price.coinName.lower() == coinName.lower()]

    return coinList if coinList else None

  def getPriceById(self, id: str) -> HistoricalPrice | None:
    coinFound: HistoricalPrice = None

    for price in self._prices:
      if price.id == id:
        coinFound = price

    return coinFound if coinFound else None

  def __readJSONFile(self):
    with open(self.filePath, 'r') as file:
      data = json.load(file)

    for item in data:
      self._prices.append(HistoricalPrice(
        id=str(uuid.uuid4()),
        coinName=item['coinName'],
        date=datetime.now().isoformat(),
        price=item['price'],
        volume=item['volume']
      ))
