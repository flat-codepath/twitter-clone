from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Meep
from django.contrib import messages
from .forms import MeepForm, SigninForm, UpdateUser, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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


def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password1']
            print(password)
            form.save(commit=True)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                message = messages.success(request, 'SuccessFully Created Signin')
                return redirect('home')
            else:
                error = messages.error(request, "There is Problem Try again ...")
                redirect('signin')
        else:
            error = messages.error(request, form.errors)
    return render(request, 'signin.html', {'form': form})


# Update Profile
def update_user(request):
    if request.user.is_authenticated:
        profile_user = Profile.objects.get(user__id=request.user.id)

        if request.method == "POST":

            form = UpdateUser(request.POST, instance=request.user)
            profile_form = ProfilePicForm(request.POST, request.FILES, instance=profile_user)

            # print(profile_form.cleaned_data['profile_image'])
            if form.is_valid() and profile_form.is_valid():
                form.save()
                profile_form.save()

                messages.success(request, "Your Profile has been updated")
                return redirect('home')
            else:
                messages.error(request, form.errors)
                return redirect('update_user')
        else:
            form = UpdateUser(instance=request.user)
            profile_form = ProfilePicForm(instance=profile_user)
            return render(request, 'updateProfile.html', {'form': form, 'profile_form': profile_form})
    else:
        messages.error(request, "You Must Be Logged in to Update")
        return redirect('home')


def meep_like(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)
        if meep.likes.filter(id=request.user.id):
            meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged in to Update")
        return redirect('home')


def meep_show(request, pk):
    meep = get_object_or_404(Meep, id=pk)
    if meep:
        return render(request, 'show_meep.html', {'meep': meep})
    else:
        messages.error(request, "that Meep Does not existing")
        return redirect('home')


def unfollow(request,pk):
    if request.user.is_authenticated:
        #Get the profile to unfallow
        profile=Profile.objects.get(user_id=pk)
        #unfallow the user
        request.user.profile.fallows.remove(profile)
        #save our profile
        request.user.profile.save()
        messages.success(request,f"you have succesfully unfallowed {profile.user.username}")
        return redirect('home')
    else:
        messages.success(request,"You Must Be logged in to do this")
        return redirect('home')

def follow(request,pk):
    if request.user.is_authenticated:
        profile= Profile.objects.get(user_id=pk)
        request.user.profile.fallows.add(profile)
        request.user.profile.save()

        messages.success(request,f"You Have Successfully  follwed{profile.user.username}")
        return redirect('home')
    else:
        messages.success(request,"You Must Be logged in to do this")
        return redirect('home')

def followers(request,pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles=Profile.objects.get(user_id=pk)
            return  render(request,'followers.html',{'profiles': profiles})
        else:
            messages.success(request,("That Not your Profile Page"))
            return redirect('home')
    else:
        messages.success(request, 'You Must Be LoggedIn To view This Page')
        return redirect('home')
