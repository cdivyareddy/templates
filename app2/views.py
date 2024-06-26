from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def divya(request):
    return HttpResponse('<h1>divyaaaaaaaaaaaaaa.....<h1>')

def login(request):
    return render(request,'login.html')