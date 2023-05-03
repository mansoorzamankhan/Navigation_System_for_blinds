import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
item="Hello, What's going on"
engine.setProperty('rate', 150)


def speak(str):
    engine.say(str)
    engine.runAndWait()

speak(item)