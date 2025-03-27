"""Constants for Zerion SDK."""
from typing import Final

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
}