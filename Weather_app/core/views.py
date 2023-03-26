from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import City


# Create your views here.
def home(request):
    return render(request, 'home.html')

def info(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
    return render(request, 'info.html')