import click
import json
import os

from .config import read_default_api_key
from .config import read_default_api_token

@click.command()
def get_config():
    """Reads and prints the API key and token from the config.json file in the ~/.trello_assist directory."""

    # Define the directory and file path
    dir_path = os.path.expanduser("~/.trello_assist")
    file_path = os.path.join(dir_path, "config.json")

    # Ensure the file exists
    if not os.path.exists(file_path):
        print("Configuration file not found!")
        return

    # Read and print the API key and token from the config.json file
    with open(file_path, 'r') as file:
        config = json.load(file)
        api_key = config.get("api_key", "API key not set")
        api_token = config.get("api_token", "API token not set")

    print(f"API Key: {api_key}")
    print(f"API Token: {api_token}")