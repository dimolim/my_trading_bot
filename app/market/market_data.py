from app.models.Candle import Candle
from app.models.candle_interval import CandleInterval


class MarketData:
    def __init__(self, binance_service):
        self.binance_service = binance_service

    async def get_candles(self, symbol: str, interval: CandleInterval, limit: int) -> list[Candle]:
        return await self.binance_service.get_candles(symbol, interval, limit)

