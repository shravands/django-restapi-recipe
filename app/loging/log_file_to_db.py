# This file writes the data from the log file to db
import json

log_file = open('../requestlogs.log', 'r')
count = 0
# Strips the newline character 
while True: 
    count += 1
    # Get next line from file 
    line = log_file.readline()   
    # if line is empty 
    # end of file is reached
    if not line or count == 10: 
        break
    print("Line{}: {}".format(count, line.strip()))
    clean_line = line.strip().replace("'", '"')
    jas = json.dumps(clean_line)
    c = json.loads(jas)
    print(c)

log_file.close() 
print(count)