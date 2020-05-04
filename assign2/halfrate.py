import math, wave, struct, sys

# read in input file
input_filename = sys.argv[1]
read = wave.open(input_filename, 'rb')
NUM_CHANNELS = read.getnchannels()
SAMPLE_SIZE = read.getsampwidth()
SAMPLE_RATE = read.getframerate()
print('input file "' + input_filename + '" found...')

# read in coeffients file
coeffs_file = open("coeffs.txt")
coeffs = []
for line in coeffs_file:
    coeffs.append(float(line))
coeffs_file.close()
print('coeffients file read...')

# determine integer format based on sample size
MAX_INTEGER = math.floor(math.pow(2,(SAMPLE_SIZE*8)-1)) - 1
MIN_INTEGER = MAX_INTEGER * -1
if(SAMPLE_SIZE == 1):
    integer_format = '<B'
    SIGNED = False
elif(SAMPLE_SIZE == 2):
    integer_format = '<h'
    SIGNED = True
elif(SAMPLE_SIZE == 4):
    integer_format = '<i'
    SIGNED = True
else:
    exit('ERROR: supported samples sizes are 1, 2, 4 bytes')
print('sample size (' + str(SAMPLE_SIZE) + ' bytes) determined...')

# store input integer values
input_data = []
data = read.readframes(1)
while(len(data) > 0):
    integer_value = int.from_bytes(data, byteorder='little', signed=SIGNED)
    input_data.append(integer_value/MAX_INTEGER)
    data = read.readframes(1)
read.close()
print('input data stored...')

# filter input data using FIR filter
filtered_data = [0]*len(coeffs)
for i in range(len(coeffs), len(input_data)):
    filter_sum = 0
    for j in range(0, len(coeffs)):
        filter_sum += (coeffs[j] * input_data[i-j])
    if(filter_sum > 1):
        filter_sum = 1
    if(filter_sum < -1):
        filter_sum = -1
    filtered_data.append(filter_sum)
print('input data filtered...')

# take every other sample
output_data = filtered_data[::2]
print('output created...')

# write out output file
output_filename = sys.argv[2]
write = wave.open(output_filename, 'wb')
write.setsampwidth(SAMPLE_SIZE)
write.setnchannels(NUM_CHANNELS)
write.setframerate(SAMPLE_RATE/2)

# output data to file
for i in output_data:
    integer_value = math.floor(i * MAX_INTEGER)
    # if(integer_value > MAX_INTEGER):
    #     integer_value = MAX_INTEGER
    # elif(integer_value < MIN_INTEGER):
    #     integer_value = MIN_INTEGER
    # print(integer_value)
    write.writeframes(struct.pack(integer_format, integer_value))
write.close()

# play samples for comparison
from play_wav import play
play(input_filename)
play(output_filename)