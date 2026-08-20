import requests
from src.config import settings
from datetime import date, timedelta
from src.models import Forecast

def get_weather(city: str) -> dict:
    params = {"key": settings.WEATHER_KEY, "q": city, "dt": str(date.today() + timedelta(days=1))}
    try:
        response = requests.get(settings.BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Request timed out")
    data = response.json()
    if "error" in data:
        raise ValueError(f"Weather API error for '{city}': {data['error'].get('message', 'unknown error')}")
    return data

def parse_weather(city: str) -> Forecast:
    data = get_weather(city)
    day = data["forecast"]["forecastday"][0]
    location = data["location"]
    day_forecast = day["day"]
    hour = day["hour"][10] #midday
    return Forecast(
        city=location["name"],
        date=day["date"],
        max_temp=day_forecast["maxtemp_c"],
        min_temp=day_forecast["mintemp_c"],
        humidity=day_forecast["avghumidity"],
        wind_speed=day_forecast["maxwind_kph"],
        wind_direction=hour["wind_dir"],
    )