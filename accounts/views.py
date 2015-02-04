from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from .forms import LoginForm, RegistrationForm

class IndexView(generic.View):
    template_name = 'base.html'

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)
    # Proverka danuh formu na oshibki
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #proverka sovpadaet li username i password
        user = authenticate(username=username, password=password)
        login(request, user)

    context = {'form': form}
    return render(request, 'form.html', context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    # Proverka danuh formu na oshibki
    if form.is_valid():
        #sohranenie danuh v bazu
        new_user = form.save(commit=False)
        new_user.save()

    context = {'form': form}
    return render(request, 'form.html', context)