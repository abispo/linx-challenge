
import json
import os

import aiohttp
import asynctest
import pytest

from app.request import get_city_forecast
from asynctest import CoroutineMock, patch
from tests.fixtures import getcity_content


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_get_city_data(mock_get):
    mock_get.return_value.__aenter__.return_value.json = getcity_content()

    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "fixtures/london.json"), "r") as f:
        data = json.load(f)

    async with aiohttp.ClientSession() as session:
        retorno = await get_city_forecast(session, 'London')

        assert retorno == data
