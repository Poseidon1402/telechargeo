from youtubesearchpython import VideosSearch

from telechargeo.handlers.audioHandler import AudioHandler
from telechargeo.inputHandler import displayRequestedValue, setupArguments
from telechargeo.models.video import Video
from telechargeo.views.resultDisplayer import ResultDisplayer

def main(argv=None):
    args = setupArguments()
    displayRequestedValue()

    video = Video(args.author, args.title)

    videosSearch = VideosSearch(video.getFullDescription(), limit = 5)
    resultDisplayer = ResultDisplayer(videosSearch.result()['result'])
    resultDisplayer.displayResultOfTheSearch()
    
    choosed = int(input('Which will you choose ? '))
    handler = AudioHandler(videosSearch.result()['result'][choosed-1]['link'])
    resultDisplayer.displayAllAudioAvailableFormat(handler, choosed)
    
    choose = int(input('You choose: '))
    handler.downloadTheChoosedAudio(choose)


if __name__ == "__main__":
    main()