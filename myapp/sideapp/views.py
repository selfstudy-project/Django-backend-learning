from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Code
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request) :
    code1 = Code()
    code1.code = '#include <bits/stdc++.h>'
    code1.name = 'first c++ code'
    return render(request, 'page/index.html', {'feature' : code1})
    
def page(request, pk) :
    string = 'page/' + pk 
    return render(request, string)

def code(request) :
    allcodes = Code.objects.all()
    return render(request, 'page/code.html', {'allcodes' : allcodes})

def register(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        _password = request.POST['_password']
        if password == _password :
            if User.objects.filter(email = email).exists() :
                messages.info(request, 'Email already exists !')
                return redirect('register')
            elif User.objects.filter(username=username).exists() :
                messages.info(request, 'Username already exists !')
                return redirect('register')
            else :
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')
        else :
            messages.info('Password not the same !')
            return redirect('register')
    return render(request, 'page/register.html')

def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None :
            auth.login(request, user)
            return redirect('index')
        else :
            messages.info(request, 'Wrong username or password')
            return redirect('login')


    return render(request, 'page/login.html')

def logout(request) :
    auth.logout(request)
    return redirect('index')