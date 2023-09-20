import click

from .config import read_default_api_key
from .config import read_default_api_token

from trello import list_trello_lists

@click.command()
@click.option('--api-key', default=read_default_api_key(), prompt=True, help='Your Trello API key.')
@click.option('--oauth-token', default=read_default_api_token(), prompt=True, help='Your Trello OAuth token.')
@click.option('--board-id', prompt=True, help='ID of the board whose lists you want to retrieve.')
def list_lists(api_key, oauth_token, board_id):
    """Retrieve the lists of a specific Trello board."""
    lists_info = list_trello_lists(api_key, oauth_token, board_id)
    if lists_info:
        for name, list_id in lists_info:
            click.echo(f"List Name: {name}, List ID: {list_id}")
    else:
        click.echo("Failed to retrieve lists.")