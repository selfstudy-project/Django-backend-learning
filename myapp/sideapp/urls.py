from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index, name='index'),
    path('page/<str:pk>', views.page, name='page'),
    path('cal', views.cal, name='cal'),
]