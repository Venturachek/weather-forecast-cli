from src.weather import parse_weather
from tabulate import tabulate

def build_table(cities: list[str]) -> str:
    forecasts = [parse_weather(city) for city in cities]
    headers = ["City", "Min Temp (°C)", "Max Temp (°C)", "Humidity (%)", "Wind Speed (kph)", "Wind Direction"]
    rows = [
        [
        f.city,
        f.min_temp,
        f.max_temp,
        f.humidity,
        f.wind_speed,
        f.wind_direction
        ]
        for f in forecasts
        ]
    date_ = forecasts[0].date
    table = tabulate(rows, headers=headers, tablefmt="grid")
    return f"{date_}\n\n{table}"
