from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def profile_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profile})
    else:
        messages.success(request, 'You Must Be LoggedIn To view This Page')
        return redirect('home')
