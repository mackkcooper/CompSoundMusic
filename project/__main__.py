import generate_frames, play_frames

NOTE = 'C'
OCTAVE = 5
JUST = True
LENGTH = .5

play_frames.play(generate_frames.generate_note(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_major_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_minor_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_diminished_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_major_seventh_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_minor_seventh_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_dominant_seventh_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_suspended_second_chord(NOTE, OCTAVE, JUST, LENGTH))
play_frames.play(generate_frames.generate_augmented_chord(NOTE, OCTAVE, JUST, LENGTH))


# one = generate_frames.generate_note_frames('Cb', 5, True, .25)
# two = generate_frames.generate_note_frames('Cb', 5, True, .25)
# three = generate_frames.generate_note_frames('Ab', 5, True, .25)
# four = generate_frames.generate_note_frames('Cb', 5, True, .5)
# five = generate_frames.generate_note_frames('Gb', 5, True, .5)
# six = generate_frames.generate_note_frames('Gb', 5, True, .25)
# play_frames.play(one + two + three + four + five + six)

# one = generate_frames.generate_chord_frames('Cb', 5, True, True, .25)
# two = generate_frames.generate_chord_frames('Cb', 5, True, True, .25)
# three = generate_frames.generate_chord_frames('Ab', 5, True, True, .25)
# four = generate_frames.generate_chord_frames('Cb', 5, True, True, .5)
# five = generate_frames.generate_chord_frames('Gb', 5, True, True, .5)
# six = generate_frames.generate_chord_frames('Gb', 5, True, True, .25)
# play_frames.play(one + two + three + four + five + six)