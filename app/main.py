import asyncio

from fastapi import FastAPI
from app.api import prices
from app.database.memory.MemoryPricesRepository import MemoryPricesRepository
from app.core.PricesSimulator import PricesSimulator

repo = MemoryPricesRepository()

simulator = PricesSimulator(repo)

app = FastAPI(title='Crypto Expert System API')

prices.set_repository(repo)

app.include_router(prices.router)

@app.on_event('startup')
async def startUp():
  asyncio.create_task(simulator.simulatePriceChanges())

@app.get('/')
def root():
  return {'message': 'Crypto Expert System API is running'}
