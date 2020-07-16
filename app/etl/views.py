from django.http import JsonResponse

from etl.log_file_to_db import log_db_run

from core.models import ConfigData #object which contains all the config values
from rest_framework.exceptions import NotFound

import requests
import json


def import_logs(self):
    """Authenticate user and import the logs from log file to database"""
    cread_id = int(self.GET.get('id'))
    #cread_id = 10
    if cread_id == 66:
        log_run = log_db_run(66)
        return JsonResponse({"msg": "The process has been completed successfully",
                             "logs_imported": log_run})
    else:
        return JsonResponse({"msg": "The process is not validated"})


def get_crypto_data(self):
    """Getting the data from the crypto api"""
    # Below configurations were done to get the data from cryptocompare api
    #https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=50
    #https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=INR&limit=50
    config_name = "cryptocompare"
    fsym = self.GET.get('fsym')
    tsym = self.GET.get('tsym')
    limit = self.GET.get('limit')
    api_key = ConfigData.objects.get(config_name=config_name).config_value
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    params = {'fsym': fsym, 'tsym': tsym, 'limit' : int(limit), 'api_key' : api_key}
    r = requests.get(url, params = params)
    return JsonResponse({"the api key for this is": api_key,
                         "the_data_is": r.json()['Data']['Data'],
                         "status_code": r.status_code})
