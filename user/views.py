from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User 
from django.db import IntegrityError
from django.contrib.auth import login , logout , authenticate
def index(request):
    return render(request , 'user/index.html' )

def signup(request):
    if request.method == 'GET':
        return render(request, 'user/index.html' , {'form' : UserCreationForm()})
    else :
        print(request.POST)
        if request.POST['username'] == '' :
            return render(request, 'user/index.html' , {'form' : UserCreationForm() , 'error' : 'The username sud\'nt be empty !'})
        elif request.POST['password1'] ==  '' or request.POST['password2'] == '':
            return render(request, 'user/index.html' , {'form' : UserCreationForm() , 'error' : 'The password sud\'nt be empty !'})
        elif request.POST['password1'] == request.POST['password2'] :
            try :
                user = User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main')
            except IntegrityError :
                return render(request, 'user/index.html' , {'form' : UserCreationForm() , 'error' : 'This username has ben alredy taken please , twipe another username !'})
        else :
            return render(request, 'user/index.html' , {'form' : UserCreationForm() , 'error' : 'Passwords did not math !'})
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'user/login.html' , {'form' : AuthenticationForm()})
    else :
        user = authenticate(request , username=request.POST['username'] , password=request.POST['password'])
        if user is None :
            return render(request, 'user/login.html' , {'form' : AuthenticationForm() , 'error' : 'Username and Password did not matching , Try again !'})
        login(request, user)
        return redirect('main')
