import os
import platform
from ai.OpenAI import OpenAI
from dotenv import load_dotenv
from terminal.Terminal import Terminal
from voice.GoogleVoice import GoogleVoice
from voice.Pyttsx3Voice import Pyttsx3Voice


def main():
    try:
        load_dotenv()
        ai = OpenAI()
        terminal = Terminal()

        # google_voice = GoogleVoice()
        # pyttsx3_voice = Pyttsx3Voice()

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        exit_commands = terminal.get_exit_commands()
        while True:
            message = terminal.get_user_message()
            if message in exit_commands:
                break
            terminal.wait()
            response = ai.ask(message)
            terminal.stop_wait()
            terminal.display_response(response.message_raw)
            
            # google_voice.speak(response.message, 'en')
            # pyttsx3_voice.speak(response.message)
    except OSError as e:
        pass


if __name__ == '__main__':
    main()
