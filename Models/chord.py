from typing import Dict

from Models.note import Note
from Utils.Colors import COLORS, get_color, color


class Chord:
    def __init__(self, chord_name: str, notes: list[Note], intervals: list[str]):
        self.chord_name = chord_name
        self.notes = notes
        self.intervals = intervals

    def print_chord(self):
        # print(f'Chord: {COLORS.CYAN}{self.chord_name}{COLORS.RESET}')
        print(f'Chord: {color(self.chord_name, COLORS.CYAN)}')

    def print_notes(self, chord_hist: Dict[str, int]):
        max_width = 4  # Adjust this as needed
        print('Note:     | ', end='')
        for note in self.notes:
            formatted_note = note.get_name().center(max_width)
            note_color: str = get_color(note.get_true_note(), chord_hist)
            print(f'{color(formatted_note, note_color)}', end=' | ')
        print()

    def print_intervals(self):
        max_width = 4
        print('Interval: | ', end='')
        for interval in self.intervals:
            formatted_interval = interval.center(max_width)
            print(f'{color(formatted_interval, COLORS.MAGENTA)}', end=' | ')
        print()
