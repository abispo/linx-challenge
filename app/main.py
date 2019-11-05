import aiohttp

import databases
import sqlalchemy

from datetime import datetime

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.base import database, metadata
from app.schemas import APIResponseSchema
from app.models import APIResponse
from app.request import get_city_forecast

app = FastAPI()

engine = sqlalchemy.create_engine(str(database.url))
metadata.create_all(engine)


@app.exception_handler(Exception)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error_message": f"{exc}"}
    )

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/city/{city}")
async def index(city: str, request: Request):
    async with aiohttp.ClientSession() as session:
        start_time = datetime.now()

        response = await get_city_forecast(session, city)

        end_time = datetime.now()

        try:
            api_response = await APIResponse.objects.create(
                timestamp_start=datetime.timestamp(start_time),
                timestamp_end=datetime.timestamp(end_time),
                ip_address=request.client.host,
                api_response=response
            )
        except Exception as e:
            raise SQLAlchemyError(str(e))

        api_response_schema = APIResponseSchema.from_orm(api_response)

        return api_response_schema
