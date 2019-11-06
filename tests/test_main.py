import nest_asyncio
import pytest
import sqlalchemy

from asynctest import patch
from starlette.testclient import TestClient

from app.base import database, metadata
from app.main import app
from app.models import APIResponse
from app.schemas import APIResponseSchema
from tests.fixtures import getcity_content

client = TestClient(app)

@pytest.fixture(autouse=True, scope="module")
def create_test_database():
    nest_asyncio.apply()

    engine = sqlalchemy.create_engine(str(database.url))
    metadata.create_all(engine)

    yield

    engine = sqlalchemy.create_engine(str(database.url))
    metadata.drop_all(engine)

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_post_city(mock_get):
    mock_get.return_value.__aenter__.return_value.json = getcity_content()
    
    response = client.post("/city/London")
    api_response = await APIResponse.objects.all()
    api_response_schema = APIResponseSchema.from_orm(api_response[0])
    
    assert response.status_code == 200
    assert api_response_schema.dict() == response.json()


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_get_city(mock_get):
    mock_get.return_value.__aenter__.return_value.json = getcity_content()
    
    client.post("/city/London")
    response = client.get("/city/London")
    api_response = await APIResponse.objects.get(id=1)
    api_response_schema = APIResponseSchema.from_orm(api_response)
    
    assert response.status_code == 200
    assert api_response_schema.dict() == response.json()[0]
