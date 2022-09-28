from youtubesearchpython import VideosSearch
from telechargeo.handlers.audioHandler import AudioHandler
from telechargeo.models.video import Video
from telechargeo.views.resultDisplayer import ResultDisplayer

if __name__ == "__main__":
    artist = input("Ny anaran'ilay artiste: ")
    title = input("Ny titre an'ilay hira: ")
    video = Video(artist, title)

    videosSearch = VideosSearch(video.getFullDescription(), limit = 5)
    resultDisplayer = ResultDisplayer(videosSearch.result()['result'])
    resultDisplayer.displayResultOfTheSearch()
    
    choosed = int(input('Which will you choose ? '))
    resultDisplayer.displayAllAudioAvailableFormat(videosSearch, choosed)
    
    handler = AudioHandler(videosSearch.result()['result'][choosed-1]['link'])
    choose = int(input('You choose: '))
    handler.downloadingTheChoosedAudio(choose)
    print('Audio file downloaded successfully')