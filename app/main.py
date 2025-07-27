import threading

from fastapi import FastAPI
from app.api import prices
from app.database.memory.MemoryPricesRepository import MemoryPricesRepository
from app.core.PricesSimulator import PricesSimulator

repo = MemoryPricesRepository()

simulator = PricesSimulator(repo)

app = FastAPI(title='Crypto Expert System API')

prices.set_repository(repo)

app.include_router(prices.router)


def run_simulator():
  simulator.simulatePriceChanges()

simulator_thread = threading.Thread(target=run_simulator, daemon=True)
simulator_thread.start()

@app.get('/')
def root():
  return {'message': 'Crypto Expert System API is running'}
