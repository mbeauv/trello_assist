import click

from .config import read_default_api_key
from .config import read_default_api_token

from trello import create_trello_list

@click.command()
@click.option('--api-key', default=read_default_api_key(), prompt=True, help='Your Trello API key.')
@click.option('--oauth-token', default=read_default_api_token(), prompt=True, help='Your Trello OAuth token.')
@click.option('--board-id', prompt=True, help='ID of the board where the list will be created.')
@click.option('--list-name', prompt=True, help='Name of the list to be created.')
def create_list(api_key, oauth_token, board_id, list_name):
    """Create a new list on a specific Trello board."""
    list_id = create_trello_list(api_key, oauth_token, board_id, list_name)
    if list_id:
        click.echo(f"List '{list_name}' created with ID: {list_id}")
    else:
        click.echo("Failed to create list.")