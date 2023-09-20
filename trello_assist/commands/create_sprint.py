import click

from .config import read_default_api_key
from .config import read_default_api_token

from utils.json_parsing import (
    read_json_file,
    read_and_validate_json
)

from sprint_board_factory import SprintBoardFactory

@click.command()
@click.option('--api-key', default=read_default_api_key(), prompt=True, help='Your Trello API key.')
@click.option('--oauth-token', default=read_default_api_token(), prompt=True, help='Your Trello OAuth token.')
@click.option('--filename', default="sample_sprint.json", prompt=True, help="File containing sprint info.")
def create_sprint(api_key, oauth_token, filename):
    """Processes a user story file and creates a board for it.."""
    
    schema = read_json_file("sprint_schema.json")
    sprint_info = read_and_validate_json(filename, schema)
    if sprint_info != None:  
        result = SprintBoardFactory(api_key, oauth_token).create(sprint_info)
        if result:
            print(result)
        else:
            click.echo("Failed to create sprint.")
    else:
        print("Failed processing")
