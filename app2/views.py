from app2.models import Profile
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile
from app1.models import ProfileUploadModel

# Create your views here.

class ProfilePage(TemplateView):
    model = Profile
    template_name = 'profile.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_img"] = ProfileUploadModel.objects.get()
        return context

