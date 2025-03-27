"""Tests for Zerion wallet functionality."""
import pytest
from unittest.mock import patch

from hyper_agent.zerion.wallet import ZerionWallet
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

def test_get_wallet_info(zerion_api_key, mock_wallet_response):
    """Test getting wallet info."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_wallet_response
        mock_get.return_value.status_code = 200

        wallet = ZerionWallet(zerion_api_key)
        info = wallet.get_wallet_info("0x123")

        assert info["address"] == "0x123"
        assert info["name"] == "Test Wallet"
        mock_get.assert_called_once_with(
            f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/wallets/0x123",
            headers={"Accept": "application/json", "Authorization": f"Bearer {zerion_api_key}"}
        )

def test_get_wallet_assets(zerion_api_key, mock_assets_response):
    """Test getting wallet assets."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_assets_response
        mock_get.return_value.status_code = 200

        wallet = ZerionWallet(zerion_api_key)
        assets = wallet.get_wallet_assets("0x123")

        assert len(assets) == 1
        assert assets[0]["name"] == "Test Token"
        assert assets[0]["symbol"] == "TEST"
        mock_get.assert_called_once_with(
            f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/wallets/0x123/assets",
            headers={"Accept": "application/json", "Authorization": f"Bearer {zerion_api_key}"}
        )

def test_get_wallet_transactions(zerion_api_key, mock_transactions_response):
    """Test getting wallet transactions."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_transactions_response
        mock_get.return_value.status_code = 200

        wallet = ZerionWallet(zerion_api_key)
        transactions = wallet.get_wallet_transactions("0x123")

        assert len(transactions) == 1
        assert transactions[0]["hash"] == "0xabc"
        assert transactions[0]["type"] == "transfer"
        mock_get.assert_called_once_with(
            f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/wallets/0x123/transactions",
            headers={"Accept": "application/json", "Authorization": f"Bearer {zerion_api_key}"}
        )

def test_get_wallet_nfts(zerion_api_key, mock_nfts_response):
    """Test getting wallet NFTs."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_nfts_response
        mock_get.return_value.status_code = 200

        wallet = ZerionWallet(zerion_api_key)
        nfts = wallet.get_wallet_nfts("0x123")

        assert len(nfts) == 1
        assert nfts[0]["name"] == "Test NFT"
        assert nfts[0]["collection"] == "Test Collection"
        mock_get.assert_called_once_with(
            f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/wallets/0x123/nfts",
            headers={"Accept": "application/json", "Authorization": f"Bearer {zerion_api_key}"}
        )

def test_get_wallet_portfolio(zerion_api_key, mock_portfolio_response):
    """Test getting wallet portfolio."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_portfolio_response
        mock_get.return_value.status_code = 200

        wallet = ZerionWallet(zerion_api_key)
        portfolio = wallet.get_wallet_portfolio("0x123")

        assert portfolio["total_value"] == 1000.0
        assert portfolio["total_value_change_24h"] == 100.0
        assert portfolio["total_value_change_24h_percentage"] == 10.0
        assert len(portfolio["assets"]) == 1
        mock_get.assert_called_once_with(
            f"{require_env_var(API_BASE_URL_ENV_VAR, 'Zerion API Base URL')}/wallets/0x123/portfolio",
            headers={"Accept": "application/json", "Authorization": f"Bearer {zerion_api_key}"}
        )