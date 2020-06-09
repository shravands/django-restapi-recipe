# This file writes the data from the log file to db
import json
from collections import OrderedDict

log_file = open('../requestlogs.log', 'r')
count = 0
# Strips the newline character 
while True: 
    count += 1
    # Get next line from file 
    line = log_file.readline()   
    # if line is empty 
    # end of file is reached
    if not line: 
        break
    #print("Line{}: {}".format(count, line.strip()))
    #print('count', count)
    clean_line = line.strip()
    json_data = json.dumps(clean_line)
    dict_json = eval(json.loads(json_data))
    # adding the validators for the data
    if (dict_json['request']['full_path'] == '/favicon.ico'):
        continue
    print(dict_json['ip_address'])
    print(dict_json['request']['method'])
    print(dict_json['request']['full_path'])
    print(dict_json['user']['id'])
    print(dict_json['response']['status_code'])

log_file.close() 
