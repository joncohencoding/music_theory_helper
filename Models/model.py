from typing import List, Dict

from music21.note import Note

from Models.chord import Chord
from abc import abstractmethod, ABC


from Services.music_service import get_true_note, get_chord_notes, get_chord_intervals, build_chord_object


class ModelInterface(ABC):

    @abstractmethod
    def add_chord_to_hist(self, new_chord: Chord) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear_data(self) -> None:
        raise NotImplementedError


class NonDBModel(ModelInterface):
    def __init__(self, chord_list: List[Chord] = None, note_hist: Dict[str,int] = None):
        self.chord_list: List[Chord] = [] if chord_list is None else chord_list
        self.note_hist: Dict[str, int] = {} if note_hist is None else note_hist

    # Return updated note_hist
    def add_chord_to_hist(self, new_chord: Chord) -> None:
        for note in new_chord.notes:
            if note.get_true_note() in self.note_hist:
                self.note_hist[note.get_true_note()] += 1
            else:
                self.note_hist[note.get_true_note()] = 1

    def clear_data(self) -> None:
        self.chord_list = []
        self.note_hist = {}

    @staticmethod
    def get_chord_intervals(chord_name: str) -> List[str]:
        return get_chord_intervals(chord_name)

    @staticmethod
    def build_chord_object(chord_name: str) -> Chord:
        return build_chord_object(chord_name)

    @staticmethod
    def get_true_note(chord_name: str, steps: int) -> str:
        return get_true_note(chord_name, steps)

    @staticmethod
    def get_chord_notes(chord_name: str) -> list[Note]:
        return get_chord_notes(chord_name)

    # TODO: Add add chord method
