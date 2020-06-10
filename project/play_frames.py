import pyaudio

LENGTH = 1 # second
NUM_CHANNELS = 1
SAMPLE_SIZE = 2 # bytes
FRAME_RATE = 48000 # samples per second

def play(frames):
    print('playing...')

    pa = pyaudio.PyAudio() # instantiate pyaudio
    pa_stream = pa.open( # instantiate pyaudio stream
        format = pa.get_format_from_width(SAMPLE_SIZE),
        channels = NUM_CHANNELS,
        rate = FRAME_RATE,
        output = True
    )

    for i in range(len(frames)):
        pa_stream.write(frames[i])

    # closing pyaudio and stream
    pa_stream.stop_stream()
    pa_stream.close()
    pa.terminate()
    print('playback ended')