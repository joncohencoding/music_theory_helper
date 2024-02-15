from Models.Chord import Chord
from Services.music_service import build_chord, add_chords_to_hist, build_hist, add_chord_to_hist
from View.terminal_view import view_chords_and_notes, view_note_hist, view_simple_chord_list


def listen_new_chords(controller) -> None:
    while True:
        user_input = input("Input a chord to enter or q to quit: ")

        if user_input.lower() in ("q", "", "quit"):
            break

        try:
            repeat: bool = False
            # Check for repeats
            for chord in controller.chord_list:
                if user_input == chord.chord_name:
                    repeat = True
                    print("Chord already added")
            if not repeat:
                new_chord: Chord = build_chord(user_input)
                controller.chord_list.append(new_chord)
                add_chord_to_hist(controller.note_hist, new_chord)
        except Exception as e:
            print(f"Invalid Input")
    return


#TODO Save chords always in the same case format
def listen_remove_chords(controller) -> None:
    while True:
        user_input = input("Input a chord to remove, v to view current chords, m to return to menu: ")

        if user_input.lower() in ("q", "", "quit", "m", "menu"):
            break

        if user_input.lower() in ("v", "view"):
            view_simple_chord_list(controller.chord_list)
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
                    print(user_input, "has been removed")
                else:
                    print("Chord not found")
            except Exception as e:
                print(f"Exception occurred: {e}")


def examine_chords(controller) -> None:
    if controller.note_hist:
        controller.note_hist = add_chords_to_hist(controller.note_hist, controller.new_chord_list)
    else:
        controller.note_hist = build_hist(controller.chord_list)
    controller.new_chord_list.clear()
    view_chords_and_notes(controller.chord_list, controller.note_hist)
    view_note_hist(controller.note_hist)
    input("Hit enter to return to the menu")
