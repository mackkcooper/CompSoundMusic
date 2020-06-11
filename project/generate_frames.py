import re, wave, math, struct
from wave_funcs import generate_sin_note
from frequency import get_freq, modify_freq

NUM_CHANNELS = 1
SAMPLE_SIZE = 2 # bytes
FRAME_RATE = 48000 # samples per second
MAX_AMPLITUDE = 1/6
INTEGER_FORMAT = '<h'

def generate_frames(sound_type, note, octave, just, length):
    if sound_type == 'note':
        return generate_note(note, octave, just, length)
    if sound_type == 'maj':
        return generate_major_chord(note, octave, just, length)
    if sound_type == 'min':
        return generate_minor_chord(note, octave, just, length)
    if sound_type == 'dim':
        return generate_diminished_chord(note, octave, just, length)
    if sound_type == 'maj7':
        return generate_major_seventh_chord(note, octave, just, length)
    if sound_type == 'min7':
        return generate_minor_seventh_chord(note, octave, just, length)
    if sound_type == 'dom7':
        return generate_dominant_seventh_chord(note, octave, just, length)
    if sound_type == 'sus2':
        return generate_suspended_second_chord(note, octave, just, length)
    if sound_type == 'sus4':
        return generate_suspended_fourth_chord(note, octave, just, length)
    if sound_type == 'aug':
        return generate_augmented_chord(note, octave, just, length)
    return generate_note(note, octave, just, length)

def generate_rest(length):
    frames = []
    for n in range(0, math.floor(FRAME_RATE * length)):
        frames.append(struct.pack(INTEGER_FORMAT, 0))
    return frames

def generate_note(note, octave, just, length):
    note_freq = get_freq(note, octave, just)
    #sin generation
    root_set = generate_sin_note(note_freq, FRAME_RATE, SAMPLE_SIZE, MAX_AMPLITUDE, length)
    frames = []
    # note packing
    for n in range(0, math.floor(FRAME_RATE * length)):
        integer_value = math.floor(root_set[n])
        max_integer_value = math.pow(2,(SAMPLE_SIZE*8)-1)
        if(integer_value == max_integer_value):
            integer_value -= 1
        frames.append(struct.pack(INTEGER_FORMAT, integer_value))
    return frames

def generate_major_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 4, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_minor_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 3, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_diminished_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 3, just))
    frequencies.append(modify_freq(frequencies[0], 6, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_major_seventh_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 4, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frequencies.append(modify_freq(frequencies[0], 11, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_minor_seventh_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 3, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frequencies.append(modify_freq(frequencies[0], 10, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_dominant_seventh_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 4, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frequencies.append(modify_freq(frequencies[0], 10, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_suspended_second_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 2, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_suspended_fourth_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 5, just))
    frequencies.append(modify_freq(frequencies[0], 7, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_augmented_chord(root, octave, just, length):
    frequencies = []
    frequencies.append(get_freq(root, octave, just))
    frequencies.append(modify_freq(frequencies[0], 4, just))
    frequencies.append(modify_freq(frequencies[0], 8, just))
    frame_sets = generate_frame_sets(frequencies, length)
    return frame_pack(frame_sets, length)

def generate_frame_sets(frequencies, length):
    frame_sets = []
    for freq in frequencies:
        frame_sets.append(generate_sin_note(freq, FRAME_RATE, SAMPLE_SIZE, MAX_AMPLITUDE, length))
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