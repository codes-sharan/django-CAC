# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_view(request):
    # Ensure the user has a profile, or create one if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile_view.html', {'profile': profile})

@login_required
def profile_edit(request):
    # Ensure the user has a profile, or create one if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Ensure 'profile_view' is a valid URL name
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'form': form})
