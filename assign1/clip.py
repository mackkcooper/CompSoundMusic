import math, wave, struct

read = wave.open('sin.wav', 'rb')
MAX_AMPLITUDE = .9
NUM_CHANNELS = read.getnchannels()
SAMPLE_SIZE = read.getsampwidth()
SAMPLE_RATE = read.getframerate()

write = wave.open('clipped.wav', 'wb')
write.setsampwidth(SAMPLE_SIZE)
write.setnchannels(NUM_CHANNELS)
write.setframerate(SAMPLE_RATE)

if(SAMPLE_SIZE == 1):
    integer_format = '<B'
elif(SAMPLE_SIZE == 2):
    integer_format = '<h'
elif(SAMPLE_SIZE == 4):
    integer_format = '<i'
else:
    exit('ERROR: supported samples sizes are 1, 2, 4 bytes')

if(SAMPLE_SIZE == 1):
    offset = math.floor(128 * MAX_AMPLITUDE)
    MAX_INTEGER = 128 + offset
    MIN_INTEGER = 128 - offset
    SIGNED = False
else:
    MAX_INTEGER = math.floor(math.pow(2,(SAMPLE_SIZE*8)-1) * MAX_AMPLITUDE)
    MIN_INTEGER = MAX_INTEGER * -1
    SIGNED = True

data = read.readframes(1)
while(len(data) > 0):
    integer_value = int.from_bytes(data, byteorder='little', signed=SIGNED)
    if(integer_value > MAX_INTEGER):
        integer_value = MAX_INTEGER
    elif(integer_value < MIN_INTEGER):
        integer_value = MIN_INTEGER
    data = struct.pack(integer_format, integer_value)
    write.writeframes(data)
    data = read.readframes(1)

read.close()
write.close()

print("clipped.wav created")