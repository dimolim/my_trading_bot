from app.market.indicators import Indicators
from app.models.indicators_result import IndicatorsResult
from app.models.signal import Signal
from app.models.strategy_config import StrategyConfig


class Strategy:
    def __init__(self, config: StrategyConfig):
        self.strategy_config = config

    def analyze(self, indicators: IndicatorsResult) -> Signal:
        if (indicators.ema > indicators.sma
            and indicators.macd > indicators.signal
            and indicators.rsi >= self.strategy_config.rsi_min_buy
            and indicators.rsi <= self.strategy_config.rsi_max_buy):
            return Signal.BUY
        elif (indicators.ema < indicators.sma
            and indicators.macd < indicators.signal
            and indicators.rsi >= self.strategy_config.rsi_min_sell
            and indicators.rsi <= self.strategy_config.rsi_max_sell):
            return Signal.SELL
        else:
            return Signal.HOLD

