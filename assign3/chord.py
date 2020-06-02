import argparse, re

# argument parsing
def validateChord(chord):
    regex = re.compile('^[ABCDEFG](b|m|bm|mb)?$', re.IGNORECASE)
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

ap = argparse.ArgumentParser(description='Creates a wav file containing a chord.')
ap.add_argument('chord', metavar='C', type=validateChord, help="some chord A-G, optionally followed by 'b' to flatten and/or 'm' to make it minor instead of major")
ap.add_argument('temperament', metavar='T', type=validateTemperament, help="'equal' or 'just'")
args = ap.parse_args()

filename = args.chord + '-' + args.temperament + '.wav'
print(filename)