from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .models import UserProfile
import pyrebase

config = {
    "apiKey": "AIzaSyAWDb-wpKGnexoDYLvPKHpgPurxuBzM",
    "authDomain": "shop-e05bf.firebaseapp.com",
    "databaseURL": "https://shop-e05bf-default-rtdb.firebaseio.com",
    "projectId": "shop-e05bf",
    "storageBucket": "shop-e05bf.appspot.com",
    "messagingSenderId": "1091755907124",
    "appId: ": "1091755907124:web:8dc8e3c1a322606722d261",
    "measurementId": "G-WJN803PH8X"
}


# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# database = firebase.database()


@csrf_protect
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST or None)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'lname' in request.POST:
                print('found it')
                profile.lname = request.POST['lname']
                profile.name = request.POST['username']
                profile.email = request.POST['email']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def special(request):
    return HttpResponse('You are loggod in ')


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Ваш аккаунт не активный')
        else:
            print("Это имя: {} and пароль использутеся: {}".format(username, password))
            return HttpResponse('Указаны неверные данные для входа')
    else:
        return render(request, 'index_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_udpate(request, slug):
    try:
        user = UserProfile.objects.get(name=slug)
        if request.method == 'POST':
            user.name = request.POST.get('name')
            user.lname = request.POST.get('lname')
            user.email = request.POST.get('email')
            user.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'update_user.html', {'update_profile': user})
    except UserProfile.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def profile_user(request):
    if request.user.is_active:
        profile = {'profile': UserProfile.objects.get(user_id=request.user.id)}
        return render(request, 'profile_user.html', profile)
    else:
        return HttpResponse('Ты никто')
