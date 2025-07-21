import requests

from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class CoinParams:
  coinId: str
  start: str

@dataclass
class CoinResponse:
  open: float
  high: float
  low: float
  close: float
  volume: float
  date: datetime

@dataclass
class CoinListResponse:
  id: str
  name: str
  symbol: str
  rank: int
  is_new: bool
  is_active: bool
  type: str

class HTTPCoinsData():
  api_url: str
  headers: Dict[str, str]

  def __init__(self, api_url):
    self.api_url = api_url
    self.headers = { "Accept": "application/json", "User-Agent": "myapp/1.0" }

  def fetchCoinsData(self) -> List[CoinListResponse]:
    base_url = f'{self.api_url}coins'
    response = requests.get(base_url, headers=self.headers)

    if response.status_code != 200:
      raise Exception(f"Failed to fetch the list of coins: status {response.status_code}")

    data = response.json()
    coinList = []

    for item in data:
      coinList.append(CoinListResponse(
        id = item['id'],
        name = item['name'],
        symbol = item['symbol'],
        rank = item['rank'],
        is_new = item['is_new'],
        is_active = item['is_active'],
        type = item['type']
      ))

    return coinList

  def fetchCoinStatusMarket(self, params: CoinParams) -> List[CoinResponse]:
    if params.start == "today":
        start_date = datetime.utcnow().date().isoformat()  # 'YYYY-MM-DD'
    else:
        start_date = params.start

    base_url = f'{self.api_url}coins/{params.coinId}/ohlcv/historical?start={start_date}'

    response = requests.get(base_url, headers=self.headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch updates for {params.coinId}: {response.status_code}")

    data = response.json()
    coinHistorical = []

    for item in data:
        coinHistorical.append(CoinResponse(
            open=item['open'],
            high=item['high'],
            low=item['low'],
            close=item['close'],
            volume=item['volume'],
            date=datetime.fromisoformat(item['time_open'].replace('Z', '+00:00'))
        ))

    return coinHistorical
