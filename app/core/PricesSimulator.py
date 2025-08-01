import asyncio
import time
import random

from datetime import datetime
from app.api.prices import broadcastPriceUpdate
from app.core.database.PricesRepository import PricesRepository
from app.core.database.schemas.PricesSchemas import HistoricalPriceCreate

class PricesSimulator:
  priceRepository: PricesRepository

  def __init__(self, repo: PricesRepository):
    self.priceRepository = repo

  async def simulatePriceChanges(self):
    while True:
      currentPrices = self.priceRepository.getPrices()

      today = datetime.now().date()
      todayPrices = [
        p for p in currentPrices
        if datetime.fromisoformat(p.date).date() == today
      ]

      for price in todayPrices:
        changePercent = random.uniform(-0.5, 0.5)
        volumeChange = random.uniform(-0.03, 0.03)

        newPrice = round(price.price * (1 + changePercent / 100), 4)
        newVolume = int(price.volume * (1 + volumeChange))

        newEntry = HistoricalPriceCreate(
          coinName=price.coinName,
          date=datetime.now().isoformat(),
          price=newPrice,
          volume=newVolume
        )

        self.priceRepository.addPrices([newEntry])

        await broadcastPriceUpdate(newEntry)

      await asyncio.sleep(5)
