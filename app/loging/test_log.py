import json
from collections import OrderedDict

data = '{"action_name": None, "execution_time": "00:00:00.000915", "timestamp": "2020-06-09T03:42:21.299294Z", "ip_address": None, "request": OrderedDict([("method", "GET"), ("full_path", "ggggg"), ("data", None), ("query_params", "{}")]), "response": OrderedDict([("status_code", 404), ("data", None)]), "user": OrderedDict([("id", None), ("username", None)])}'

json_data = json.dumps(data, sort_keys=True, indent=4)
dict_json = eval(json.loads(json_data))
print(dict_json['request'])
