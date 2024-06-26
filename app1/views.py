from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hi(request):
    return HttpResponse('<h1>hiiiiiiiii..........<h1>')

def hello(request):
    return render(request,'hello.html')