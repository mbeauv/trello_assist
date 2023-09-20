import requests

class TrelloError(Exception):
    def __init__(self, message="Error when interacting with Trello."):
        self.message = message
        super().__init__(self.message)


def add_item_to_checklist(key, token, checklist_id, item_name):
    base_url = "https://api.trello.com/1"
    checklist_item_url = f"{base_url}/checklists/{checklist_id}/checkItems"

    print(checklist_item_url)
    headers = {
        "Accept": "application/json"
    }

    query = {
        "key": key,
        "token": token,
        "name": item_name
    }

    response = requests.post(checklist_item_url, headers=headers, params=query)

    if response.status_code == 200:
        return response.json()
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")
    
def create_card_checklist(key, token, card_id, name):
    base_url = "https://api.trello.com/1"
    checklist_url = f"{base_url}/cards/{card_id}/checklists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        "key": key,
        "token": token,
        "name": name
    }

    response = requests.post(checklist_url, headers=headers, params=query)

    if response.status_code == 200:
        print("Checklist added successfully!")
        return response.json()
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")

def list_trello_boards(key, token, username):
    base_url = "https://api.trello.com/1/members/"
    endpoint = f"{username}/boards"

    auth = {
        'key': key,
        'token': token,
    }
    response = requests.get(base_url + endpoint, params=auth)

    if response.status_code == 200:
        boards = response.json()
        return [(board['name'], board['id']) for board in boards]
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")

def create_trello_board(key, token, board_name, board_desc=None):
    """
    Create a new Trello board.

    :param key: Your Trello API key.
    :param token: Your Trello OAuth token.
    :param board_name: Name of the board to be created.
    :param board_desc: Optional description for the board.
    :return: Board ID if successful, None otherwise.
    """
    base_url = "https://api.trello.com/1/boards/"

    payload = {
        'key': key,
        'token': token,
        'name': board_name,
        'desc': board_desc,
        'defaultLists': 'false',
    }

    response = requests.post(base_url, params=payload)

    if response.status_code == 200:
        return response.json()['id']
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")

def create_trello_list(key, token, board_id, list_name):
    """
    Create a new list on a specific Trello board.

    :param key: Your Trello API key.
    :param token: Your Trello OAuth token.
    :param board_id: ID of the board where the list will be created.
    :param list_name: Name of the list to be created.
    :return: List ID if successful, None otherwise.
    """
    base_url = f"https://api.trello.com/1/boards/{board_id}/lists"

    payload = {
        'key': key,
        'token': token,
        'name': list_name
    }

    response = requests.post(base_url, params=payload)

    if response.status_code == 200:
        list_data = response.json()
        return list_data['id']
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")

def create_trello_card(key, token, list_id, card_name, card_desc=None):
    """
    Create a new card in a specific Trello list.

    :param key: Your Trello API key.
    :param token: Your Trello OAuth token.
    :param list_id: ID of the list where the card will be created.
    :param card_name: Name of the card to be created.
    :param card_desc: Optional description for the card.
    :return: Card ID if successful, None otherwise.
    """
    base_url = "https://api.trello.com/1/cards"

    payload = {
        'key': key,
        'token': token,
        'idList': list_id,
        'name': card_name,
        'desc': card_desc
    }

    response = requests.post(base_url, params=payload)

    if response.status_code == 200:
        card_data = response.json()
        return card_data['id']
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")

def list_trello_lists(key, token, board_id):
    """
    Retrieve the lists of a specific Trello board.

    :param key: Your Trello API key.
    :param token: Your Trello OAuth token.
    :param board_id: ID of the board whose lists you want to retrieve.
    :return: A list of tuples where each tuple contains the list name and its ID.
    """
    base_url = f"https://api.trello.com/1/boards/{board_id}/lists"

    params = {
        'key': key,
        'token': token
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        lists_data = response.json()
        return [(lst['name'], lst['id']) for lst in lists_data]
    else:
        raise TrelloError(f"Error {response.status_code}: {response.text}")