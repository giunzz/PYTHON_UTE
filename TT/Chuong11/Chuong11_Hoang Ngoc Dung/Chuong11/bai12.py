# Below are the notes used in music:
# C C# D D# E F F# G G# A A# B
# The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps
# past C and G is 7 steps past C. This works for any base. For example, the notes for D major
# are D, F#, A. We can represent the major chord steps as a list with two elements: [4,7]. The
# corresponding lists for some other chord types are shown below:
# Minor [3,7] Dominant seventh [4,7,10]
# Augmented fifth [4,8] Minor seventh [3,7,10]
# Minor fifth [4,6] Major seventh [4,7,11]
# Major sixth [4,7,9] Diminished seventh [3,6,10]
# Minor sixth [3,7,9]
# Write a program that asks the user for the key and the chord type and prints out the notes of
# the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists
# of steps.

chord_steps = {
    'C' : 1,
    'C#' : 2,
    'D' : 3,
    'D#' : 4,
    'E' : 5,
    'F' : 6,
    'F#' : 7,
    'G' : 8,
    'G#' : 9,
    'A' : 10,
    'A#' : 11,
    'B' : 12,}

type_chord_steps = {
    "Minor" : [3,7],
    "Dominant seventh" : [4,7,10],
    "Augmented fifth" : [4,8],
    "Minor seventh" : [3,7,10],
    "Minor fifth" : [4,6],
    "Major seventh" : [4,7,11],
    "Major sixth" : [4,7,9],
    "Diminished seventh" : [3,6,10],
    "Minor sixth" : [3,7,9]}


key = input("Enter the key (C C# D D# E F F# G G# A A# B ): ")
chord_type = input("Enter the chord type (Minor, Dominant seventh, Augmented fifth, Minor seventh, Minor fifth, Major seventh, Major sixth, Diminished seventh, Minor sixth): ")

if key in chord_steps and chord_type in type_chord_steps:
    key_value = chord_steps[key]
    chord_type_steps = type_chord_steps[chord_type]
    
    chord_notes = []
    for step in chord_type_steps:
        note_value = (key_value + step - 1) % 12 + 1
        chord_notes.append(list(chord_steps.keys())[list(chord_steps.values()).index(note_value)])

    print("Notes of the chord:", [key] + chord_notes)
else:
    print("Invalid key or chord type.")


