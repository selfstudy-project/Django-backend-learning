from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
import markdown
from purifier.purifier import HTMLPurifier

purifier = HTMLPurifier({
'div': ['*'], 
'span': ['*'], 
'h1': ['*'],
'h2': ['*'],
'h3': ['*'],
'h4': ['*'],
'h5': ['*'],
'h6': ['*'],
'br': ['*'],
'b': ['*'],
'i': ['*'],
'strong': ['*'],
'em': ['*'],
'a': ['*'],
'pre': ['*'],
'code': ['*'],
'img': ['*'],
'tt': ['*'],
'div': ['*'],
'ins': ['*'],
'del': ['*'],
'sup': ['*'],
'sub': ['*'],
'p': ['*'],
'ol': ['*'],
'ul': ['*'],
'table': ['*'],
'thead': ['*'],
'tbody': ['*'],
'tfoot': ['*'],
'blockquote': ['*'],
'dl': ['*'],
'dt': ['*'],
'dd': ['*'],
'kbd': ['*'],
'q': ['*'],
'samp': ['*'],
'var': ['*'],
'hr': ['*'],
'li': ['*'],
'tr': ['*'],
'td': ['*'],
'th': ['*'],
's': ['*'],
'strike': ['*'],
})

def index(request) :
    return render(request, 'index.html')

    
def page(request, num) :
    detail = Post.objects.filter(id = num)
    detail = detail[0]
    detail.content = markdown.markdown(detail.content , extensions = [
        'extra',
        'codehilite',
        'nl2br',
        'tables',
        'admonition',
        'legacy_em',
        'smarty',
        'sane_lists',
    ])
    detail.content = purifier.feed(detail.content)
    return render(request, 'code.html', {'detail' : detail})
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
            elif len(password) < 8:
                messages.info(request, 'Password should be at least 8 characters')
            else :
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')
        else :
            messages.info(request, 'Password not the same !')
            return redirect('register')
    return render(request, 'register.html')

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
    return render(request, 'login.html')

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
    return redirect('index')

def change_pw(request) :
    if request.method == 'POST' :
        oripw = request.POST['oripw']
        npw = request.POST['npw']
        _npw = request.POST['_npw']
        user = request.user
        username = user.username
        if(len(npw) < 8 or len(_npw) < 8 or len(oripw) < 8):
            messages.info(request, 'Password should be at least 8 characters')
            return redirect('account')
        elif (user.check_password(oripw)):
            if(npw == _npw):
                user.set_password(npw)
                user.save()
                user = auth.authenticate(username = username, password = npw)
                auth.login(request, user)
                return redirect('index')
            else:
                messages.info(request, '新密碼不相同')
                return redirect('account')
        else :
            messages.info(request, '原始密碼不正確')
            return redirect('account')
    return redirect('index')
def sf(request) :
    return render(request, 'sf.html')

def ls(request) :
    posts = Post.objects.all()
    return render(request, 'ls.html', {'posts' : posts})

def pf(request) :
    return render(request, 'pf.html')

def addpost(request) :
    if request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']
        tags = request.POST['tags']
        author = request.POST['author']
        newpost = Post.objects.create(title = title, content = content, tags = tags, author = author)
        newpost.save()
        messages.info(request, '新增成功 !')
        return redirect('addpost')
    else :
        return render(request, 'addpost.html')

def post(request, s) :
    problem = Post.objects.filter(tags = s)
    return render(request, 'post.html', {'problem' : problem})

def edit_post(request, num):
    detail = Post.objects.filter(id = num)
    detail = detail[0]
    return render(request, 'edit.html', {'detail': detail})

def edit(request, num):
    detail = Post.objects.get(id = num)
    detail.title = request.POST['title']
    detail.content = request.POST['content']
    detail.tags = request.POST['tags']
    detail.author = request.POST['author']
    detail.save()
    return redirect(f'/page/{num}')
def log_in(request) :
    return render(request, 'login.html')
def account(request) :
    return render(request, 'account.html')
def _register(request) :
    return render(request, 'register.html')
