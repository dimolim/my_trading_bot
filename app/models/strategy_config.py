from dataclasses import dataclass


@dataclass
class StrategyConfig:
    sma_period: int
    ema_period: int
    rsi_period: int
    rsi_min_buy: float
    rsi_max_buy: float
    rsi_min_sell: float
    rsi_max_sell: float