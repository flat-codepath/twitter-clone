from django.shortcuts import render, redirect
from .models import Profile, Meep
from django.contrib import messages
from .forms import MeepForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                return redirect('home')
        meeps = Meep.objects.all().order_by('-id')
        return render(request, 'home.html', {'meeps': meeps, 'form': form})
    else:
        meeps = Meep.objects.all()
        return render(request, 'home.html', {'meeps': meeps})


def profile_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profile})
    else:
        messages.success(request, 'You Must Be LoggedIn To view This Page')
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)  # Soni

        meeps = Meep.objects.filter(user_id=pk)

        # Post Form Logic
        if request.method == "POST":
            # Get current.ID
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.fallows.remove(profile)
            elif action == 'follow':
                current_user_profile.fallows.add(profile)
            # Save the Profile
            current_user_profile.save()
        return render(request, 'profile.html', {'profile': profile, 'meeps': meeps})
    else:
        messages.success(request, ('you Must Be Logged in To view This '))
        return redirect('home')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            success = messages.success(request, 'You have Been Logged In Successfully')
            return redirect('home')
        else:
            error = messages.error(request, 'Some Thing went Wrong Please Try Again after Sometime')
    return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    success = messages.success(request, 'You are Logged Out... Now')
    return redirect('home')
