from Models.Chord import Chord
from Services.music_service import build_chord, add_chords_to_hist, build_hist, add_chord_to_hist
from View.terminal_view import view_note_hist


def listen_new_chords(controller) -> None:
    while True:
        user_input = controller.view.get_input("Input a chord to enter or q to quit: ")

        if user_input.lower() in ("q", "", "quit"):
            break

        try:
            repeat: bool = False
            # Check for repeats
            for chord in controller.chord_list:
                if user_input == chord.chord_name:
                    repeat = True
                    controller.view.display_message("Chord already added")
            if not repeat:
                new_chord: Chord = build_chord(user_input)
                controller.chord_list.append(new_chord)
                add_chord_to_hist(controller.note_hist, new_chord)
        except Exception as e:
            controller.view.display_message(f"Invalid Input")
    return


# TODO Save chords always in the same case format
def listen_remove_chords(controller) -> None:
    while True:
        controller.view.display_simple_chord_list(controller.chord_list)
        user_input = controller.view.get_input("Input a chord to remove, v to view current chords, m to return to menu: ")

        if user_input.lower() in ("q", "", "quit", "m", "menu"):
            break

        if user_input.lower() in ("v", "view"):
            controller.view.display_simple_chord_list(controller.chord_list)
        else:
            try:
                chord_to_remove = None
                for chord in controller.chord_list:
                    if user_input == chord.chord_name:
                        chord_to_remove = chord
                        break

                if chord_to_remove:
                    controller.chord_list.remove(chord_to_remove)
                    # Remove notes from note_hist
                    for note in chord_to_remove.notes:
                        controller.note_hist[note.get_true_note()] -= 1
                    controller.view.display_message(f'{user_input} has been removed')
                else:
                    controller.view.display_message('Chord not found')
            except Exception as e:
                controller.view.display_message(f'Exception occurred: {e}')


def examine_chords(controller) -> None:
    controller.new_chord_list.clear()
    controller.view.display_chords_and_notes(controller.chord_list, controller.note_hist)
    view_note_hist(controller.note_hist)
    controller.view.get_input("Hit enter to return to the menu")
