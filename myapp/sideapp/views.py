from django.shortcuts import render
from django.http import HttpResponse
from .models import Code

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
    if request.method == 'POST'
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        _password = request.POST['_password']
        if password == _password :

    return render(request, 'page/register.html')