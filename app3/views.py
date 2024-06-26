from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def bottle(request):
    return HttpResponse('<h1>bottle is full of water..</h1>')
def reg(request):
    return render(request,'reg.html')