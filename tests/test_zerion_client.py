"""Tests for the Zerion client base functionality."""
import pytest
from aiohttp import web
from hyper_agent.zerion.client import ZerionClient
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR
from hyper_agent.config import require_env_var

def test_client_initialization(zerion_api_key: str):
    """Test client initialization with API key."""
    client = ZerionClient(api_key=zerion_api_key)
    assert client.api_key == zerion_api_key
    assert client.base_url == require_env_var(API_BASE_URL_ENV_VAR, "Zerion API Base URL")

def test_client_initialization_without_api_key():
    """Test client initialization without API key raises error."""
    with pytest.raises(ValueError, match="API key is required"):
        ZerionClient()

def test_client_headers(zerion_api_key: str):
    """Test client headers are correctly set."""
    client = ZerionClient(api_key=zerion_api_key)
    assert client.headers["Authorization"] == f"Bearer {zerion_api_key}"
    assert client.headers["Accept"] == "application/json"

@pytest.mark.asyncio
async def test_client_request(aiohttp_client, zerion_api_key: str):
    """Test client makes correct API requests."""
    async def handler(request):
        assert request.headers["Authorization"] == f"Bearer {zerion_api_key}"
        assert request.headers["Accept"] == "application/json"
        return web.json_response({"status": "success"})

    app = web.Application()
    app.router.add_get("/test", handler)
    client = await aiohttp_client(app)

    zerion_client = ZerionClient(api_key=zerion_api_key)
    zerion_client.base_url = str(client.make_url(""))
    response = await zerion_client._request("GET", "/test")
    assert response == {"status": "success"}

@pytest.mark.asyncio
async def test_client_error_handling(aiohttp_client, zerion_api_key: str):
    """Test client handles API errors correctly."""
    async def handler(request):
        return web.json_response({"error": "Not found"}, status=404)

    app = web.Application()
    app.router.add_get("/test", handler)
    client = await aiohttp_client(app)

    zerion_client = ZerionClient(api_key=zerion_api_key)
    zerion_client.base_url = str(client.make_url(""))
    with pytest.raises(Exception, match="API request failed: Not found"):
        await zerion_client._request("GET", "/test")

@pytest.mark.asyncio
async def test_client_rate_limit_handling(aiohttp_client, zerion_api_key: str):
    """Test client handles rate limiting correctly."""
    async def handler(request):
        return web.Response(
            status=429,
            headers={"Retry-After": "5"},
            text="Rate limit exceeded"
        )

    app = web.Application()
    app.router.add_get("/test", handler)
    client = await aiohttp_client(app)

    zerion_client = ZerionClient(api_key=zerion_api_key)
    zerion_client.base_url = str(client.make_url(""))
    with pytest.raises(Exception, match="Rate limit exceeded. Retry after 5 seconds"):
        await zerion_client._request("GET", "/test")