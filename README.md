# Hyper Agent

A Python project using uv for dependency management.

## Setup

This project uses `uv` for dependency management. To get started:

1. Install `uv` if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv pip install -e .
```

## Development

- The project uses `ruff` for linting
- Python version >= 3.8 is required