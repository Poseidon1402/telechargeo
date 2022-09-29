from pytube import YouTube

class AudioHandler:
    """
        Prepare the audio object for the download
    """
    def __init__(self, url) -> None:
        self._streams = YouTube(url).streams.filter(only_audio=True)
        self._audios = {}

    def fetchingAllAudio(self) -> None:
        """
            Affect results to the audios dictionary
        """
        for (i, val) in enumerate(self._streams):
            self._audios[i] = [val.itag, val.mime_type]
    
    def downloadTheChoosedAudio(self, choosed: int) -> None:
        """
            Download the audio choosed by users
        """
        stream = self._streams.get_by_itag(self._audios[choosed-1][0])
        stream.download()
    
    def getAudiosFormat(self):
        return [value[1] for value in self._audios.values()]