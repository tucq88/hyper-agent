"""Base client for Zerion API interactions."""
import aiohttp
import base64
from typing import Any, Dict, Optional

from .constants import API_BASE_URL_ENV_VAR, API_KEY_ENV_VAR, HEADERS
from ..config import require_env_var

class ZerionClient:
    """Client for interacting with the Zerion API."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Zerion client.

        Args:
            api_key: The Zerion API key. If not provided, will be loaded from environment.

        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.base_url = require_env_var(API_BASE_URL_ENV_VAR, "Zerion API Base URL")

        # Create Basic Auth header with base64 encoded API key
        auth_string = f"{self.api_key}:"
        auth_bytes = auth_string.encode('ascii')
        base64_bytes = base64.b64encode(auth_bytes)
        base64_auth = base64_bytes.decode('ascii')

        self.headers = {
            **HEADERS,
            "Authorization": f"Basic {base64_auth}"
        }

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make an API request.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data

        Returns:
            Dict[str, Any]: API response data

        Raises:
            Exception: If the API request fails
        """
        url = f"{self.base_url}{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                url,
                headers=self.headers,
                params=params,
                json=data
            ) as response:
                if response.status == 429:
                    retry_after = response.headers.get("Retry-After", "unknown")
                    raise Exception(f"Rate limit exceeded. Retry after {retry_after} seconds")

                if response.status != 200:
                    error_data = await response.json()
                    raise ValueError(f"API request failed: {error_data}")

                return await response.json()

    async def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make an API request with retries.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            data: Request body data

        Returns:
            Dict[str, Any]: API response data

        Raises:
            Exception: If the API request fails
        """
        return await self._request(method, endpoint, params, data)