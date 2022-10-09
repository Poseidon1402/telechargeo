from telechargeo.handlers.audioHandler import AudioHandler

class ResultDisplayer:
    """
        class for displaying data
    """
    def __init__(self, videos) -> None:
        self._videos = videos

    def displayResultOfTheSearch(self):
        """
            Output all results related to the search
        """
        for (ind, value) in enumerate(self._videos):
            
            print('{0} - {1} => {2}'.format(
                ind + 1,
                value['title'],
                value['link']
            ))
    
    def displayAllAudioAvailableFormat(self, handler: AudioHandler, videoNumber: int):
        """
            Output all audio's formats available for the download
        """
        handler.fetchingAllAudio()
        for (key, value) in handler._audios.items():
            print('{0} - format: {1}'.format(key + 1, value[1]))
    