from datetime import datetime, UTC


from app.clients.binance_client import BinanceClient
from app.models import candle_interval
from app.models.Candle import Candle
from app.models.price import Price
from aiohttp import ClientSession
from app.models.candle_interval import CandleInterval


class BinanceService:

    def __init__(self, client: BinanceClient):
        self.client = client

    async def get_current_price(self, symbol: str) -> Price:
        data = await self.client.get_current_price(symbol)

        return Price(
            symbol=data["symbol"],
            price=float(data["price"]),
            time=datetime.now(UTC)
        )


    async def get_historical_price(self, symbol: str, start, end):
        pass

    async def get_candles(self, symbol: str, interval: CandleInterval, limit: int):
        data = await self.client.get_candles(
            symbol,
            interval.value,
            limit
        )
        candles = []
        for candle in data:
            candle_data = Candle(
                open_time=datetime.fromtimestamp(candle[0] / 1000, UTC),
                open= float(candle[1]),
                high=float(candle[2]),
                low=float(candle[3]),
                close=float(candle[4]),
                volume=float(candle[5]),
            )
            candles.append(candle_data)
        return candles

    async def get_market_depth(self):
        pass

