from dataclasses import dataclass

from app.models.candle_interval import CandleInterval


@dataclass
class CandleRequest:
    symbol: str
    interval: CandleInterval
    limit: int