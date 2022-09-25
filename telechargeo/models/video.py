class Video :

    def __init__(self, artist, title) -> None:
        self._artist = artist
        self._title = title
    
    def getFullDescription(self) -> str:

        return '{0} - {1}'.format(self._artist, self._title)
    