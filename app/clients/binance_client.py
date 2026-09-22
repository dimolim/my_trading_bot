from aiohttp import ClientSession
from app.models.candle_interval import CandleInterval

BASE_URL = "https://api.binance.com"
TICKER_PRICE_ENDPOINT = "/api/v3/ticker/price"
CANDLE_PRICE_ENDPOINT = "/api/v3/klines"

class BinanceClient:

    def __init__(self, session: ClientSession):
        self.session = session

    async def get_current_price(self, symbol: str):

        url = f"{BASE_URL}{TICKER_PRICE_ENDPOINT}"

        async with self.session.get(
                url,
                params={"symbol": symbol}
        ) as response:
            if response.status != 200:
                raise Exception(response.status)

            return await response.json()

    async def get_candles(self, symbol: str, interval: CandleInterval, limit: int):

        url = f"{BASE_URL}{CANDLE_PRICE_ENDPOINT}"
        async with self.session.get(
            url,
                params={"symbol": symbol,
                        "interval": interval,
                        "limit": limit}
        ) as response:
            if response.status != 200:
                text = await response.text()
                raise Exception(
                    f"Binance error {response.status}: {text}"
                )

            return await response.json()