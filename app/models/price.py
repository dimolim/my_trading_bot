from dataclasses import dataclass
from datetime import datetime


@dataclass
class Price:
    symbol: str
    price: float
    time: datetime