import math

BASE_FREQ = 32.703

equal_note_table = {
    'C': 0,'Db': 1, 'D': 2, 'Eb': 3, 'E': 4, 'Fb': 4, 'F': 5, 'Gb': 6, 'G': 7, 'Ab': 8, 'A': 9, 'Bb': 10, 'B': 11, 'Cb': 11
}

just_note_table = {
    'C': 1, 'Db': 16/15, 'D': 9/8, 'Eb': 6/5, 'E': 5/4, 'Fb': 5/4, 'F': 4/3, 'Gb': 45/32, 'G': 3/2, 'Ab': 8/5, 'A': 5/3, 'Bb': 9/5, 'B': 15/8, 'Cb': 15/8
}

def get_equal_frequency(note, octave):
    half_steps_up = equal_note_table[note] + ((octave - 1) * 12)
    return BASE_FREQ * math.pow(2, half_steps_up/12)

def get_just_frequency(note, octave):
    return BASE_FREQ * just_note_table[note] * math.pow(2, octave - 1)

def equal_freqency_steps(root_freq, i):
    return root_freq * math.pow(2, i/12)

just_multiplier_table = [1, 16/15, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 9/5, 15/8]
def just_freqency_steps(root_freq, i):
    return root_freq * just_multiplier_table[i]