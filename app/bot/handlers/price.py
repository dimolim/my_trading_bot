from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.models.candle_interval import CandleInterval
from app.services.binance_service import BinanceService

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Бот работает!")

@router.message(Command("price"))
async def price_handler(message: Message, binance_service: BinanceService):
    price = await binance_service.get_current_price("BTCUSDT")

    await message.answer(
        f"{price.symbol}: {price.price}"
    )

@router.message(Command("candle"))
async def get_candle(message: Message, binance_service: BinanceService):


    parts = message.text.split()

    if len(parts) != 4:
        await message.answer(
            "Использование:\n"
            "/candle BTCUSDT 5m 10"
        )
        return

    symbol = parts[1]

    try:
        interval = CandleInterval(parts[2])
    except ValueError:
        await message.answer(
            "Неверный интервал.\n"
            "Доступные интервалы: 1m, 5m, 15m, 30m, 1h, 1d"
        )
        return
    try:
        limit = int(parts[3])
    except ValueError:
        await message.answer(
            "Неверный лимит. \n"
            "Количество свечей должно быть целым числом."
        )
        return

    if limit < 1 and limit > 100:
        await message.answer(
            "Количество свечей должно быть от 1 до 100."
        )
        return

    candles = await binance_service.get_candles(
        symbol,
        interval,
        limit)
    text = ""
    for candle in candles:
        text += (
            f"🕐 {candle.open_time}\n"
            f"Open: {candle.open}\n"
            f"High: {candle.high}\n"
            f"Low: {candle.low}\n"
            f"Close: {candle.close}\n"
            f"Volume: {candle.volume}\n\n"
        )

    await message.answer(text)