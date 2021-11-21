from django.shortcuts import render
from django.http import HttpResponse
from .models import people

def index(request) :
    return render(request, 'page/index.html')
    
def page(request, pk) :
    string = 'page/' + pk 
    return render(request, string)