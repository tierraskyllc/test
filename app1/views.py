from django.shortcuts import render, redirect
from .forms import ProfileUploadForm

# Create your views here.
def profileUploadFview(request):
    # Handle profile image upload
    if request.method == 'POST':
        form = ProfileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.user = request.user
            form.save()
            return redirect('profile_upload')
    else:
        form = ProfileUploadForm()
    return render(request, 'profile_upload.html', {
        'form': form
    })
