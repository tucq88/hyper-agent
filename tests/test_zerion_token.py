"""Tests for the Zerion token functionality."""
import pytest
import responses
from hyper_agent.zerion.client import ZerionClient
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR
from hyper_agent.config import require_env_var

@pytest.mark.asyncio
async def test_get_token_info(mock_responses: responses.RequestsMock, zerion_api_key: str, sample_token_address: str):
    """Test getting token information."""
    client = ZerionClient(api_key=zerion_api_key)

    # Mock token info response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/tokens/{sample_token_address}",
        json={
            "data": {
                "type": "token",
                "id": sample_token_address,
                "attributes": {
                    "name": "Wrapped Bitcoin",
                    "symbol": "WBTC",
                    "decimals": 8,
                    "total_supply": "100000000000000"
                }
            }
        },
        status=200
    )

    token_info = await client.get_token_info(sample_token_address)
    assert token_info["type"] == "token"
    assert token_info["attributes"]["symbol"] == "WBTC"
    assert token_info["attributes"]["decimals"] == 8

@pytest.mark.asyncio
async def test_get_token_price(mock_responses: responses.RequestsMock, zerion_api_key: str, sample_token_address: str):
    """Test getting token price."""
    client = ZerionClient(api_key=zerion_api_key)

    # Mock token price response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/tokens/{sample_token_address}/price",
        json={
            "data": {
                "type": "price",
                "attributes": {
                    "price": "50000.00",
                    "currency": "USD",
                    "change_24h": "2.5"
                }
            }
        },
        status=200
    )

    price_info = await client.get_token_price(sample_token_address)
    assert price_info["type"] == "price"
    assert price_info["attributes"]["price"] == "50000.00"
    assert price_info["attributes"]["change_24h"] == "2.5"

@pytest.mark.asyncio
async def test_get_token_holders(mock_responses: responses.RequestsMock, zerion_api_key: str, sample_token_address: str):
    """Test getting token holders."""
    client = ZerionClient(api_key=zerion_api_key)

    # Mock token holders response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/tokens/{sample_token_address}/holders",
        json={
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
        },
        status=200
    )

    holders = await client.get_token_holders(sample_token_address)
    assert len(holders) == 1
    assert holders[0]["type"] == "holder"
    assert holders[0]["attributes"]["balance"] == "100.5"

@pytest.mark.asyncio
async def test_get_token_transactions(mock_responses: responses.RequestsMock, zerion_api_key: str, sample_token_address: str):
    """Test getting token transactions."""
    client = ZerionClient(api_key=zerion_api_key)

    # Mock token transactions response
    mock_responses.add(
        responses.GET,
        f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/tokens/{sample_token_address}/transactions",
        json={
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
        },
        status=200
    )

    transactions = await client.get_token_transactions(sample_token_address)
    assert len(transactions) == 1
    assert transactions[0]["type"] == "transaction"
    assert transactions[0]["attributes"]["value"] == "10.5"