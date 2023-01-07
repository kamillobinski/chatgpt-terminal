import pyttsx3


class Pyttsx3Voice:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 178)

    def get_voices(self):
        return [{'name': voice.name} for voice in self.voices]

    def speak(self, message: str):
        self.engine.say(message)
        self.engine.runAndWait()
