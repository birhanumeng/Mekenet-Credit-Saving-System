from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from .forms import CustomUserCreationForm



def searchProfile(request):
    """ Create a users profile page """
    #f request.method == 'GET':
        #username = request.GET.get('username')
    #profile = Profile.objects.get(username=username)
    #context ={'profile': profile}
    return render(request, 'users/search_profile.html')


def userProfile(request):
    """ Create a single user profile page """
    #profile = Profile.objects.get(username=key)
    #username = request.POST['username']
    #user = Profile.objects.get(username=username)
    username = ''
    if request.GET.get('username'):
        username = request.GET.get('username')
    
    profile = Profile.objects.get(username=username)
    context ={'profile': profile}
    return render(request, 'users/user_profile.html', context)


def userRegister(request):
    """ User creation form """
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User is successfully created')
        else:
            messages.error(request, 'an error has occurred during registration')
    
    context = {'form': form}
    return render(request, 'users/user_register.html', context)



def loginUser(request):
    """ Create users login page """
    if request.user.is_authenticated:
        return redirect('customers')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username or password is incorrect')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('customers')
        else:
            messages.error(request,'Username or password is incorrect')

    return render(request, 'users/login_user.html')


def logoutUser(request):
    """ Logout a user """
    logout(request)
    messages.info(request,'User is successfully logout')
    return redirect('login')
