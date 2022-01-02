from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
import markdown

def index(request) :
    return render(request, 'page/index.html')
    
def page(request, num) :
    detail = Post.objects.filter(id = num)
    detail = detail[0]
    return render(request, 'page/code.html', {'detail' : detail})
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
            messages.info(request, 'Password not the same !')
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

def sf(request) :
    return render(request, 'page/sf.html')

def ls(request) :
    return render(request, 'page/ls.html')

def pf(request) :
    return render(request, 'page/pf.html')

def addpost(request) :

    if request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']
        content = markdown.markdown(content, extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        tags = request.POST['tags']
        author = request.POST['author']
        id = Post.objects.count() + 1
        newpost = Post.objects.create(title = title, content = content, tags = tags, author = author, id = id)
        newpost.save()
        messages.info(request, '新增成功 !')
        return redirect('addpost')
    else :
        return render(request, 'page/addpost.html')