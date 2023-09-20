import click

from .config import read_default_api_key
from .config import read_default_api_token

from trello import create_trello_card

@click.command()
@click.option('--api-key', default=read_default_api_key(), prompt=True, help='Your Trello API key.')
@click.option('--oauth-token', default=read_default_api_token(), prompt=True, help='Your Trello OAuth token.')
@click.option('--list-id', prompt=True, help='ID of the list where the card will be created.')
@click.option('--card-name', prompt=True, help='Name of the card to be created.')
@click.option('--card-desc', default='', help='Optional description for the card.')
def create_card(api_key, oauth_token, list_id, card_name, card_desc):
    """Create a new card in a specific Trello list."""
    card_id = create_trello_card(api_key, oauth_token, list_id, card_name, card_desc)
    if card_id:
        click.echo(f"Card '{card_name}' created with ID: {card_id}")
    else:
        click.echo("Failed to create card.")