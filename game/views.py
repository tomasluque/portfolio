import random
import json

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'game/home.html')
def test(request):
    return render(request, 'game/test.html')