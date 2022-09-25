from youtubesearchpython import VideosSearch
from telechargeo.models.video import Video

if __name__ == "__main__":
    artist = input("Ny anaran'ilay artiste: ")
    title = input("Ny titre an'ilay hira: ")
    video = Video(artist, title)

    videosSearch = VideosSearch(video.getFullDescription(), limit = 5)

    print(videosSearch.result()['result'][0]['title'])
    print(videosSearch.result()['result'][0]['link'])