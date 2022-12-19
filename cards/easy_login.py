from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def elogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')
            return redirect('elogin')
        
        authuser = authenticate(request,username=username, password=password)
        if authuser:
            login(request, authuser)
            return redirect('books:books')
        else:
            messages.error(request, 'Incorrect password')
            return redirect('elogin')

    else:
        context = {}
        return render(request,'elogin.html',context=context)

def mylogout(request):
    logout(request)
    context = {}
    return redirect('books:books')

def eregister(request):
    if request.GET:
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:books')
        else:
            messages.error(request, 'Error registration failed')

    return render(request, 'elogin.html',{'form':form, 'page':'register'})