from django.http import JsonResponse

from etl.log_file_to_db import log_db_run

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
