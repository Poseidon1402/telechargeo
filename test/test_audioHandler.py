from telechargeo.handlers.audioHandler import AudioHandler


class TestAudioHandler:

    AUDIO_FORMAT = ['audio/mp4', 'audio/webm', 'audio/mp3']

    def test_audioFormat(self):
        audios = AudioHandler('www.youtube.com/watch?v=2Vv-BfVoq4g')
        audios.fetchingAllAudio()
        for i in audios.getAudiosFormat():
            assert i in self.AUDIO_FORMAT