from youtubesearchpython import VideosSearch
from telechargeo.handlers.audioHandler import AudioHandler
from telechargeo.models.video import Video

if __name__ == "__main__":
    artist = input("Ny anaran'ilay artiste: ")
    title = input("Ny titre an'ilay hira: ")
    video = Video(artist, title)

    videosSearch = VideosSearch(video.getFullDescription(), limit = 5)
    handler = AudioHandler(videosSearch.result()['result'][0]['link'])
    handler.displayAllFetchedAudio()
    choose = int(input('You choose: '))
    handler.downloadingTheChoosedAudio(choose)
    print('Video file downloaded successfully')