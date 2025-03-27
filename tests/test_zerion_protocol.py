"""Tests for the Zerion protocol functionality."""
import pytest
import responses
from hyper_agent.zerion.client import ZerionClient
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR
from hyper_agent.config import require_env_var

@pytest.mark.asyncio
async def test_get_protocol_info(mock_responses: responses.RequestsMock, zerion_api_key: str):
    """Test getting protocol information."""
    client = ZerionClient(api_key=zerion_api_key)
    protocol_id = "uniswap-v3"

    # Mock protocol info response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/protocols/{protocol_id}",
        json={
            "data": {
                "type": "protocol",
                "id": protocol_id,
                "attributes": {
                    "name": "Uniswap V3",
                    "description": "Decentralized exchange protocol",
                    "tvl": "1000000000",
                    "chain": "ethereum"
                }
            }
        },
        status=200
    )

    protocol_info = await client.get_protocol_info(protocol_id)
    assert protocol_info["type"] == "protocol"
    assert protocol_info["attributes"]["name"] == "Uniswap V3"
    assert protocol_info["attributes"]["tvl"] == "1000000000"

@pytest.mark.asyncio
async def test_get_protocol_pools(mock_responses: responses.RequestsMock, zerion_api_key: str):
    """Test getting protocol pools."""
    client = ZerionClient(api_key=zerion_api_key)
    protocol_id = "uniswap-v3"

    # Mock protocol pools response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/protocols/{protocol_id}/pools",
        json={
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
        },
        status=200
    )

    pools = await client.get_protocol_pools(protocol_id)
    assert len(pools) == 1
    assert pools[0]["type"] == "pool"
    assert pools[0]["attributes"]["name"] == "ETH/USDC"
    assert pools[0]["attributes"]["fee"] == "0.003"

@pytest.mark.asyncio
async def test_get_protocol_tokens(mock_responses: responses.RequestsMock, zerion_api_key: str):
    """Test getting protocol tokens."""
    client = ZerionClient(api_key=zerion_api_key)
    protocol_id = "uniswap-v3"

    # Mock protocol tokens response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/protocols/{protocol_id}/tokens",
        json={
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
        },
        status=200
    )

    tokens = await client.get_protocol_tokens(protocol_id)
    assert len(tokens) == 1
    assert tokens[0]["type"] == "token"
    assert tokens[0]["attributes"]["symbol"] == "ETH"
    assert tokens[0]["attributes"]["price"] == "3000.00"

@pytest.mark.asyncio
async def test_get_protocol_stats(mock_responses: responses.RequestsMock, zerion_api_key: str):
    """Test getting protocol statistics."""
    client = ZerionClient(api_key=zerion_api_key)
    protocol_id = "uniswap-v3"

    # Mock protocol stats response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/protocols/{protocol_id}/stats",
        json={
            "data": {
                "type": "stats",
                "attributes": {
                    "tvl": "1000000000",
                    "volume_24h": "50000000",
                    "fees_24h": "150000",
                    "users_24h": 1000
                }
            }
        },
        status=200
    )

    stats = await client.get_protocol_stats(protocol_id)
    assert stats["type"] == "stats"
    assert stats["attributes"]["tvl"] == "1000000000"
    assert stats["attributes"]["volume_24h"] == "50000000"
    assert stats["attributes"]["fees_24h"] == "150000"
    assert stats["attributes"]["users_24h"] == 1000