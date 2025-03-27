"""Tests for ZerionWallet class."""

import pytest
from unittest.mock import patch

from hyper_agent.zerion.wallet import ZerionWallet
from hyper_agent.zerion.client import ZerionClient
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR, DEFAULT_API_BASE_URL
from hyper_agent.config import require_env_var

@pytest.fixture
def mock_wallet_response():
    """Mock response for wallet info."""
    return {
        "data": {
            "id": "0x123",
            "type": "wallet",
            "attributes": {
                "address": "0x123",
                "name": "Test Wallet",
                "created_at": "2024-01-01T00:00:00Z",
            }
        }
    }

@pytest.fixture
def mock_assets_response():
    """Mock response for wallet assets."""
    return {
        "data": [
            {
                "id": "1",
                "type": "asset",
                "attributes": {
                    "name": "Test Token",
                    "symbol": "TEST",
                    "balance": "1000000000000000000",
                    "price": 1.0,
                    "value": 1.0,
                }
            }
        ]
    }

@pytest.fixture
def mock_transactions_response():
    """Mock response for wallet transactions."""
    return {
        "data": [
            {
                "id": "1",
                "type": "transaction",
                "attributes": {
                    "hash": "0xabc",
                    "timestamp": "2024-01-01T00:00:00Z",
                    "value": "1000000000000000000",
                    "type": "transfer",
                }
            }
        ]
    }

@pytest.fixture
def mock_nfts_response():
    """Mock response for wallet NFTs."""
    return {
        "data": [
            {
                "id": "1",
                "type": "nft",
                "attributes": {
                    "name": "Test NFT",
                    "collection": "Test Collection",
                    "token_id": "1",
                    "image_url": "https://example.com/image.png",
                }
            }
        ]
    }

@pytest.fixture
def mock_portfolio_response():
    """Mock response for wallet portfolio."""
    return {
        "data": {
            "id": "1",
            "type": "portfolio",
            "attributes": {
                "total_value": 1000.0,
                "total_value_change_24h": 100.0,
                "total_value_change_24h_percentage": 10.0,
                "assets": [
                    {
                        "name": "Test Token",
                        "symbol": "TEST",
                        "balance": "1000000000000000000",
                        "price": 1.0,
                        "value": 1.0,
                    }
                ]
            }
        }
    }

@pytest.fixture
def mock_protocols_response():
    """Mock response for wallet protocols."""
    return {
        "data": [
            {
                "id": "1",
                "type": "protocol",
                "attributes": {
                    "name": "Test Protocol",
                    "description": "A test protocol",
                    "website": "https://example.com",
                }
            }
        ]
    }

@pytest.fixture
def wallet_client(zerion_api_key):
    """Create a ZerionWallet instance."""
    client = ZerionClient(api_key=zerion_api_key)
    return ZerionWallet(client)

@pytest.mark.asyncio
async def test_get_wallet_info(wallet_client, mock_wallet_response):
    """Test getting wallet info."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_wallet_response
        mock_request.return_value.__aenter__.return_value.status = 200

        info = await wallet_client.get_wallet_info("0x123")
        assert info["data"]["attributes"]["address"] == "0x123"

@pytest.mark.asyncio
async def test_get_wallet_balances(wallet_client, mock_assets_response):
    """Test getting wallet balances."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_assets_response
        mock_request.return_value.__aenter__.return_value.status = 200

        balances = await wallet_client.get_wallet_balances("0x123")
        assert len(balances["data"]) == 1
        assert balances["data"][0]["attributes"]["symbol"] == "TEST"

@pytest.mark.asyncio
async def test_get_wallet_transactions(wallet_client, mock_transactions_response):
    """Test getting wallet transactions."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_transactions_response
        mock_request.return_value.__aenter__.return_value.status = 200

        transactions = await wallet_client.get_wallet_transactions("0x123")
        assert len(transactions["data"]) == 1
        assert transactions["data"][0]["attributes"]["hash"] == "0xabc"

@pytest.mark.asyncio
async def test_get_wallet_protocols(wallet_client, mock_protocols_response):
    """Test getting wallet protocols."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_protocols_response
        mock_request.return_value.__aenter__.return_value.status = 200

        protocols = await wallet_client.get_wallet_protocols("0x123")
        assert len(protocols["data"]) == 1
        assert protocols["data"][0]["attributes"]["name"] == "Test Protocol"

@pytest.mark.asyncio
async def test_get_wallet_portfolio(wallet_client, mock_portfolio_response):
    """Test getting wallet portfolio."""
    with patch("aiohttp.ClientSession.request") as mock_request:
        mock_request.return_value.__aenter__.return_value.json.return_value = mock_portfolio_response
        mock_request.return_value.__aenter__.return_value.status = 200

        portfolio = await wallet_client.get_wallet_portfolio("0x123")
        assert portfolio["data"]["attributes"]["total_value"] == 1000.0
        assert portfolio["data"]["attributes"]["total_value_change_24h"] == 100.0