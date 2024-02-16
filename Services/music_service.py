from typing import Dict

from music21 import harmony, interval
from Models.chord import Chord
from Models.note import Note, TRUE_NOTES


def get_chord_notes(chord_name) -> list[Note]:
    # Parse the chord name to a Chord object
    chord = harmony.ChordSymbol(chord_name)
    notes: list[Note] = []

    for pitch in chord.pitches:
        steps: int = 0
        note_name: str = pitch.name
        natural_note: str = note_name[0]
        for char in note_name[1:]:
            if char == "#":
                steps += 1
            elif char == "-":
                steps -= 1
        true_note: str = get_true_note(natural_note, steps)

        root_note = chord.root()
        interv = interval.Interval(noteStart=root_note, noteEnd=pitch)

        notes.append(Note(note_name, interv, true_note))

    return notes


# Take a chord name as input, convert to a ChordSymbol object, get intervals
def get_chord_intervals(chord_name) -> list[str]:
    # Parse the chord name to a Chord object
    chord_obj = harmony.ChordSymbol(chord_name)
    root_note = chord_obj.root()

    intervals = []
    for pitch in chord_obj.pitches:
        # Calculate the interval from the root note to the current note
        interv = interval.Interval(noteStart=root_note, noteEnd=pitch)
        intervals.append(interv.simpleName)

    return intervals


def build_chord_object(chord_name: str) -> Chord:
    chord_notes: list[Note] = get_chord_notes(chord_name)
    chord_intervals: list[str] = get_chord_intervals(chord_name)

    return Chord(chord_name, chord_notes, chord_intervals)



# Find and return the true note, so we can compare notes that are the same but don't have the same name
# For Example, C- and B#
def get_true_note(natural_note: str, steps) -> str:
    try:
        natural_note_index: int = TRUE_NOTES.index(natural_note)
        note_index = (natural_note_index + steps) % len(TRUE_NOTES)
        return TRUE_NOTES[note_index]
    except ValueError:
        print(f"'{natural_note}' is not a valid note")
        return ""
