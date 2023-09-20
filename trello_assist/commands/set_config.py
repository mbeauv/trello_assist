import click
import json
import os

from .config import read_default_api_key
from .config import read_default_api_token

@click.command()
@click.option('--api_key', prompt='API Key', help='Your Trello API key.')
@click.option('--api_token', prompt='API Token', help='Your Trello API token.')
def set_config(api_key, api_token):
    """Writes the provided API key and token to a config.json file in the ~/.trello_assist directory."""
    
    # Define the directory and file path
    dir_path = os.path.expanduser("~/.trello_assist")
    file_path = os.path.join(dir_path, "config.json")

    # Ensure the directory exists
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Write the API key and token to the config.json file
    with open(file_path, 'w') as file:
        json.dump({"api_key": api_key, "api_token": api_token}, file, indent=4)

    click.echo(f"Configuration saved to {file_path}")