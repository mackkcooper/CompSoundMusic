import pyaudio, wave

def play(filename):
    print('playing ' + filename + '...')
    file = wave.open(filename, mode='rb') # open wav file
    NUM_CHANNELS = file.getnchannels()
    SAMPLE_SIZE = file.getsampwidth()
    SAMPLE_RATE = file.getframerate()
    CHUNK_SIZE = 1024
    # print(NUM_CHANNELS, SAMPLE_SIZE, SAMPLE_RATE)

    pa = pyaudio.PyAudio() # instantiate pyaudio
    pa_stream = pa.open( # instantiate pyaudio stream
        format = pa.get_format_from_width(SAMPLE_SIZE),
        channels = NUM_CHANNELS,
        rate = SAMPLE_RATE,
        output = True
    )

    data = file.readframes(CHUNK_SIZE)
    while(len(data) > 0):
        pa_stream.write(data)
        data = file.readframes(CHUNK_SIZE)

    # closing pyaudio and stream
    pa_stream.stop_stream()
    pa_stream.close()
    pa.terminate()
    print('playback ended')