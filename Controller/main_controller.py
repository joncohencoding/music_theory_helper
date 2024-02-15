from Services.music_service import build_chord, build_hist, add_chords_to_hist
from Models.Chord import Chord
from Services.chatgpt import test_response, find_key
from View.terminal_view import view_chords_and_notes, view_note_hist, view_simple_chord_list
from Controller.controller_helper import accept_new_chords, examine_chords


class MainController:
    def __init__(self):
        self.chord_list: list[Chord] = []
        self.note_hist: dict[str, int] = {}
        self.new_chord_list: list[Chord] = []

    def run(self) -> None:
        print("Welcome to the music theory helper")
        # TODO: Switch to switch Case
        while True:
            user_input = input("Choose one of the following:\n"
                               "1. add : To start adding chords to examine\n"
                               "2. Remove: To remove chords you have added\n"
                               "3. View: To view current chord list\n"
                               "4. Examine: To examine and compare notes in your chord list\n"
                               "5. ChatGPT: To use ChatGPT capabilities\n"
                               "6: Clear: To clear chord_list\n\n")
            if user_input.lower() == 'exit':
                break

            elif user_input == 'test':
                test_response()

            elif user_input.lower() in ('1', 'add'):
                accept_new_chords(self)

            elif user_input.lower() in ('2', 'remove'):
                # add remove function
                print("Remove not yet implemented")

            elif user_input.lower() in ('3', 'View'):
                view_simple_chord_list(self.chord_list)
                input("Press enter to return to menu")

            elif user_input.lower() in ('4', 'examine'):
                examine_chords(self)

            elif user_input.lower() in ('5', 'chatgpt'):
                find_key(self.chord_list)

            elif user_input.lower() in ('6', 'clear'):
                self.chord_list.clear()
                self.note_hist.clear()


            else:
                print("Invalid input")

            print()


