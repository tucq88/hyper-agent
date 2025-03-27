"""Wallet-related functionality for Zerion SDK."""

from typing import Dict, List, Optional

from .client import ZerionClient
from .constants import ENDPOINTS


class ZerionWallet:
    """Client for interacting with Zerion wallet endpoints."""

    def __init__(self, client: ZerionClient):
        """Initialize the wallet client.

        Args:
            client: ZerionClient instance for making API requests
        """
        self.client = client

    async def get_wallet_info(self, address: str) -> Dict:
        """Get information about a wallet.

        Args:
            address: The wallet address to get information for

        Returns:
            Dict containing wallet information
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["wallet_info"].format(address=address)
        )

    async def get_wallet_balances(self, address: str) -> List[Dict]:
        """Get token balances for a wallet.

        Args:
            address: The wallet address to get balances for

        Returns:
            List of token balances
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["wallet_balances"].format(address=address)
        )

    async def get_wallet_transactions(
        self,
        address: str,
        limit: Optional[int] = None,
        cursor: Optional[str] = None
    ) -> Dict:
        """Get transaction history for a wallet.

        Args:
            address: The wallet address to get transactions for
            limit: Maximum number of transactions to return
            cursor: Pagination cursor

        Returns:
            Dict containing transactions and pagination info
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor

        return await self.client.request(
            "GET",
            ENDPOINTS["wallet_transactions"].format(address=address),
            params=params
        )

    async def get_wallet_protocols(self, address: str) -> List[Dict]:
        """Get protocols used by a wallet.

        Args:
            address: The wallet address to get protocols for

        Returns:
            List of protocols used by the wallet
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["wallet_protocols"].format(address=address)
        )

    async def get_wallet_portfolio(self, address: str) -> Dict:
        """Get portfolio information for a wallet.

        Args:
            address: The wallet address to get portfolio for

        Returns:
            Dict containing portfolio information
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["wallet_portfolio"].format(address=address)
        )