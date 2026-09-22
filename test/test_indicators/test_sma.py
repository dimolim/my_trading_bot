from datetime import datetime

import pytest

from app.market.indicators import Indicators
from app.models.Candle import Candle


def test_sma():
    candles = []

    for value in [10, 20, 30, 40, 50]:
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

    result = indicators.sma(candles, 3)
    assert result == 40

def test_sma_1():
    candles = []

    for value in [10, 20, 30, 40, 50]:
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

    result = indicators.sma(candles, 1)
    assert result == 50

def test_sma_zero():
    candles = []

    for value in [10, 20, 30, 40, 50]:
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

    with pytest.raises(ValueError):
        indicators.sma(candles, 0)

def test_sma_not_enough_candles():
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

    with pytest.raises(ValueError):
        indicators.sma(candles, 5)

def test_sma_uses_last_candles():
    candles = []
    for value in [10, 20, 30, 100, 200]:
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

    result = indicators.sma(candles, 2)
    assert result == 150