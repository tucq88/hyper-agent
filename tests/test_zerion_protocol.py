"""Tests for the Zerion protocol functionality."""
import pytest
from unittest.mock import patch

from hyper_agent.zerion.protocol import ZerionProtocol
from hyper_agent.zerion.client import ZerionClient
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR
from hyper_agent.config import require_env_var


@pytest.fixture
def protocol_client(zerion_api_key):
    """Create a ZerionProtocol instance."""
    client = ZerionClient(api_key=zerion_api_key)
    return ZerionProtocol(client)


@pytest.fixture
def mock_protocol_info():
    """Mock response for protocol info."""
    return {
        "data": {
            "type": "protocol",
            "id": "uniswap-v3",
            "attributes": {
                "name": "Uniswap V3",
                "description": "Decentralized exchange protocol",
                "tvl": "1000000000",
                "chain": "ethereum"
            }
        }
    }


@pytest.fixture
def mock_protocol_pools():
    """Mock response for protocol pools."""
    return {
        "data": [
            {
                "type": "pool",
                "id": "0x123...",
                "attributes": {
                    "name": "ETH/USDC",
                    "tvl": "1000000",
                    "volume_24h": "500000",
                    "fee": "0.003"
                }
            }
        ]
    }


@pytest.fixture
def mock_protocol_tokens():
    """Mock response for protocol tokens."""
    return {
        "data": [
            {
                "type": "token",
                "id": "0x123...",
                "attributes": {
                    "name": "ETH",
                    "symbol": "ETH",
                    "price": "3000.00",
                    "volume_24h": "1000000"
                }
            }
        ]
    }


@pytest.fixture
def mock_protocol_stats():
    """Mock response for protocol stats."""
    return {
        "data": {
            "type": "stats",
            "attributes": {
                "tvl": "1000000000",
                "volume_24h": "50000000",
                "fees_24h": "150000",
                "users_24h": 1000
            }
        }
    }


@pytest.mark.asyncio
async def test_get_protocol_info(protocol_client, mock_protocol_info):
    """Test getting protocol information."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_protocol_info
        mock_request.return_value.__aenter__.return_value.status = 200

        protocol_info = await protocol_client.get_protocol_info("uniswap-v3")
        assert protocol_info["data"]["type"] == "protocol"
        assert protocol_info["data"]["attributes"]["name"] == "Uniswap V3"
        assert protocol_info["data"]["attributes"]["tvl"] == "1000000000"


@pytest.mark.asyncio
async def test_get_protocol_pools(protocol_client, mock_protocol_pools):
    """Test getting protocol pools."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_protocol_pools
        mock_request.return_value.__aenter__.return_value.status = 200

        pools = await protocol_client.get_protocol_pools("uniswap-v3")
        assert len(pools["data"]) == 1
        assert pools["data"][0]["type"] == "pool"
        assert pools["data"][0]["attributes"]["name"] == "ETH/USDC"
        assert pools["data"][0]["attributes"]["fee"] == "0.003"


@pytest.mark.asyncio
async def test_get_protocol_tokens(protocol_client, mock_protocol_tokens):
    """Test getting protocol tokens."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_protocol_tokens
        mock_request.return_value.__aenter__.return_value.status = 200

        tokens = await protocol_client.get_protocol_tokens("uniswap-v3")
        assert len(tokens["data"]) == 1
        assert tokens["data"][0]["type"] == "token"
        assert tokens["data"][0]["attributes"]["symbol"] == "ETH"
        assert tokens["data"][0]["attributes"]["price"] == "3000.00"


@pytest.mark.asyncio
async def test_get_protocol_stats(protocol_client, mock_protocol_stats):
    """Test getting protocol statistics."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_protocol_stats
        mock_request.return_value.__aenter__.return_value.status = 200

        stats = await protocol_client.get_protocol_stats("uniswap-v3")
        assert stats["data"]["type"] == "stats"
        assert stats["data"]["attributes"]["tvl"] == "1000000000"
        assert stats["data"]["attributes"]["volume_24h"] == "50000000"
        assert stats["data"]["attributes"]["fees_24h"] == "150000"
        assert stats["data"]["attributes"]["users_24h"] == 1000