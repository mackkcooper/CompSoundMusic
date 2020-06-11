import math

SOFTEN_RANGE = 2000

# sin generation function
def generate_sin_note(frequency, frame_rate, sample_size, max_amplitude, length):
    total_samples = math.floor(frame_rate * length)
    samples_per_cycle = frame_rate / frequency
    sample_unit = (2 * math.pi) / samples_per_cycle
    value = 0
    sample_set = []
    max_integer_value = math.pow(2,(sample_size*8)-1)
    for n in range(0, total_samples):
        if n < SOFTEN_RANGE:
            soften = n/SOFTEN_RANGE
        elif n > (total_samples - SOFTEN_RANGE):
            soften = (total_samples - n)/SOFTEN_RANGE
        else: 
            soften = 1
        value = (value + sample_unit) % (2 * math.pi)
        integer_value = math.floor(math.sin(value) * max_integer_value * max_amplitude * soften)
        if(integer_value == max_integer_value):
            integer_value -= 1
        sample_set.append(integer_value)
    return sample_set

def generate_piano_note(frequency, frame_rate, sample_size, max_amplitude, length):
    total_samples = math.floor(frame_rate * length)
    samples_per_cycle = frame_rate / frequency
    sample_unit = (2 * math.pi) / samples_per_cycle
    value = 0
    sample_set = []
    max_integer_value = math.pow(2,(sample_size*8)-1)
    for n in range(0, total_samples):
        if n < SOFTEN_RANGE:
            soften = n/SOFTEN_RANGE
        elif n > (total_samples - SOFTEN_RANGE):
            soften = (total_samples - n)/SOFTEN_RANGE
        else: 
            soften = 1
        value = (value + sample_unit) % (2 * math.pi)
        integer_value = math.floor(piano_note_func(value) * max_integer_value * max_amplitude * soften)
        if(integer_value == max_integer_value):
            integer_value -= 1
        sample_set.append(integer_value)
    return sample_set

def piano_note_func(value):
    wave_value = -1/4 * math.sin(3 * math.pi * value)
    wave_value += 1/4 * math.sin(math.pi * value)
    wave_value += (math.sqrt(3)/2) * math.cos(math.pi * value)
    return wave_value