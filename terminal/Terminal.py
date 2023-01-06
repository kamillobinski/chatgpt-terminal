import sys
import time
import itertools
import threading
from colored import fg, bg, attr


class Terminal:

    SETTINGS = {
        'usernames': {
            'ai': 'ChatGPT',
            'user': 'you'
        },
        'exit_commands': [
            'exit',
            'end',
            'close',
            'stop'
        ],
        'message_colors': {
            'ai': 8,
            'user': 15
        }
    }

    def __init__(self):
        self.done = True
        pass

    def get_exit_commands(self):
        return self.SETTINGS['exit_commands']

    def wait(self):
        self.done = False

        def animate():
            for c in itertools.cycle(['⢿', '⣻', '⣽', '⣾', '⣷', '⣯', '⣟', '⡿']):
                if self.done:
                    break
                sys.stdout.write('\r{}{} {} is thinking... {}'.format(
                    fg(self.SETTINGS["message_colors"]["ai"]), c, self.SETTINGS["usernames"]["ai"], attr(0)))
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

    def stop_wait(self):
        self.done = True

    def display_response(self, message: str):
        print(
            f'\r{fg(self.SETTINGS["message_colors"]["ai"]) + self.SETTINGS["usernames"]["ai"]}: {message + attr(0)}')

    def get_user_message(self):
        return input(f'{self.SETTINGS["usernames"]["user"]}: ')
