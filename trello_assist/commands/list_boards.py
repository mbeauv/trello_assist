import click

from .config import read_default_api_key
from .config import read_default_api_token

from trello import list_trello_boards

@click.command()
@click.option('--api-key', default=read_default_api_key(), prompt=True, help='Your Trello API key.')
@click.option('--oauth-token', default=read_default_api_token(), prompt=True, help='Your Trello OAuth token.')
@click.option('--username', default='me', help='Trello username. Defaults to "me" (the authenticated user).')
def list_boards(api_key, oauth_token, username):
    """List all Trello boards for a given user."""
    boards = list_trello_boards(api_key, oauth_token, username)
    if boards:
        for name, board_id in boards:
            click.echo(f"Board Name: {name}, Board ID: {board_id}")