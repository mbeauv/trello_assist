import os
import json

# Name of the directory where config is stored.
_config_dir = "~/.trello_assist"

# Name of the configuration file.
_config_file = "config.json"

def read_default_api_key():
     # Define the directory and file path
    dir_path = os.path.expanduser(_config_dir)
    file_path = os.path.join(dir_path, _config_file)

    # Ensure the file exists
    if not os.path.exists(file_path):
        return None

    # Read and return the API key and token from the config.json file
    with open(file_path, 'r') as file:
        config = json.load(file)
        if config:
            return config.get("api_key", "API key not set")
        else:
            return None
    
def read_default_api_token():
     # Define the directory and file path
    dir_path = os.path.expanduser(_config_dir)
    file_path = os.path.join(dir_path, _config_file)

    # Ensure the file exists
    if not os.path.exists(file_path):
        return None

    # Read and return the API key and token from the config.json file
    with open(file_path, 'r') as file:
        config = json.load(file)
        if config:
            return config.get("api_token", "API token not set")
        else:
            return None
