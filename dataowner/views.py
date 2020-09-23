from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from dataowner.models import DataOwner
from dataowner.forms import SignUpForm, LoginForm

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = DataOwner.objects.create_user(
                username=data.get('username'), 
                password=data.get('password'), 
                email=data.get('email'),
                display_name=data.get('display_name'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                account_type=data.get('account_type'),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, 'generic_form.html',  {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            check_user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if check_user:
                login(request, check_user)
                return HttpResponseRedirect(reverse('ownerprofile'))
                # return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
      
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))