from youtubesearchpython import VideosSearch

from telechargeo.handlers.audioHandler import AudioHandler

class ResultDisplayer:

    def __init__(self, videos) -> None:
        self._videos = videos

    def displayResultOfTheSearch(self):
        
        for (ind, value) in enumerate(self._videos):
            
            print('{0} - {1} => {2}'.format(
                ind + 1,
                value['title'],
                value['link']
            ))
    
    def displayAllAudioAvailableFormat(self, videoSearch: VideosSearch, videoNumber: int):

        handler = AudioHandler(videoSearch.result()['result'][videoNumber-1]['link'])
        handler.fetchingAllAudio()
        for (key, value) in handler._audios.items():
            print('{0} - format: {1}'.format(key + 1, value[1]))
    