import math, wave, struct

LENGTH = 1 # seconds
FREQUENCY = 440 # Hz
MAX_AMPLITUDE = .25
NUM_CHANNELS = 1
SAMPLE_SIZE = 1 # bytes
SAMPLE_RATE = 48_000 # per second

total_samples = math.floor(SAMPLE_RATE * LENGTH)
samples_per_cycle = SAMPLE_RATE / FREQUENCY
sample_unit = (2 * math.pi) / samples_per_cycle

file = wave.open('sin.wav', mode='wb')
file.setsampwidth(SAMPLE_SIZE)
file.setnchannels(NUM_CHANNELS)
file.setframerate(SAMPLE_RATE)

value = 0
samples = []
if(SAMPLE_SIZE > 1):
    # samples are signed
    if(SAMPLE_SIZE == 2):
        integer_format = '<h'
    elif(SAMPLE_SIZE == 4):
        integer_format = '<i'
    elif(SAMPLE_SIZE == 8):
        integer_format = '<q'
    else:
        exit('Supported samples sizes: 1, 2, 4, 8 bytes')
    for n in range(0, total_samples):
        value = (value + sample_unit) % (2 * math.pi)
        max_integer_value = math.pow(2,(SAMPLE_SIZE*8)-1)
        integer_value = math.floor(math.sin(value) * max_integer_value * MAX_AMPLITUDE)
        if(integer_value == max_integer_value):
            integer_value -= 1
        file.writeframes(struct.pack(integer_format, integer_value))
else:
    # samples are unsigned
    for n in range(0, total_samples):
        value = (value + sample_unit) % (2 * math.pi)
        sin_value = (math.sin(value) + 1)/2
        integer_value = math.floor(sin_value * 0xff * MAX_AMPLITUDE)
        if(integer_value == 0xff):
            integer_value -= 1
        file.writeframes(struct.pack('<B', integer_value))

file.close()