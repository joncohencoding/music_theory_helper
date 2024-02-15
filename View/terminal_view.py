from Models.Chord import Chord
from typing import Dict, List

from Utils.Colors import color, COLORS, get_color


def view_chords_and_notes(chord_list: List[Chord], chord_hist: Dict[str, int]):
    print()
    # for chord in chord_list:
    #     chord.print_chord()
    #     chord.print_notes(chord_hist)
    #     chord.print_intervals()
    #     print()
    for chord in chord_list:
        view_chord(chord)
        view_notes(chord, chord_hist)
        view_intervals(chord)
        print()


def view_note_hist(note_hist: Dict[str, int]) -> None:
    sorted_hist = dict(sorted(note_hist.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_hist.items():
        if int(value) > 1:
            print(f'{key}: {value}')
        else:
            break


def view_chord(chord: Chord) -> None:
    print(f'Chord: {color(chord.chord_name, COLORS.CYAN)}')


def view_notes(chord: Chord, chord_hist: Dict[str, int]) -> None:
    max_width = 4  # Adjust this as needed
    print('Note:     | ', end='')
    for note in chord.notes:
        formatted_note = note.get_name().center(max_width)
        note_color: str = get_color(note.get_true_note(), chord_hist)
        print(f'{color(formatted_note, note_color)}', end=' | ')
    print()

def view_intervals(chord: Chord):
    max_width = 4
    print('Interval: | ', end='')
    for interval in chord.intervals:
        formatted_interval = interval.center(max_width)
        print(f'{color(formatted_interval, COLORS.MAGENTA)}', end=' | ')
    print()


def view_simple_chord_list(chords: List[Chord]) -> None:
    for chord in chords:
        print(chord)
