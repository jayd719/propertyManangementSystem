from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

# Create your views here.
def homepage(requests):
    data={'askForEmail': True}
    return render(requests,'homepage/main.html',data)

class Login(LoginView):
    template_name = 'registration/login.html'


def signIn(requests):
    if requests.method=="POST":
        username = requests.POST["Username"]
        password = requests.POST["password"]
        user = authenticate(requests, username=username, password=password)
        if user is not None:
            login(requests, user)
            return redirect('home-main')
            
    return render(requests,'registration/login.html')


