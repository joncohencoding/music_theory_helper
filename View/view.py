from abc import ABC, abstractmethod
from typing import List, Dict, Any

from Models.Chord import Chord
from Utils.Colors import color, COLORS, get_color


class ViewInterface(ABC):
    @abstractmethod
    def display_message(self, message: str):
        pass

    @abstractmethod
    def get_input(self, prompt: Any) -> Any:
        pass

    @abstractmethod
    def display_chord(self, chord: Chord) -> None:
        pass

    @abstractmethod
    def display_notes(self, chord: Chord, chord_hist: Dict[str, int]) -> None:
        pass

    @abstractmethod
    def display_intervals(self, chord: Chord) -> None:
        pass

    @abstractmethod
    def display_chords_and_notes(self, chord_list: List[Chord], chord_hist: Dict[str, int]) -> None:
        pass

    @abstractmethod
    def display_note_hist(self, note_hist: Dict[str, int]) -> None:
        pass

    @abstractmethod
    def display_simple_chord_list(self, chords: List[Chord]) -> None:
        pass


class TerminalView(ViewInterface):
    def display_message(self, message: str) -> None:
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def display_chord(self, chord: Chord) -> None:
        print(f'Chord: {color(chord.chord_name, COLORS.CYAN)}')

    def display_notes(self, chord: Chord, chord_hist: Dict[str, int]) -> None:
        max_width = 4  # Adjust this as needed
        print('Note:     | ', end='')
        for note in chord.notes:
            formatted_note = note.get_name().center(max_width)
            note_color: str = get_color(note.get_true_note(), chord_hist)
            print(f'{color(formatted_note, note_color)}', end=' | ')
        print()

    def display_intervals(self, chord: Chord):
        max_width = 4
        print('Interval: | ', end='')
        for interval in chord.intervals:
            formatted_interval = interval.center(max_width)
            print(f'{color(formatted_interval, COLORS.MAGENTA)}', end=' | ')
        print()

    def display_chords_and_notes(self, chord_list: List[Chord], chord_hist: Dict[str, int]) -> None:
        for chord in chord_list:
            self.display_chord(chord)
            self.display_notes(chord, chord_hist)
            self.display_intervals(chord)
            print()

    def display_note_hist(self, note_hist: Dict[str, int]) -> None:
        pass

    def display_simple_chord_list(self, chords: List[Chord]) -> None:
        print("Chords: " + ", ".join(chord.chord_name for chord in chords))

