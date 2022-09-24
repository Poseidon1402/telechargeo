class Video :

    def __init__(self, artist, title) -> None:
        self._artist = artist
        self._title = title
    
    def getFullDescription(self) -> str:

        return self._artist + ' - ' + self._title
    