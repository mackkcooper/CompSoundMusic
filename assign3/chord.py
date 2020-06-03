import argparse, re, wave, math, struct

# argument validation functions
def validateChord(chord):
    regex = re.compile('^[CDEFGAB](b|m|bm|mb)?$')
    if regex.match(str(chord)):
        return chord
    else:
        raise argparse.ArgumentTypeError("First argument ('" + chord + "') must be composed of a note A-G, optionally followed by 'b' and/or 'm'.")

def validateTemperament(temp):
    if str(temp) == 'equal':
        return temp
    if str(temp) == 'just':
        return temp
    raise argparse.ArgumentTypeError("Second argument ('" + temp + "') must be either 'equal' or 'just'.")

# argument parsing
ap = argparse.ArgumentParser(description='Creates a wav file containing a chord.')
ap.add_argument('chord', metavar='C', type=validateChord, help="some chord A-G, optionally followed by 'b' to flatten and/or 'm' to make it minor instead of major")
ap.add_argument('temperament', metavar='T', type=validateTemperament, help="'equal' or 'just'")
args = ap.parse_args()

# argument interpretation
FILENAME = args.chord + '-' + args.temperament + '.wav'
ROOT = args.chord[0]
FLATTEN = 'b' in args.chord
MINOR = 'm' in args.chord
EQUAL = args.temperament == 'equal'
JUST = args.temperament == 'just'

# write variable setup
MAX_AMPLITUDE = 1/6
LENGTH = 1 # second
NUM_CHANNELS = 1
SAMPLE_SIZE = 2 # bytes
FRAME_RATE = 48000 # samples per second

if(SAMPLE_SIZE == 1):
    integer_format = '<B'
elif(SAMPLE_SIZE == 2):
    integer_format = '<h'
elif(SAMPLE_SIZE == 4):
    integer_format = '<i'
else:
    exit('ERROR: supported samples sizes are 1, 2, 4 bytes')

# freqency functions
def equalFreqency(base_freq, i):
    return base_freq * math.pow(2, i/12)

just_table = [1, 16/15, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 9/5, 15/8]
def justFreqency(base_freq, i):
    return base_freq * just_table[i]

# root frequency selection
octave_5_freq_table = {
    'C': 523.25,
    'Db': 554.37,
    'D': 587.33,
    'Eb': 622.25,
    'E': 659.26,
    'Fb': 659.26,
    'F': 698.46,
    'Gb': 739.99,
    'G': 783.99,
    'Ab': 830.61,
    'A': 880.00,
    'Bb': 932.33,
    'B': 987.77,
    'Cb': 987.77
}

if FLATTEN:
    root_freq = octave_5_freq_table[ROOT + 'b']
else: 
    root_freq = octave_5_freq_table[ROOT]
if EQUAL:
    fifth_freq = equalFreqency(root_freq, 7)
    if MINOR:
        third_freq = equalFreqency(root_freq, 3)
    else: # major
        third_freq = equalFreqency(root_freq, 4)
if JUST:
    fifth_freq = justFreqency(root_freq, 7)
    if MINOR:
        third_freq = justFreqency(root_freq, 3)
    else: # major
        third_freq = justFreqency(root_freq, 4)

# sin generation function
def generate_sin(frequency, frame_rate, sample_size, length):
    total_samples = math.floor(frame_rate * length)
    samples_per_cycle = frame_rate / frequency
    sample_unit = (2 * math.pi) / samples_per_cycle
    value = 0
    sample_set = []
    max_integer_value = math.pow(2,(SAMPLE_SIZE*8)-1)
    for n in range(0, total_samples):
        value = (value + sample_unit) % (2 * math.pi)
        integer_value = math.floor(math.sin(value) * max_integer_value * MAX_AMPLITUDE)
        if(integer_value == max_integer_value):
            integer_value -= 1
        sample_set.append(integer_value)
    return sample_set

# sin generation
root_set = generate_sin(root_freq, FRAME_RATE, SAMPLE_SIZE, LENGTH)
fifth_set = generate_sin(fifth_freq, FRAME_RATE, SAMPLE_SIZE, LENGTH)
third_set = generate_sin(third_freq, FRAME_RATE, SAMPLE_SIZE, LENGTH)

# file write setup
file = wave.open(FILENAME, 'wb')
file.setnchannels(NUM_CHANNELS)
file.setsampwidth(SAMPLE_SIZE)
file.setframerate(FRAME_RATE)

# root note test
# for n in range(0, math.floor(FRAME_RATE * LENGTH)):
#     file.writeframes(struct.pack(integer_format, root_set[n]))

# chord creation
for n in range(0, math.floor(FRAME_RATE * LENGTH)):
    integer_value = root_set[n] + fifth_set[n] + third_set[n]
    integer_value = math.floor(integer_value)
    max_integer_value = math.pow(2,(SAMPLE_SIZE*8)-1)
    if(integer_value == max_integer_value):
        integer_value -= 1
    file.writeframes(struct.pack(integer_format, integer_value))

# wrap-up
file.close()
print('Output file ' + FILENAME + ' created.')