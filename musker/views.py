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


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk) # Soni
        #Post Form Logic
        if request.method =="POST":
            # Get current.ID
            current_user_profile =request.user.profile
            # Get form data
            action=request.POST['follow']
            #Decide to follow or unfollow
            if action =='unfollow':
                current_user_profile.fallows.remove(profile)
            elif action == 'follow':
                current_user_profile.fallows.add(profile)
            # Save the Profile
            current_user_profile.save()
        return render(request, 'profile.html', {'profile': profile})
    else:
        messages.success(request, ('you Must Be Logged in To view This '))
        return redirect('home')
