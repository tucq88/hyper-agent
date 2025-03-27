"""Mock responses for Zerion API tests."""
from typing import Any, Dict

def get_wallet_assets_response(address: str) -> Dict[str, Any]:
    """Get mock wallet assets response."""
    return {
        "data": [
            {
                "type": "asset",
                "id": "ethereum",
                "attributes": {
                    "name": "Ethereum",
                    "symbol": "ETH",
                    "balance": "1.23456789",
                    "value": "2345.67"
                }
            }
        ]
    }

def get_wallet_transactions_response(address: str) -> Dict[str, Any]:
    """Get mock wallet transactions response."""
    return {
        "data": [
            {
                "type": "transaction",
                "id": "0x123...",
                "attributes": {
                    "timestamp": "2024-03-26T12:00:00Z",
                    "type": "transfer",
                    "value": "0.1",
                    "currency": "ETH"
                }
            }
        ]
    }

def get_wallet_nfts_response(address: str) -> Dict[str, Any]:
    """Get mock wallet NFTs response."""
    return {
        "data": [
            {
                "type": "nft",
                "id": "0x123...",
                "attributes": {
                    "name": "Test NFT",
                    "collection": "Test Collection",
                    "token_id": "1"
                }
            }
        ]
    }

def get_wallet_portfolio_response(address: str) -> Dict[str, Any]:
    """Get mock wallet portfolio response."""
    return {
        "data": {
            "type": "portfolio",
            "attributes": {
                "total_value": "5000.00",
                "currency": "USD",
                "change_24h": "5.2"
            }
        }
    }

def get_token_info_response(address: str) -> Dict[str, Any]:
    """Get mock token info response."""
    return {
        "data": {
            "type": "token",
            "id": address,
            "attributes": {
                "name": "Wrapped Bitcoin",
                "symbol": "WBTC",
                "decimals": 8,
                "total_supply": "100000000000000"
            }
        }
    }

def get_token_price_response(address: str) -> Dict[str, Any]:
    """Get mock token price response."""
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

def get_token_holders_response(address: str) -> Dict[str, Any]:
    """Get mock token holders response."""
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

def get_token_transactions_response(address: str) -> Dict[str, Any]:
    """Get mock token transactions response."""
    return {
        "data": [
            {
                "type": "transaction",
                "id": "0x123...",
                "attributes": {
                    "timestamp": "2024-03-26T12:00:00Z",
                    "type": "transfer",
                    "amount": "1.5",
                    "from": "0x456...",
                    "to": "0x789..."
                }
            }
        ]
    }

def get_protocol_info_response(protocol_id: str) -> Dict[str, Any]:
    """Get mock protocol info response."""
    return {
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
    }

def get_protocol_pools_response(protocol_id: str) -> Dict[str, Any]:
    """Get mock protocol pools response."""
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

def get_protocol_tokens_response(protocol_id: str) -> Dict[str, Any]:
    """Get mock protocol tokens response."""
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

def get_protocol_stats_response(protocol_id: str) -> Dict[str, Any]:
    """Get mock protocol stats response."""
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