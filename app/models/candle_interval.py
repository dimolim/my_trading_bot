from enum import Enum

class CandleInterval(str, Enum):
    MINUTE_1 = "1m"
    MINUTE_5 = "5m"
    MINUTE_15 = "15m"
    HOUR_1 = "1h"
    MINUTE_30 = "30m"
    DAY_1 = "1d"