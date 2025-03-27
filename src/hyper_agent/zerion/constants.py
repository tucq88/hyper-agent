"""Constants for Zerion SDK."""
from typing import Final
from ..config import require_api_key

# API Configuration
API_BASE_URL_ENV_VAR: Final[str] = "ZERION_API_BASE_URL"
API_KEY_ENV_VAR: Final[str] = "ZERION_API_KEY"
DEFAULT_API_BASE_URL: Final[str] = "https://api.zerion.io/v1"

# API Headers
HEADERS: Final[dict[str, str]] = {
    "Accept": "application/json",
}

# API Endpoints
ENDPOINTS: Final[dict] = {
    "wallet": {
        "assets": "/wallets/{address}/assets",
        "transactions": "/wallets/{address}/transactions",
        "nfts": "/wallets/{address}/nfts",
        "portfolio": "/wallets/{address}/portfolio",
    },
    "token": {
        "info": "/tokens/{address}",
        "price": "/tokens/{address}/price",
        "holders": "/tokens/{address}/holders",
        "transactions": "/tokens/{address}/transactions",
    },
    "protocol": {
        "info": "/protocols/{id}",
        "pools": "/protocols/{id}/pools",
        "tokens": "/protocols/{id}/tokens",
        "stats": "/protocols/{id}/stats",
    },
    "wallet_info": "/wallets/{address}",
    "wallet_balances": "/wallets/{address}/positions",
    "wallet_transactions": "/wallets/{address}/transactions",
    "wallet_protocols": "/wallets/{address}/protocols",
    "wallet_portfolio": "/wallets/{address}/portfolio",
    "token_info": "/tokens/{token_id}",
    "token_price": "/tokens/{token_id}/price",
    "token_holders": "/tokens/{token_id}/holders",
    "token_transactions": "/tokens/{token_id}/transactions",
    "protocol_info": "/protocols/{protocol_id}",
    "protocol_pools": "/protocols/{protocol_id}/pools",
    "protocol_tokens": "/protocols/{protocol_id}/tokens",
    "protocol_stats": "/protocols/{protocol_id}/stats"
}

def get_zerion_api_key() -> str:
    """Get Zerion API key from environment variables."""
    return require_api_key(API_KEY_ENV_VAR)

def require_zerion_api_key() -> str:
    """Get Zerion API key from environment variables or raise an error."""
    return require_api_key(API_KEY_ENV_VAR)