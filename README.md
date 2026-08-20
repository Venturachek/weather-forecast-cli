# Weather Forecast CLI

Simple CLI app that fetches tomorrow's weather forecast for a list of cities using WeatherAPI.com

## Data shown per city

- Min / Max Temperature (°C)
- Humidity (%)
- Wind Speed (kph)
- Wind Direction

## Setup

```bash
git clone https://github.com/Venturachek/weather-forecast-cli.git
cd weather-forecast-cli
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```env
WEATHER_KEY=your_api_key
BASE_URL=http://api.weatherapi.com/v1/history.json
```

## Run

```bash
python -m src.main
```

## Cities

Chisinau, Madrid, Kyiv, Amsterdam — editable in `src/main.py`.

## Author

Ihor Deriabkin
