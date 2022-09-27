from pytube import YouTube

class AudioHandler:

    def __init__(self, url) -> None:
        self._url = url
        self._streams = YouTube(self._url).streams.filter(only_audio=True)
        self._audios = {}

    def fetchingAllAudio(self) -> None:
        for (i, val) in enumerate(self._streams):
            self._audios[i] = [val.itag, val.mime_type]
    
    def displayAllFetchedAudio(self) -> None:
        self.fetchingAllAudio()
        for (key, value) in self._audios.items():
            print('{0} - format: {1}'.format(key + 1, value[1]))
    
    def downloadingTheChoosedAudio(self, choosed: int) -> None:
        stream = self._streams.get_by_itag(self._audios[choosed-1][0])
        stream.download()
    
    def getAudiosFormat(self):
        return [value[1] for value in self._audios.values()]