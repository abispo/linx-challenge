import aiohttp

from decouple import config
from typing import Dict


API_KEY = config('OPENWEATHER_API_KEY')
API_URL = config('OPENWEATHER_API_URL')


async def get_city_forecast(session: aiohttp.ClientSession, city: str) -> Dict:
    url = f"{API_URL}?q={city}&appid={API_KEY}"

    try:
        async with session.get(url) as response:
            return await response.json()

    except Exception as e:
        raise aiohttp.ClientError(str(e))
