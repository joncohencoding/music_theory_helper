from typing import Dict

from Services.music_service import get_chord_notes, get_chord_intervals, build_chord, build_hist, add_chords_to_hist
from Models.Chord import Chord
from Services.chatgpt import test_response, find_key
from View.terminal_view import view_chords_and_notes, view_note_hist


def init_controller():
    chord_list: list[Chord] = []
    note_hist: Dict[str, int] = {}
    new_chord_list: list[Chord] = []
    while True:
        chord_name = input("Enter a chord name to compare, type enter to compare, clear to reset: ")
        if chord_name.lower() == 'exit':
            break

        elif chord_name == 'test':
            test_response()

        elif chord_name == '':
            if note_hist:
                note_hist = add_chords_to_hist(note_hist, new_chord_list)
            else:
                note_hist = build_hist(chord_list)
            new_chord_list.clear()
            view_chords_and_notes(chord_list, note_hist)
            view_note_hist(note_hist)
        elif chord_name.lower() == 'clear':
            chord_list.clear()
            note_hist.clear()

        elif chord_name.lower() == 'key':
            find_key(chord_list)
        else:
            try:
                repeat: bool = False
                for chord in chord_list:
                    if chord_name == chord.chord_name:
                        repeat = True
                        print("Chord already added")
                if not repeat:
                    new_chord: Chord = build_chord(chord_name)
                    chord_list.append(new_chord)
                    new_chord_list.append(new_chord)
            except Exception as e:
                print(f"Invalid Input")

        print("")


