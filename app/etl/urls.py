from django.urls import path

from etl import views


app_name = 'etl'

urlpatterns = [
    path('logwritedb/', views.import_logs, name='logwritedb'),
]
