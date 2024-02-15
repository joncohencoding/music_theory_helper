from Models.Chord import Chord
from Services.music_service import build_chord, add_chords_to_hist, build_hist
from View.terminal_view import view_chords_and_notes, view_note_hist


def accept_new_chords(controller) -> None:
    while True:
        user_input = input("Input a chord to enter or q to quit: ")

        if user_input.lower() in ("q", "", "quit"):
            break

        try:
            repeat: bool = False
            for chord in controller.chord_list:
                if user_input == chord.chord_name:
                    repeat = True
                    print("Chord already added")
            if not repeat:
                new_chord: Chord = build_chord(user_input)
                controller.chord_list.append(new_chord)
                controller.new_chord_list.append(new_chord)
        except Exception as e:
            print(f"Invalid Input")
    return


def examine_chords(controller) -> None:
    if controller.note_hist:
        controller.note_hist = add_chords_to_hist(controller.note_hist, controller.new_chord_list)
    else:
        controller.note_hist = build_hist(controller.chord_list)
    controller.new_chord_list.clear()
    view_chords_and_notes(controller.chord_list, controller.note_hist)
    view_note_hist(controller.note_hist)
    input("Hit enter to return to the menu")