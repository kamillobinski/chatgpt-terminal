import os
from gtts import gTTS
from playsound import playsound
from contextlib import contextmanager


output_file = f'voice/output.mp3'


class GoogleVoice:

    LANGUAGES = {}

    @classmethod
    def get_languages(cls):
        if not cls.LANGUAGES:
            import gtts.lang
            cls.LANGUAGES = [{'code': code, 'name': name}
                             for code, name in gtts.lang.tts_langs().items()]
        return cls.LANGUAGES

    def speak(self, message: str, language: str) -> None:
        with self.__delete_output_on_exit():
            tts = gTTS(message, lang=language)
            tts.save(output_file)
            current_dir = os.getcwd()
            playsound(current_dir + '/' + output_file)

    @contextmanager
    def __delete_output_on_exit(self):
        try:
            yield
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)
