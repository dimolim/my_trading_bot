import asyncio
from aiohttp import ClientSession
from app.clients.binance_client import BinanceClient
from app.market.indicators import Indicators
from app.market.market_data import MarketData
from app.services.binance_service import BinanceService
from app.models.candle_interval import CandleInterval
from aiogram import Bot, Dispatcher
from app.config.settings import settings
from app.bot.routers.routers import router


async def main():
    bot = Bot(token=settings.bot_token)

    async with ClientSession() as session:
        client = BinanceClient(session)
        binance_service = BinanceService(client)

        dp = Dispatcher()
        dp.include_router(router)

        market_data = MarketData(binance_service)
        indicators = Indicators()

        candles = await market_data.get_candles(
            "BTCUSDT",
            CandleInterval.MINUTE_5,
            100
        )
        sma = indicators.sma(candles, 20)
        print(candles)
        print(f"SMA: {sma:.2f}")
        ema = indicators.ema_series(candles, 5)
        print(f"EMA: {ema}")
        rsi = indicators.rsi(candles, 14)
        print(f"RSI: {rsi:.2f}")
        print("Количество свечей:", len(candles))
        result = indicators.macd(candles)

        print("MACD:", result.macd)
        print("Signal:", result.signal)
        print("Histogram:", result.histogram)

        await dp.start_polling(
            bot,
            binance_service=binance_service
        )


if __name__ == "__main__":
    asyncio.run(main())