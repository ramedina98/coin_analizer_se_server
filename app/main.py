from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
from app.api import prices
from app.database.memory.MemoryPricesRepository import MemoryPricesRepository
from app.utils.HTTPCoinsData import HTTPCoinsData

app = FastAPI(title='Crypto Expert System API')

app.include_router(prices.router)

repo = MemoryPricesRepository()
coins_client = HTTPCoinsData("https://api.coinpaprika.com/v1/")
coins = ["btc-bitcoin", "eth-ethereum", "ltc-litecoin"]

@app.get('/')
def root():
  return {'message': 'Crypto Expert System API is running'}
