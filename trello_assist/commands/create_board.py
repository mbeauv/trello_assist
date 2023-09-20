import click

from .config import read_default_api_key
from .config import read_default_api_token

from trello import create_trello_board

@click.command()
@click.option('--api-key', default=read_default_api_key(), prompt=True, help='Your Trello API key.')
@click.option('--oauth-token', default=read_default_api_token(), prompt=True, help='Your Trello OAuth token.')
@click.option('--board-name', prompt=True, help='Name of the board to be created.')
@click.option('--board-desc', default='', help='Optional description for the board.')
def create_board(api_key, oauth_token, board_name, board_desc):
    """Create a new Trello board."""
    board_id = create_trello_board(api_key, oauth_token, board_name, board_desc)
    if board_id:
        click.echo(f"Board '{board_name}' created with ID: {board_id}")
    else:
        click.echo("Failed to create board.")