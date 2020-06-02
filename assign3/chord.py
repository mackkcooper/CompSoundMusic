import argparse, re, wave, math

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

# wav file setup
MAX_AMPLITUDE = 1/6
LENGTH = 1 # second
NUM_CHANNELS = 1
SAMPLE_WIDTH = 2 # bytes
FRAMERATE = 48000 # samples per second
write = wave.open(FILENAME, 'wb')
write.setnchannels(1)
write.setsampwidth(2)
write.setframerate(48000)

# freqency functions
def equalFreqency(base_freq, i):
    return base_freq * math.pow(2, i/12)

just_table = {1, 16/15, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 9/5, 15/8}
def justFreqency(base_freq, i):
    return base_freq * just_table[i]

# chord creation

# wrap-up
write.close()
print('Output file ' + FILENAME + ' created.')