from youtubesearchpython import VideosSearch

from telechargeo.handlers.audioHandler import AudioHandler
from telechargeo.inputHandler import displayRequestedValue, setupArguments
from telechargeo.models.video import Video
from telechargeo.views.resultDisplayer import ResultDisplayer

def main(argv=None):
    """
        Entry point of the command
    """
    try:

        args = setupArguments()
        displayRequestedValue()

        video = Video(args.author, args.title)

        videosSearch = VideosSearch(video.getFullDescription(), limit = 5)
        results = videosSearch.result()['result']
        resultDisplayer = ResultDisplayer(results)
        resultDisplayer.displayResultOfTheSearch()
        
        choosed = int(input('Which will you choose ? '))
        handler = AudioHandler(results[choosed-1]['link'])
        resultDisplayer.displayAllAudioAvailableFormat(handler, choosed)
        
        choose = int(input('You choose: '))
        handler.downloadTheChoosedAudio(choose)

    except KeyboardInterrupt:
        print('The program was interrupted by the user')
        

if __name__ == "__main__":
    main()