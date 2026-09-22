from datetime import datetime

import pytest

from app.market.strategy import Strategy
from app.models.strategy_config import StrategyConfig
from app.models.indicators_result import IndicatorsResult
from app.models.signal import Signal
from app.market.indicators import Indicators
from app.models.Candle import Candle


def test_buy_signal():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )

    strategy = Strategy(config)

    indicators = IndicatorsResult(
    sma=100,
    ema=105,
    rsi=60,
    macd=3,
    signal=1,
    histogram=2
)
    result = strategy.analyze(indicators)

    assert result == Signal.BUY

def test_rsi_low():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)

    indicators = IndicatorsResult(
        sma=100,
        ema=105,
        rsi=40,
        macd=3,
        signal=1,
        histogram=2
    )
    result = strategy.analyze(indicators)

    assert result == Signal.HOLD

def test_sell_signal():

    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema=100,
        rsi=40,
        macd=1,
        signal=3,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.SELL

def test_buy_rsi_min():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,)
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=100,
        ema=105,
        rsi=50,
        macd=3,
        signal=1,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.BUY

def test_buy_rsi_max():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=100,
        ema=105,
        rsi=70,
        macd=3,
        signal=1,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.BUY

def test_buy_rsi_above_max():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=100,
        ema=105,
        rsi=71,
        macd=3,
        signal=1,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

def test_sell_rsi_min():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema=100,
        rsi=30,
        macd=1,
        signal=3,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.SELL

def test_sell_rsi_max():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema=100,
        rsi=50,
        macd=1,
        signal=3,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.SELL
def test_sell_rsi_below_min():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema=100,
        rsi=29,
        macd=1,
        signal=3,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

def test_sell_rsi_above_max():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema=100,
        rsi=78,
        macd=1,
        signal=3,
        histogram=2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

def test_by_without_macd_confirmation():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=100,
        ema = 105,
        rsi = 60,
        macd = 1,
        signal = 3,
        histogram = 2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

def test_by_without_macd_confirmation_sell():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema = 100,
        rsi = 60,
        macd = 3,
        signal = 1,
        histogram = 2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

def test_by_without_ema_confirmation_buy():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=105,
        ema = 100,
        rsi = 60,
        macd = 3,
        signal = 1,
        histogram = 2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

def test_by_without_ema_confirmation_sell():
    config = StrategyConfig(
        sma_period=20,
        ema_period=9,
        rsi_period=14,
        rsi_min_buy=50.0,
        rsi_max_buy=70.0,
        rsi_min_sell=30.0,
        rsi_max_sell=50.0,
    )
    strategy = Strategy(config)
    indicators = IndicatorsResult(
        sma=100,
        ema = 101,
        rsi = 40,
        macd = 1,
        signal = 3,
        histogram = 2
    )
    result = strategy.analyze(indicators)
    assert result == Signal.HOLD

