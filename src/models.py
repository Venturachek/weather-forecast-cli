from dataclasses import dataclass
from datetime import date
@dataclass
class Forecast:
    date: date
    city: str
    max_temp: float
    min_temp: float
    humidity: int
    wind_speed: float
    wind_direction: str