"""Tests for the Zerion token functionality."""
import pytest
from unittest.mock import patch

from hyper_agent.zerion.token import ZerionToken
from hyper_agent.zerion.client import ZerionClient
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR
from hyper_agent.config import require_env_var


@pytest.fixture
def token_client(zerion_api_key):
    """Create a ZerionToken instance."""
    client = ZerionClient(api_key=zerion_api_key)
    return ZerionToken(client)


@pytest.fixture
def mock_token_info():
    """Mock response for token info."""
    return {
        "data": {
            "type": "token",
            "id": "0x123",
            "attributes": {
                "name": "Wrapped Bitcoin",
                "symbol": "WBTC",
                "decimals": 8,
                "total_supply": "100000000000000"
            }
        }
    }


@pytest.fixture
def mock_token_price():
    """Mock response for token price."""
    return {
        "data": {
            "type": "price",
            "attributes": {
                "price": "50000.00",
                "currency": "USD",
                "change_24h": "2.5"
            }
        }
    }


@pytest.fixture
def mock_token_holders():
    """Mock response for token holders."""
    return {
        "data": [
            {
                "type": "holder",
                "id": "0x123...",
                "attributes": {
                    "balance": "100.5",
                    "percentage": "0.5"
                }
            }
        ]
    }


@pytest.fixture
def mock_token_transactions():
    """Mock response for token transactions."""
    return {
        "data": [
            {
                "type": "transaction",
                "id": "0x456...",
                "attributes": {
                    "hash": "0x789...",
                    "timestamp": "2024-03-26T00:00:00Z",
                    "value": "10.5"
                }
            }
        ]
    }


@pytest.mark.asyncio
async def test_get_token_info(token_client, mock_token_info, sample_token_address):
    """Test getting token information."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_token_info
        mock_request.return_value.__aenter__.return_value.status = 200

        token_info = await token_client.get_token_info(sample_token_address)
        assert token_info["data"]["type"] == "token"
        assert token_info["data"]["attributes"]["symbol"] == "WBTC"
        assert token_info["data"]["attributes"]["decimals"] == 8


@pytest.mark.asyncio
async def test_get_token_price(token_client, mock_token_price, sample_token_address):
    """Test getting token price."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_token_price
        mock_request.return_value.__aenter__.return_value.status = 200

        price_info = await token_client.get_token_price(sample_token_address)
        assert price_info["data"]["type"] == "price"
        assert price_info["data"]["attributes"]["price"] == "50000.00"
        assert price_info["data"]["attributes"]["change_24h"] == "2.5"


@pytest.mark.asyncio
async def test_get_token_holders(token_client, mock_token_holders, sample_token_address):
    """Test getting token holders."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_token_holders
        mock_request.return_value.__aenter__.return_value.status = 200

        holders = await token_client.get_token_holders(sample_token_address)
        assert len(holders["data"]) == 1
        assert holders["data"][0]["type"] == "holder"
        assert holders["data"][0]["attributes"]["balance"] == "100.5"


@pytest.mark.asyncio
async def test_get_token_transactions(token_client, mock_token_transactions, sample_token_address):
    """Test getting token transactions."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_token_transactions
        mock_request.return_value.__aenter__.return_value.status = 200

        transactions = await token_client.get_token_transactions(sample_token_address)
        assert len(transactions["data"]) == 1
        assert transactions["data"][0]["type"] == "transaction"
        assert transactions["data"][0]["attributes"]["value"] == "10.5"