from app.core.database.schemas.PricesSchemas import HistoricalPrice
from app.database.memory.MemoryPricesRepository import MemoryPricesRepository
from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect, WebSocketException
from typing import List

router = APIRouter(prefix='/api/se/prices', tags=['prices'])

activeConnections: List[WebSocket] = []

repo: MemoryPricesRepository = None

def set_repository(memoryRepository: MemoryPricesRepository):
  global repo
  repo = memoryRepository

@router.get('/', response_model=List[HistoricalPrice])
def getPrices():
  return repo.getPrices()

@router.get('/by-coin/{coin}', response_model=List[HistoricalPrice])
def getPricesByCoinName(coin: str):
  prices = repo.getPricesByCoinName(coin)

  if prices == None:
    raise HTTPException(status_code=404, detail=f'COIN_NAME_NOT_FOUND')

  return prices

@router.get('/by-id/{id}', response_model=HistoricalPrice)
def getPriceById(id: str):
  price = repo.getPriceById(id)

  if price == None:
    raise HTTPException(status_code=404, detail=f'COIN_ID_NOT_FOUND')

  return price

# Web socket needed to seend the updated prices on real time...
@router.websocket('/ws')
async def websocketPrices(websocket: WebSocket):
  await websocket.accept()
  activeConnections.append(websocket)

  try:
    while True:
      await websocket.receive_text()
  except WebSocketDisconnect:
    activeConnections.remove(websocket)

async def broadcastPriceUpdate(message: HistoricalPrice):
  jsonData = message.json()

  for connection in activeConnections:
    await connection.send_tex(jsonData)