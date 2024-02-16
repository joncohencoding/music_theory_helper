import os

from Models.chord import Chord
from Models.model import NonDBModel
from Services.chatgpt import test_response, find_key
import threading

from View.view import TerminalView

config_to_view = {
    "TERMINAL": TerminalView,
}

config_to_model = {
    "NONDBMODEL": NonDBModel
}

view_type = os.getenv('VIEW_TYPE', 'TERMINAL')
ViewClass = config_to_view.get(view_type)

model_type = os.getenv('MODEL_TYPE', 'NONDBMODEL')
ModelClass = config_to_model.get(model_type)

class MainController:
    def __init__(self):
        self.model = ModelClass()
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
                                             "6: Clear: To clear chord list\n\n")

            self.handle_input(user_input)

    def handle_input(self, user_input):
        if user_input.lower() == 'exit':
            return

        elif user_input == 'test':
            test_response()

        elif user_input.lower() in ('1', 'add'):
            self.listen_new_chords()

        elif user_input.lower() in ('2', 'remove'):
            self.listen_remove_chords()

        elif user_input.lower() in ('3', 'view'):
            self.view.display_simple_chord_list(self.model.chord_list)
            self.view.get_input("Press enter to return to menu")

        elif user_input.lower() in ('4', 'examine'):
            self.examine_chords()

        elif user_input.lower() in ('5', 'chatgpt', 'key'):
            gpt_thread = threading.Thread(target=self.gpt_integration(), daemon=True)
            gpt_thread.start()
            gpt_thread.join()  # Wait for GPT to finish before accepting more user input

        elif user_input.lower() in ('6', 'clear'):
            self.model.clear_data()

        else:
            self.view.display_message("Invalid input")

        self.view.display_message("")

    def listen_new_chords(self) -> None:
        while True:
            user_input = self.view.get_input("Input a chord to enter or q to quit: ")

            if user_input.lower() in ("q", "", "quit"):
                break

            try:
                repeat: bool = False
                # Check for repeats
                for chord in self.model.chord_list:
                    if user_input == chord.chord_name:
                        repeat = True
                        self.view.display_message("Chord already added")
                if not repeat:
                    new_chord: Chord = self.model.build_chord_object(user_input)
                    # Left off here, invalid input for chord  name
                    self.model.chord_list.append(new_chord)  # make this a method
                    self.model.add_chord_to_hist(new_chord)
            except Exception as e:
                self.view.display_message(f"Exception occurred: {e}")
        return

    # TODO Save chords always in the same case format
    def listen_remove_chords(self) -> None:
        while True:
            self.view.display_simple_chord_list(self.model.chord_list)
            user_input = self.view.get_input(
                "Input a chord to remove, v to view current chords, m to return to menu: ")

            if user_input.lower() in ("q", "", "quit", "m", "menu"):
                break

            if user_input.lower() in ("v", "view"):
                self.view.display_simple_chord_list(self.model.chord_list)
            else:
                try:
                    chord_to_remove = None
                    for chord in self.model.chord_list:
                        if user_input == chord.chord_name:
                            chord_to_remove = chord
                            break

                    if chord_to_remove:
                        self.model.chord_list.remove(chord_to_remove)
                        # Remove notes from note_hist
                        for note in chord_to_remove.notes:
                            self.model.note_hist[note.get_true_note()] -= 1
                        self.view.display_message(f'{user_input} has been removed')
                    else:
                        self.view.display_message('Chord not found')
                except Exception as e:
                    self.view.display_message(f'Exception occurred: {e}')

    def gpt_integration(self):
        self.view.display_message("GPT thinking...")
        find_key(self.model.chord_list)

    def examine_chords(self) -> None:
        self.view.display_chords_and_notes(self.model.chord_list, self.model.note_hist)
        self.view.display_note_hist(self.model.note_hist)
        self.view.get_input("Hit enter to return to the menu")