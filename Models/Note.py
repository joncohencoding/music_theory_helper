from typing import List

TRUE_NOTES: List[str] = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


class Note:
    def __init__(self, name, interval, true_note):
        self.name = name
        self.interval = interval
        self.true_note = true_note

    def set_name(self, name) -> None :
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_interval(self, interval) -> None:
        self.interval = interval

    def get_interval(self) -> str:
        return self.interval

    def set_true_note(self, true_note) -> None:
        self.true_note = true_note

    def get_true_note(self) -> str:
        return self.true_note
