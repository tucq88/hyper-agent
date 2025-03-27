"""Test configuration and fixtures."""
import pytest
import responses
from hyper_agent.zerion.constants import API_BASE_URL_ENV_VAR, API_KEY_ENV_VAR
from hyper_agent.config import require_env_var

@pytest.fixture
def mock_responses():
    """Fixture for mocking HTTP responses."""
    with responses.RequestsMock() as rsps:
        yield rsps

@pytest.fixture
def zerion_api_key():
    """Get the Zerion API key from environment variables."""
    return require_env_var(API_KEY_ENV_VAR, "Zerion API")

@pytest.fixture
def sample_wallet_address():
    """Get a sample wallet address for testing."""
    return "0x1234567890123456789012345678901234567890"

@pytest.fixture
def sample_token_address():
    """Get a sample token address for testing."""
    return "0xabcdef1234567890abcdef1234567890abcdef12"

@pytest.fixture
def sample_protocol_id():
    """Get a sample protocol ID for testing."""
    return "uniswap-v3"