import re, argparse, csv
from play_frames import play
from generate_frames import generate_frames, generate_rest

def validateNote(note):
    regex = re.compile('^[CDEFGAB](b)?$')
    if regex.match(str(note)):
        return note
    else:
        raise argparse.ArgumentTypeError("Argument for note ('" + note + "' given) must be composed of a note A-G, optionally followed by 'b' for a flattened note.")

def validateStyle(style):
    regex = re.compile('^(note|maj|min|dim|maj7|min7|dom7|sus2|sus4|aug)$')
    if regex.match(str(style)):
        return style
    else:
        error_message = "Argument for style ('" + style + "' given) must be one of:\n"
        error_message += "\t'note' = single note\n"
        error_message += "\t'maj' = major chord\n"
        error_message += "\t'min' = minor chord\n"
        error_message += "\t'dim' = diminished chord\n"
        error_message += "\t'maj7' = major seventh chord\n"
        error_message += "\t'min7' = minor seventh chord\n" 
        error_message += "\t'dom7' = dominant seventh chord\n" 
        error_message += "\t'sus2' = suspended second chord\n"
        error_message += "\t'sus4' = suspended fourth chord\n"
        error_message += "\t'aug' = augmented chord"
        raise argparse.ArgumentTypeError(error_message)

# argument parsing
ap = argparse.ArgumentParser(description='Plays a neat tune!')
ap.add_argument('--note', '-n', help='specify the note played when showing styles', default='C', type=validateNote)
ap.add_argument('--octave', '-o', help='specify the octave of the note or root octave of a tune', type=int, default=5)
ap.add_argument('--length', '-l', help='specify the length of each note', type=float, default=.25)
ap.add_argument('--style', '-s', help='specify the kind of style the note will take when you play a file (e.g. note, maj, min, dim, maj7, min7, dom7, sus2, sus4, aug)', default='note', type=validateStyle)
ap.add_argument('--just', '-j', help='use the just instead of equal scale', default=False, action='store_true')
ap.add_argument('--file', '-f', help='specify a properly formatted csv file to play instead of all the styles')
args = ap.parse_args()

NOTE = args.note
OCTAVE = args.octave
LENGTH = args.length
STYLE = args.style
JUST = args.just
FILE_NAME = args.file

print(
    'note=' + NOTE + 
    ', octave=' + str(OCTAVE) + 
    ', length=' + str(LENGTH) + 
    ', style=' + STYLE + 
    ', just=' + str(JUST) + 
    ', file=' + str(FILE_NAME)
)

if FILE_NAME:
    file_reader = csv.reader(open(FILE_NAME, newline=''))
    audio = []
    for row in file_reader:
        if row == []:
            continue
        if row[0] == 'rest':
            audio += generate_rest(float(row[1]) * LENGTH)
        else:
            audio += generate_frames(STYLE, row[0], int(row[1]) + OCTAVE, JUST, float(row[2]) * LENGTH)
    play(audio)
else:
    audio = generate_frames('note', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_rest(LENGTH)
    audio += generate_frames('maj', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('min', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('dim', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('maj7', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('min7', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('dom7', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('sus2', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('sus4', NOTE, OCTAVE, JUST, LENGTH)
    audio += generate_frames('aug', NOTE, OCTAVE, JUST, LENGTH)
    play(audio)