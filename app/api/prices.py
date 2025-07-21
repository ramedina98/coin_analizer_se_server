from fastapi import APIRouter
from typing import List
from app.core.database.schemas.PricesSchemas import HistoricalPrice
from app.database.memory.PricesRepository import MemoryPricesRepository

router = APIRouter(prefix='/api/prices', tags=['prices'])
repo = MemoryPricesRepository()

@router.get('/{coin}', response_model=List[HistoricalPrice])
def get_prices(coin: str):
  return repo.getPricesByCoin(coin)
