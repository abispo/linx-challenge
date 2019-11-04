import aiohttp

from fastapi import FastAPI

from app.request import get_city_forecast


app = FastAPI()

@app.get("/city/{city}")
async def index(city):
    async with aiohttp.ClientSession() as session:
        response = await get_city_forecast(session, city)

        return response
