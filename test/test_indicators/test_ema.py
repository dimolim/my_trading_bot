from datetime import datetime

from app.market.indicators import Indicators
from app.models.Candle import Candle

def test_ema():
    candles = []
    for value in [10, 20, 30]:
        candle = Candle(
            open_time=datetime(2020, 1, 1),
            open=1,
            high=5,
            low=3,
            close=value,
            volume=10
        )
        candles.append(candle)
    indicators = Indicators()

    result = indicators.ema_series(candles, 3)
    assert result == [20]

def test_ema_four_candles():
    candles = []
    for value in [10, 20, 30,40]:
        candle = Candle(
            open_time=datetime(2020, 1, 1),
            open=1,
            high=5,
            low=3,
            close=value,
            volume=10
        )
        candles.append(candle)
    indicators = Indicators()

    result = indicators.ema_series(candles, 3)
    assert result == [20,30]