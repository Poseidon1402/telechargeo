class Video :
    """
        Represents video search object
    """
    def __init__(self, artist: str, title: str) -> None:
        self._artist = artist
        self._title = title
    
    def getFullDescription(self) -> str:
        """
            Obtain the full description of videos searches
        """
        return '{0} - {1}'.format(self._artist, self._title)