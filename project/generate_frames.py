import re, wave, math, struct
import wave_funcs, frequency

NUM_CHANNELS = 1
SAMPLE_SIZE = 2 # bytes
FRAME_RATE = 48000 # samples per second
MAX_AMPLITUDE = 1/6
INTEGER_FORMAT = '<h'

def generate_note(note, octave, just, length):
    if just:
        note_freq = frequency.get_just_frequency(note, octave)
    else:
        note_freq = frequency.get_equal_frequency(note, octave)
    #sin generation
    root_set = wave_funcs.generate_sin_note(note_freq, FRAME_RATE, SAMPLE_SIZE, MAX_AMPLITUDE, length)
    frames = []
    # note packing
    for n in range(0, math.floor(FRAME_RATE * length)):
        integer_value = root_set[n]
        integer_value = math.floor(integer_value)
        max_integer_value = math.pow(2,(SAMPLE_SIZE*8)-1)
        if(integer_value == max_integer_value):
            integer_value -= 1
        frames.append(struct.pack(INTEGER_FORMAT, integer_value))
    return frames

def generate_major_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_minor_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 3))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 3))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_diminished_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 3))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 6))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 3))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 6))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_major_seventh_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 11))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 11))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_minor_seventh_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 3))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 10))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 3))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 10))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_dominant_seventh_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 10))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 10))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_suspended_second_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 2))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 2))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_suspended_fourth_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 5))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 7))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 5))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 7))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_augmented_chord(root, octave, just, length):
    frequencies = []
    if just:
        frequencies.append(frequency.get_just_frequency(root, octave))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.just_freqency_steps(frequencies[0], 8))
    else:
        frequencies.append(frequency.get_equal_frequency(root, octave))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 4))
        frequencies.append(frequency.equal_freqency_steps(frequencies[0], 8))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_frame_sets(frequencies, length):
    frame_sets = []
    for freq in frequencies:
        frame_sets.append(wave_funcs.generate_sin_note(freq, FRAME_RATE, SAMPLE_SIZE, MAX_AMPLITUDE, length))
    return frame_sets

def frame_pack(frame_sets, length):
    frames = []
    # chord creation and packing
    for n in range(0, math.floor(FRAME_RATE * length)):
        integer_value = 0
        for frame_set in frame_sets:
            integer_value += frame_set[n]
        integer_value = math.floor(integer_value)
        max_integer_value = math.pow(2,(SAMPLE_SIZE*8)-1)
        if(integer_value == max_integer_value):
            integer_value -= 1
        frames.append(struct.pack(INTEGER_FORMAT, integer_value))
    return frames