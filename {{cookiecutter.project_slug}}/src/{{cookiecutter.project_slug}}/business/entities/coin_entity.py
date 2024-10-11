from pydantic import BaseModel

class CoinEntity(BaseModel):
    id: int
    symbol: str
    value: float
    