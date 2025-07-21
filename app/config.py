from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  coingecko_api_url: str = "https://api.coingecko.com/api/v3"

  class Config:
    env_file = '.env'

setting = Settings()
