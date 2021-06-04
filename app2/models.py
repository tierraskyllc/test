from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    firstName = models.CharField(max_length=32, blank=True, verbose_name='First Name')
    
    lastName = models.CharField(max_length=32, blank=True, verbose_name='Last Name')

    

