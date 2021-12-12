from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index, name = 'index'),
    path('page/<str:pk>', views.page, name = 'page'),
    path('code', views.code, name = 'code'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout')
]