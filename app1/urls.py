from django.urls import path
from .views import profileUploadFview

urlpatterns = [
    
    path('', profileUploadFview, name='profile_upload'),



    ] 