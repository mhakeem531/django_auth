from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpClientForm, SignUpFormOstafandy
from django.contrib.auth import authenticate, login, logout


# Create your views here.
#@login_required
def home(request):
    #if request.user.is_authenticated():
    return render(request, 'ostafandy/home.html', {'section': 'home'})


# def home_no_logging(request):
#     return render(request, 'ostafandy/home.html', {'section': 'home'})


def l_logout(request):
    # if request.method == "POST":
    logout(request)
    #return redirect('ostafandy:home_no_logging')
    return redirect('ostafandy:home')


def signup(request):
    print("*****client")
    if request.method == 'POST':
        form = SignUpClientForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = True
            user.available_now = False
            user.available_today = False
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('ostafandy:home')
    else:
        form = SignUpClientForm()
    return render(request, 'ostafandy/auth/signup.html', {'form': form})


def signup_ostafandy(request):
    print("*****ostafandy")
    if request.method == 'POST':
        form = SignUpFormOstafandy(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = False
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('ostafandy:home')
    else:
        form = SignUpFormOstafandy()
    return render(request, 'ostafandy/auth/signup-ostafandy.html', {'form': form})
