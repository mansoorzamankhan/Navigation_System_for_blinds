
from gtts import gTTS
import playsound as ps

def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    ps.playsound(filename)
speak("mansoor Zaman Khan  ")

