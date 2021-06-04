from django import forms

from .models import ProfileUploadModel

class ProfileUploadForm(forms.ModelForm):
    class Meta:
        model = ProfileUploadModel
        fields = ('profileImage', 'expDate', )