from fastapi import FastAPI
from app.api import prices

app = FastAPI(title='crypto Expert System API')

app.include_router(prices.router)

@app.get('/')
def root():
  return {'message': 'Crypto Expert System API is running'}
