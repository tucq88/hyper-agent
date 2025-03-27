"""Command-line interface for Zerion SDK."""

import asyncio
import click
from typing import Optional

from .client import ZerionClient
from .wallet import ZerionWallet
from .token import ZerionToken
from .protocol import ZerionProtocol
from .constants import require_zerion_api_key


@click.group()
def cli():
    """Zerion SDK CLI."""
    pass


@cli.group()
def wallet():
    """Wallet-related commands."""
    pass


@wallet.command()
@click.argument("address")
def info(address: str):
    """Get wallet information."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        wallet_client = ZerionWallet(client)
        info = await wallet_client.get_wallet_info(address)
        click.echo(info)

    asyncio.run(_run())


@wallet.command()
@click.argument("address")
def balances(address: str):
    """Get wallet balances."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        wallet_client = ZerionWallet(client)
        balances = await wallet_client.get_wallet_balances(address)
        click.echo(balances)

    asyncio.run(_run())


@wallet.command()
@click.argument("address")
@click.option("--limit", type=int, help="Maximum number of transactions to return")
@click.option("--cursor", help="Pagination cursor")
def transactions(address: str, limit: Optional[int], cursor: Optional[str]):
    """Get wallet transactions."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        wallet_client = ZerionWallet(client)
        transactions = await wallet_client.get_wallet_transactions(address, limit, cursor)
        click.echo(transactions)

    asyncio.run(_run())


@wallet.command()
@click.argument("address")
def protocols(address: str):
    """Get wallet protocols."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        wallet_client = ZerionWallet(client)
        protocols = await wallet_client.get_wallet_protocols(address)
        click.echo(protocols)

    asyncio.run(_run())


@wallet.command()
@click.argument("address")
def portfolio(address: str):
    """Get wallet portfolio."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        wallet_client = ZerionWallet(client)
        portfolio = await wallet_client.get_wallet_portfolio(address)
        click.echo(portfolio)

    asyncio.run(_run())


@cli.group()
def token():
    """Token-related commands."""
    pass


@token.command()
@click.argument("token_id")
def info(token_id: str):
    """Get token information."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        token_client = ZerionToken(client)
        info = await token_client.get_token_info(token_id)
        click.echo(info)

    asyncio.run(_run())


@token.command()
@click.argument("token_id")
def price(token_id: str):
    """Get token price."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        token_client = ZerionToken(client)
        price = await token_client.get_token_price(token_id)
        click.echo(price)

    asyncio.run(_run())


@token.command()
@click.argument("token_id")
def holders(token_id: str):
    """Get token holders."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        token_client = ZerionToken(client)
        holders = await token_client.get_token_holders(token_id)
        click.echo(holders)

    asyncio.run(_run())


@token.command()
@click.argument("token_id")
def transactions(token_id: str):
    """Get token transactions."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        token_client = ZerionToken(client)
        transactions = await token_client.get_token_transactions(token_id)
        click.echo(transactions)

    asyncio.run(_run())


@cli.group()
def protocol():
    """Protocol-related commands."""
    pass


@protocol.command()
@click.argument("protocol_id")
def info(protocol_id: str):
    """Get protocol information."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        protocol_client = ZerionProtocol(client)
        info = await protocol_client.get_protocol_info(protocol_id)
        click.echo(info)

    asyncio.run(_run())


@protocol.command()
@click.argument("protocol_id")
def pools(protocol_id: str):
    """Get protocol pools."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        protocol_client = ZerionProtocol(client)
        pools = await protocol_client.get_protocol_pools(protocol_id)
        click.echo(pools)

    asyncio.run(_run())


@protocol.command()
@click.argument("protocol_id")
def tokens(protocol_id: str):
    """Get protocol tokens."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        protocol_client = ZerionProtocol(client)
        tokens = await protocol_client.get_protocol_tokens(protocol_id)
        click.echo(tokens)

    asyncio.run(_run())


@protocol.command()
@click.argument("protocol_id")
def stats(protocol_id: str):
    """Get protocol statistics."""
    async def _run():
        client = ZerionClient(api_key=require_zerion_api_key())
        protocol_client = ZerionProtocol(client)
        stats = await protocol_client.get_protocol_stats(protocol_id)
        click.echo(stats)

    asyncio.run(_run())


if __name__ == "__main__":
    cli()