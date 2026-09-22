from app.models.Candle import Candle
from app.models.indicators_result import IndicatorsResult
from app.models.macd_result import MACDResult

class Indicators():
    def sma(self, candles: list[Candle], period: int) -> float:

        if period < 1:
            raise ValueError("period must be >= 1")
        if len(candles) < period:
            raise ValueError(f"Недостаточно свечей: доступно {len(candles)}, требуется {period}.")

        candles = candles[-period:]
        closes = []

        for candle in candles:
            closes.append(candle.close)

        return sum(closes)/len(closes)

    def ema_series(self, candles: list[Candle], period: int) -> list[float]:
        if period < 1:
            raise ValueError("period must be >= 1")
        if len(candles) < period:
            raise ValueError(f"Недостаточно свечей: доступно {len(candles)}, требуется {period}.")

        closes = []
        for candle in candles:
            closes.append(candle.close)

        ema = sum(closes[:period])/period
        alpha = 2 / (period + 1)

        ema_values = []
        ema_values.append(ema)

        for i in range(period, len(closes)):
            ema = closes[i] * alpha + ema * (1 - alpha)
            ema_values.append(ema)
        return ema_values

    def rsi(self, candles: list[Candle], period: int) -> float:
        if period < 1:
            raise ValueError("period must be >= 1")
        if len(candles) < period + 1:
            raise ValueError(f"Недостаточно свечей: доступно {len(candles)}, требуется {period + 1}.")
        closes = []
        for candle in candles:
            closes.append(candle.close)
        changes = []
        for i in range(1, len(closes)):
            change = closes[i] - closes[i - 1]
            changes.append(change)

        gains = []
        losses = []

        for change in changes:
            if change > 0:
                gains.append(change)
                losses.append(0)
            elif change < 0:
                losses.append(abs(change))
                gains.append(0)
            else:
                gains.append(0)
                losses.append(0)
        average_gain = sum(gains[:period])/len(gains[:period])
        average_loss = sum(losses[:period])/len(losses[:period])
        if average_loss == 0:
            rsi = 100
        else:
            rs = average_gain / average_loss
            rsi = 100 - 100 / (1 + rs)

        for i in range(period, len(gains)):
            current_gain = gains[i]
            current_loss = losses[i]
            average_gain = (average_gain * (period - 1) + current_gain) / period
            average_loss = (average_loss * (period - 1) + current_loss) / period
            if average_loss == 0:
                rsi = 100
            else:
                rs = average_gain / average_loss
                rsi = 100 - 100 / (1 + rs)
        return rsi

    def macd(self, candles: list[Candle]) -> MACDResult:

        ema12 = self.ema_series(candles, period=12)
        ema26 = self.ema_series(candles, period=26)
        ema12_aligned = ema12[14:]
        macd_values = []

        for i in range(len(ema26)):
            macd = ema12_aligned[i] - ema26[i]
            macd_values.append(macd)

        if len(macd_values) < 9:
            raise ValueError("Недостаточно значений MACD для расчёта Signal.")

        signal = self.ema_from_values(macd_values, period=9)
        macd = macd_values[-1]
        histogram = macd - signal

        return MACDResult(macd=macd , signal=signal, histogram=histogram)


    def ema_from_values(self, values: list[float], period: int) -> float:
        if period < 1:
            raise ValueError("period must be >= 1")
        if len(values) < period:
            raise ValueError(f"Недостаточно значений: доступно {len(values)}, требуется {period}.")
        ema = sum(values[:period]) / period
        alpha = 2 / (period + 1)

        for i in range(period, len(values)):
            ema = values[i] * alpha + ema * (1 - alpha)

        return ema

    def calculate_all(self, candles: list[Candle],
                      sma_period: int,
                      ema_period: int,
                      rsi_period: int) -> IndicatorsResult:
        sma = self.sma(candles, period=sma_period)
        ema_values = self.ema_series(candles, period=ema_period)
        ema = ema_values[-1]
        rsi = self.rsi(candles, period=rsi_period)

        result = self.macd(candles)
        macd = result.macd
        signal = result.signal
        histogram = result.histogram
        return IndicatorsResult(sma=sma,
                                ema=ema,
                                rsi=rsi,
                                macd=macd ,
                                signal=signal,
                                histogram=histogram)

