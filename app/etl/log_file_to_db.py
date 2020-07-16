# This file writes the data from the log file to db
from core.models import RequestLogs
import json
from collections import OrderedDict

def log_db_run(abc):
    """writing the logs to db function"""
    log_file = open('./requestlogs.log', 'r+')
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
        if dict_json['ip_address'] is None:
            dict_json['ip_address'] = 'ip not found'

        if dict_json['user']['id'] is None:
            dict_json['user']['id'] = 00

        log_line = RequestLogs(ip_address=dict_json['ip_address'], user_id=dict_json['user']['id'],
                               method_type=dict_json['request']['method'], request_path=dict_json['request']['full_path'],
                               response_code=dict_json['response']['status_code'])
        log_line.save()
    #erasing the data from the file which has been written into the db
    log_file.truncate(0)
    log_file.close()
    return count 

