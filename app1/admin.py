from django.contrib import admin
from .models import ProfileUploadModel
# Register your models here.
class ProfileUploadModelAdmin(admin.ModelAdmin):
    list_display = ['profileImage', 'expDate']

admin.site.register(ProfileUploadModel, ProfileUploadModelAdmin)