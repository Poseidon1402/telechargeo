from youtubesearchpython import VideosSearch
from telechargeo.handlers.audioHandler import AudioHandler
from telechargeo.models.video import Video
from telechargeo.views.dataDisplayer import ResultDisplayer

if __name__ == "__main__":
    artist = input("Ny anaran'ilay artiste: ")
    title = input("Ny titre an'ilay hira: ")
    video = Video(artist, title)

    videosSearch = VideosSearch(video.getFullDescription(), limit = 5)
    videoDisplayer = ResultDisplayer(videosSearch.result()['result'])
    videoDisplayer.displayResultOfTheSearch()
    
    choosed = int(input('Which will you choose ? '))
    handler = AudioHandler(videosSearch.result()['result'][choosed-1]['link'])
    handler.displayAllFetchedAudio()
    choose = int(input('You choose: '))
    handler.downloadingTheChoosedAudio(choose)
    print('Video file downloaded successfully')