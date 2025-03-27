"""Protocol-related functionality for Zerion SDK."""

from typing import Dict, List

from .client import ZerionClient
from .constants import ENDPOINTS


class ZerionProtocol:
    """Client for interacting with Zerion protocol endpoints."""

    def __init__(self, client: ZerionClient):
        """Initialize the protocol client.

        Args:
            client: ZerionClient instance for making API requests
        """
        self.client = client

    async def get_protocol_info(self, protocol_id: str) -> Dict:
        """Get information about a protocol.

        Args:
            protocol_id: The protocol ID to get information for

        Returns:
            Dict containing protocol information
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["protocol_info"].format(protocol_id=protocol_id)
        )

    async def get_protocol_pools(self, protocol_id: str) -> List[Dict]:
        """Get pools for a protocol.

        Args:
            protocol_id: The protocol ID to get pools for

        Returns:
            List of protocol pools
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["protocol_pools"].format(protocol_id=protocol_id)
        )

    async def get_protocol_tokens(self, protocol_id: str) -> List[Dict]:
        """Get tokens for a protocol.

        Args:
            protocol_id: The protocol ID to get tokens for

        Returns:
            List of protocol tokens
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["protocol_tokens"].format(protocol_id=protocol_id)
        )

    async def get_protocol_stats(self, protocol_id: str) -> Dict:
        """Get statistics for a protocol.

        Args:
            protocol_id: The protocol ID to get stats for

        Returns:
            Dict containing protocol statistics
        """
        return await self.client.request(
            "GET",
            ENDPOINTS["protocol_stats"].format(protocol_id=protocol_id)
        )