from django.db import models
from django.conf import settings



def user_directory_path(instance, filename):
    return 'user: {0}/{1}'.format(instance.user, filename)




class ProfileUploadModel(models.Model):
    profileImage = models.ImageField(upload_to=user_directory_path, null=True)
    expDate = models.DateField(verbose_name='Exp Date', blank=True, null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)