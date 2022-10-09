from prompt_toolkit import print_formatted_text, prompt
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.completion import WordCompleter
from youtubesearchpython import VideosSearch

from telechargeo.handlers.audioHandler import AudioHandler
from telechargeo.inputHandler import displayRequestedValue, setupArguments
from telechargeo.models.video import Video
from telechargeo.validator.rangeValidator import RangeValidator
from telechargeo.helpers.resultDisplayer import ResultDisplayer

def askUserChoice(message) -> int:
    """
        Ask user about his choice
        setup autocompletion
    """
    userPossibleChoice = WordCompleter(['1', '2', '3', '4', '5'])
    choice = prompt(message, completer=userPossibleChoice,
        complete_while_typing=True, validator=RangeValidator())

    return int(choice)

def main(argv=None):
    """
        Entry point of the command
    """
    try:

        args = setupArguments()

        video = Video(args.author, args.title)

        videosSearch = VideosSearch(video.getFullDescription(), limit = 5)
        results = videosSearch.result()['result']
        displayRequestedValue()
        resultDisplayer = ResultDisplayer(results)
        resultDisplayer.displayResultOfTheSearch()
        
        choosed = askUserChoice('Which will you choose ? ')
        handler = AudioHandler(results[choosed-1]['link'])
        resultDisplayer.displayAllAudioAvailableFormat(handler, choosed)
        
        choose = askUserChoice('You choose: ')
        handler.downloadTheChoosedAudio(choose)

    except KeyboardInterrupt:
        print_formatted_text(FormattedText([('#FF0000', 'The program was interrupted by the user')]))
        

if __name__ == "__main__":
    main()