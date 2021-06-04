from django.urls import path
from .views import ProfilePage

urlpatterns = [
    
    path('profile/', ProfilePage.as_view(), name='profile'),


    ] 