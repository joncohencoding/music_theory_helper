# music_theory_helper
Python Project to see how the notes in chords progressions interact with each other

# CHORD_TYPES 
    # regular
    ('major', ['1,3,5', ['', 'M', 'maj']]),  # Y
    ('minor', ['1,-3,5', ['m', 'min']]),  # Y
    ('augmented', ['1,3,#5', ['+', 'aug']]),  # Y
    ('diminished', ['1,-3,-5', ['dim', 'o']]),  # Y

    # sevenths
    ('dominant-seventh', ['1,3,5,-7', ['7', 'dom7', ]]),  # Y: 'dominant'
    ('major-seventh', ['1,3,5,7', ['maj7', 'M7']]),  # Y
    ('minor-major-seventh', ['1,-3,5,7', ['mM7', 'm#7', 'minmaj7']]),  # Y: 'major-minor'
    ('minor-seventh', ['1,-3,5,-7', ['m7', 'min7']]),  # Y
    ('augmented-major-seventh', ['1,3,#5,7', ['+M7', 'augmaj7']]),  # N
    ('augmented-seventh', ['1,3,#5,-7', ['7+', '+7', 'aug7']]),  # Y
    ('half-diminished-seventh', ['1,-3,-5,-7', ['ø7', 'm7b5']]),  # Y: 'half-diminished'
    ('diminished-seventh', ['1,-3,-5,--7', ['o7', 'dim7']]),  # Y
    ('seventh-flat-five', ['1,3,-5,-7', ['dom7dim5']]), 

    # sixths
    ('major-sixth', ['1,3,5,6', ['6']]),  # Y
    ('minor-sixth', ['1,-3,5,6', ['m6', 'min6']]),  # Y

    # ninths
    ('major-ninth', ['1,3,5,7,9', ['M9', 'Maj9']]),  # Y
    ('dominant-ninth', ['1,3,5,-7,9', ['9', 'dom9']]),  # Y
    ('minor-major-ninth', ['1,-3,5,7,9', ['mM9', 'minmaj9']]),  # N
    ('minor-ninth', ['1,-3,5,-7,9', ['m9', 'min9']]),  # N
    ('augmented-major-ninth', ['1,3,#5,7,9', ['+M9', 'augmaj9']]),  # Y
    ('augmented-dominant-ninth', ['1,3,#5,-7,9', ['9#5', '+9', 'aug9']]),  # N
    ('half-diminished-ninth', ['1,-3,-5,-7,9', ['ø9']]),  # N
    ('half-diminished-minor-ninth', ['1,-3,-5,-7,-9', ['øb9']]),  # N
    ('diminished-ninth', ['1,-3,-5,--7,9', ['o9', 'dim9']]),  # N
    ('diminished-minor-ninth', ['1,-3,-5,--7,-9', ['ob9', 'dimb9']]),  # N

    # elevenths
    ('dominant-11th', ['1,3,5,-7,9,11', ['11', 'dom11']]),  # Y
    ('major-11th', ['1,3,5,7,9,11', ['M11', 'Maj11']]),  # Y
    ('minor-major-11th', ['1,-3,5,7,9,11', ['mM11', 'minmaj11']]),  # N
    ('minor-11th', ['1,-3,5,-7,9,11', ['m11', 'min11']]),  # Y
    ('augmented-major-11th', ['1,3,#5,7,9,11', ['+M11', 'augmaj11']]),  # N
    ('augmented-11th', ['1,3,#5,-7,9,11', ['+11', 'aug11']]),  # N
    ('half-diminished-11th', ['1,-3,-5,-7,9,11', ['ø11']]),  # N
    ('diminished-11th', ['1,-3,-5,--7,9,11', ['o11', 'dim11']]),  # N

    # thirteenths
    ('major-13th', ['1,3,5,7,9,11,13', ['M13', 'Maj13']]),  # Y
    ('dominant-13th', ['1,3,5,-7,9,11,13', ['13', 'dom13']]),  # Y
    ('minor-major-13th', ['1,-3,5,7,9,11,13', ['mM13', 'minmaj13']]),  # N
    ('minor-13th', ['1,-3,5,-7,9,11,13', ['m13', 'min13']]),  # Y
    ('augmented-major-13th', ['1,3,#5,7,9,11,13', ['+M13', 'augmaj13']]),  # N
    ('augmented-dominant-13th', ['1,3,#5,-7,9,11,13', ['+13', 'aug13']]),  # N
    ('half-diminished-13th', ['1,-3,-5,-7,9,11,13', ['ø13']]),  # N

    # other
    ('suspended-second', ['1,2,5', ['sus2']]),  # Y
    ('suspended-fourth', ['1,4,5', ['sus', 'sus4']]),  # Y
    ('suspended-fourth-seventh', ['1,4,5,-7', ['7sus', '7sus4']]),  # Y
    ('Neapolitan', ['1,2-,3,5-', ['N6']]),  # Y
    ('Italian', ['1,#4,-6', ['It+6', 'It']]),  # Y
    ('French', ['1,2,#4,-6', ['Fr+6', 'Fr']]),  # Y
    ('German', ['1,-3,#4,-6', ['Gr+6', 'Ger']]),  # Y
    ('pedal', ['1', ['pedal']]),  # Y
    ('power', ['1,5', ['power']]),  # Y
    ('Tristan', ['1,#4,#6,#9', ['tristan']]),  # Y
