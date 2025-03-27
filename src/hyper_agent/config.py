"""Configuration module for Hyper Agent."""
import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_var(key: str) -> Optional[str]:
    """Get an environment variable.

    Args:
        key: The environment variable name.

    Returns:
        Optional[str]: The environment variable value if found, None otherwise.
    """
    return os.getenv(key)

def require_env_var(key: str, service: str) -> str:
    """Get a required environment variable.

    Args:
        key: The environment variable name.
        service: The service name for better error messages.

    Returns:
        str: The environment variable value.

    Raises:
        ValueError: If the environment variable is not found.
    """
    value = get_env_var(key)
    if not value:
        raise ValueError(
            f"{service} configuration not found. Please set the {key} "
            "environment variable or add it to your .env file."
        )
    return value