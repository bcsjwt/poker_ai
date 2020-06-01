import click

from poker_ai.ai.runner import train
from poker_ai.terminal.runner import run_terminal_app


@click.group()
def cli():
    """The CLI for the poker_ai package that groups the various scripts.

    The root command will allow you to do the following. The "train" option
    builds a model and manages the search for the offline strategy. The "play"
    option allows you to play against the strategy you have trained.
    """
    pass


cli.add_command(train, name="train")
cli.add_command(run_terminal_app, name="play")
