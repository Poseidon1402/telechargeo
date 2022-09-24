from models.Video import Video

class TestVideo:
    
    def test_fullDescription_method(self):
        video = Video("Ed Sheeran", "Perfect")
        assert video.getFullDescription() == "Ed Sheeran - Perfect"