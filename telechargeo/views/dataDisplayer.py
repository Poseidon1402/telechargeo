from youtubesearchpython import VideosSearch

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
    