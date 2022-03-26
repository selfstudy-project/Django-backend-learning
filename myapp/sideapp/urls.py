from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('page/<int:num>', views.page, name = 'page'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('index', views.index, name = 'index'),
    path('ls', views.ls, name = 'ls'),
    path('pf', views.pf, name = 'pf'),
    path('sf', views.sf, name = 'sf'),
    path('addpost', views.addpost, name = 'addpost'),
    path('post/<str:s>', views.post, name = 'post'),
    path('log_in', views.log_in, name = 'log_in'),
    path('account', views.account, name = 'account'),
    path('_register', views._register, name = '_register')
]