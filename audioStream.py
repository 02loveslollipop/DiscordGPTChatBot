import io
import soundfile as sn

class AudioStream:
    def __init__(self,audio):
        with io.open(audio, "rb") as audio_file:
            content = audio_file.read()
        self.stream = [content]
        

        
    def 
        
        