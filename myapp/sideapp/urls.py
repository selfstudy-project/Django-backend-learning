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
    path('page/register', views.pregister, name = 'pregister'),
    path('page/login', views.plogin, name = 'plogin'),
    path('page/logout', views.plogout, name = 'plogout'),
    path('page/index', views.pindex, name = 'pindex'),
    path('page/ls', views.pls, name = 'pls'),
    path('page/pf', views.ppf, name = 'ppf'),
    path('page/sf', views.psf, name = 'psf'),
    path('page/addpost', views.paddpost, name = 'paddpost'),
]