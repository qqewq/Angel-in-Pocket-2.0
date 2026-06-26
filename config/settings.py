import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    llm_model: str = "gpt-4"
    memory_backend: str = "postgresql+asyncpg://user:pass@localhost/memory"
    gra_core_path: str = "./gra_core"
    stripe_api_key: str = ""
    paypal_client_id: str = ""
    paypal_secret: str = ""
    crypto_wallet: str = ""
    tariff_plans: list = [{"id": "basic", "amount": 9.99, "stripe_price_id": "price_123"}]

    class Config:
        env_file = ".env"

settings = Settings()
