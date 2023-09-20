import json
from jsonschema import validate, ValidationError

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    return None

def read_and_validate_json(filename, schema):
    """
    Reads the content of a file, parses it as JSON, and validates it against a given schema.

    Parameters:
    - filename (str): The name of the file to read.
    - schema (dict): The JSON schema to validate against.

    Returns:
    - dict: The parsed JSON content if valid.
    - None: If the content is not valid.
    """
    try:
        with open(filename, 'r') as file:
            content = json.load(file)
        
        validate(instance=content, schema=schema)
        return content

    except ValidationError as e:
        print(f"Validation error: {e.message}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None