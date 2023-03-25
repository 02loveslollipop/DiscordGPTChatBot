from google.cloud import speech
from audioStream import AudioStream as st

class Speech2text:
    def __init__(self):
        config = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,sample_rate_hertz=16000,language_code="en-US",)
        audio = speech.RecognitionAudio('synthesis.ogg',)
        
    def speechToText(config: speech.RecognitionConfig,audio: speech.RecognitionAudio,) -> speech.RecognizeResponse:
        client = speech.SpeechClient()
        # Synchronous speech recognition request
        response = client.recognize(config=config, audio=audio)
        return response
    
audio = st('synthesis.ogg')