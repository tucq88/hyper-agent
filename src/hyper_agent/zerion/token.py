"""Token-related functionality for Zerion SDK."""

from typing import Dict, List

from .client import ZerionClient
from .constants import ENDPOINTS


class ZerionToken:
    """Client for interacting with Zerion token endpoints."""

    def __init__(self, client: ZerionClient):
        """Initialize the token client.

        Args:
            client: ZerionClient instance for making API requests
        """
        self.client = client

    async def get_token_info(self, token_id: str) -> Dict:
        """Get information about a token.

        Args:
            token_id: The token ID to get information for

        Returns:
            Dict containing token information
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["token_info"].format(token_id=token_id)
        )

    async def get_token_price(self, token_id: str) -> Dict:
        """Get price information for a token.

        Args:
            token_id: The token ID to get price for

        Returns:
            Dict containing token price information
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["token_price"].format(token_id=token_id)
        )

    async def get_token_holders(self, token_id: str) -> List[Dict]:
        """Get holders of a token.

        Args:
            token_id: The token ID to get holders for

        Returns:
            List of token holders
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["token_holders"].format(token_id=token_id)
        )

    async def get_token_transactions(self, token_id: str) -> List[Dict]:
        """Get transactions for a token.

        Args:
            token_id: The token ID to get transactions for

        Returns:
            List of token transactions
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["token_transactions"].format(token_id=token_id)
        )