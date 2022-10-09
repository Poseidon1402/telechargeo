import argparse
from time import sleep
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import ProgressBar

def setupArguments(argv=None):
    """
        configure the CLI parameters
    """
    parser = argparse.ArgumentParser(description="Search and download youtube video")
    parser.add_argument(
        '-A', '--author',
        type=str,
        required=True,
        help='Represents the name of the author like artists'
    )
    parser.add_argument(
        '-T', '--title',
        type=str,
        required=True,
        help="Represents the video's title"
    )
    arguments = parser.parse_args(argv)

    return arguments

def displayRequestedValue(argv=None):
    """
        Display the user input through the console
    """
    args = setupArguments(argv)
    print(f'searching for the video {args.author} - {args.title}')
    label = HTML('<ansired>Progression</ansired>: ')
    with ProgressBar() as pb:
        for i in pb(range(100), label=label):
            sleep(.01)