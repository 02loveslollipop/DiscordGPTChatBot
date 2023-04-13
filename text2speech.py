import google.cloud.texttospeech as tts
from gtts import gTTS as g_tts

class GoogleCloudTTS:
    
    def __init__(self,model: str):
        self.model = model
        language_code = "-".join(self.model.split("-")[:2])
        self.voice_params = tts.VoiceSelectionParams(language_code=language_code, name=self.model)
        self.audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.OGG_OPUS)

        
    def synth(self,message: str):
        text_input = tts.SynthesisInput(text=message)
        client = tts.TextToSpeechClient()
        response = client.synthesize_speech(
            input=text_input,
            voice=self.voice_params,
            audio_config=self.audio_config,
        )
        return response.audio_content
        filename = "tts.wav"
        with open(filename, "wb") as out:
            out.write(response.audio_content)

class Gtts:
    
    def __init__(self,language: str,tld: str):
        self.language = language
        self.tld = tld
        
    def synth(self,message: str):
        response = g_tts(text=message,lang=self.language,tld=self.tld)
        return response.stream()
        sound.save("tts.wav")
        
        