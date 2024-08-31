import json
import time
target_file = '/home/developer/kafka/sinkFiles/tarFile.log'

# Print the data on file
with open(target_file) as f:
    print(f.read())