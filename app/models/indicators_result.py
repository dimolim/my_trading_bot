from dataclasses import dataclass


@dataclass
class IndicatorsResult:
    sma: float
    ema: float
    rsi: float
    macd: float
    signal: float
    histogram: float
