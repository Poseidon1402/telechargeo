from youtubesearchpython import VideosSearch

artist = input("Ny anaran'ilay artiste: ")
title = input("Ny titre an'ilay hira: ")
videosSearch = VideosSearch('{0} - {1}'.format(artist, title), limit = 1)

print(videosSearch.result()['result'][0]['link'])