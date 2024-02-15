from typing import Dict

from music21 import harmony, interval
from Models.Chord import Chord
from Models.Note import Note, TRUE_NOTES


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


# Take a chord name as input, convert to a ChordSymbol object
# using 
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


def build_chord(chord_name: str) -> Chord:
    chord_notes: list[Note] = get_chord_notes(chord_name)
    chord_intervals: list[str] = get_chord_intervals(chord_name)

    return Chord(chord_name, chord_notes, chord_intervals)


# This histogram is used to compare notes between chords and find matches
def build_hist(chord_list: list[Chord]) -> Dict[str, int]:
    note_hist: dict[str, int] = {}
    for chord in chord_list:
        for note in chord.notes:
            if note.get_true_note() in note_hist:
                # Need to change this to read note.name
                note_hist[note.get_true_note()] += 1
            else:
                note_hist[note.get_true_note()] = 1

    return note_hist


def add_chords_to_hist(note_hist: dict[str, int], new_chord_list: list[Chord]):
    for chord in new_chord_list:
        for note in chord.notes:
            if note.get_true_note() in note_hist:
                # Need to change this to read note.name
                note_hist[note.get_true_note()] += 1
            else:
                note_hist[note.get_true_note()] = 1
    return note_hist

# Return updated note_hist
def add_chord_to_hist(note_hist: dict[str, int], new_chord: Chord) -> dict[str, int]:
    for note in new_chord.notes:
        if note.get_true_note() in note_hist:
            note_hist[note.get_true_note()] += 1
        else:
            note_hist[note.get_true_note()] = 1
    return note_hist



# Find and return the true note so we can compare notes that are the same but don't have the same name
# For Example, C- and B#
def get_true_note(natural_note, steps) -> str:
    try:
        natural_note_index: int = TRUE_NOTES.index(natural_note)
        note_index = (natural_note_index + steps) % len(TRUE_NOTES)
        return TRUE_NOTES[note_index]
    except ValueError:
        print(f"'{natural_note}' is not a valid note")
        return ""
