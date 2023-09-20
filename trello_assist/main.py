# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import click

from commands.list_boards import list_boards
from commands.create_board import create_board
from commands.create_list import create_list
from commands.create_card import create_card
from commands.list_lists import list_lists
from commands.set_config import set_config
from commands.get_config import get_config
from commands.create_sprint import create_sprint

@click.group()
def cli():
    """Trello Assist CLI"""
    pass

cli.add_command(list_boards)
cli.add_command(create_board)
cli.add_command(create_list)
cli.add_command(create_card)
cli.add_command(list_lists)
cli.add_command(set_config)
cli.add_command(get_config)
cli.add_command(create_sprint)

if __name__ == "__main__":
    cli()
