
from django.urls import path
from .views import get_google_drive_info
from . import views

urlpatterns = [
    path('get_google_drive_info/', get_google_drive_info, name='get_google_drive_info'),
    
]


