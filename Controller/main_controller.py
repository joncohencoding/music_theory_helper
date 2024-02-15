import os

from Models.Chord import Chord
from Services.chatgpt import test_response, find_key
from View.terminal_view import view_simple_chord_list
from Controller.controller_helper import listen_new_chords, listen_remove_chords, examine_chords
import threading

from View.view import TerminalView

config_to_view = {
    "TERMINAL": TerminalView,
}

view_type = os.getenv('VIEW_TYPE', 'TERMINAL')
ViewClass = config_to_view.get(view_type)


class MainController:
    def __init__(self):
        self.chord_list: list[Chord] = []
        self.note_hist: dict[str, int] = {}
        self.new_chord_list: list[Chord] = []
        self.view = ViewClass()

    def run(self) -> None:
        print("Welcome to the music theory helper")
        # TODO: Switch to switch Case
        while True:
            user_input = self.view.get_input("Choose one of the following:\n"
                                             "1. add : To start adding chords to examine\n"
                                             "2. Remove: To remove chords you have added\n"
                                             "3. View: To view current chord list\n"
                                             "4. Examine: To examine and compare notes in your chord list\n"
                                             "5. Key: To find the key\n"
                                             "6: Clear: To clear chord_list\n\n")

            if user_input.lower() == 'exit':
                break

            elif user_input == 'test':
                test_response()

            elif user_input.lower() in ('1', 'add'):
                listen_new_chords(self)

            elif user_input.lower() in ('2', 'remove'):
                listen_remove_chords(self)

            elif user_input.lower() in ('3', 'view'):
                self.view.display_simple_chord_list(self.chord_list)
                self.view.get_input("Press enter to return to menu")

            elif user_input.lower() in ('4', 'examine'):
                examine_chords(self)

            elif user_input.lower() in ('5', 'chatgpt', 'key'):
                gpt_thread = threading.Thread(target=gpt_integration(self), daemon=True)
                gpt_thread.start()
                gpt_thread.join()  # Wait for GPT to finish before accepting more user input

            elif user_input.lower() in ('6', 'clear'):
                self.chord_list.clear()
                self.note_hist.clear()

            else:
                self.view.display_message("Invalid input")

            self.view.display_message("")


def gpt_integration(controller):
    controller.view.display_message("GPT thinking...")
    find_key(controller.chord_list)
