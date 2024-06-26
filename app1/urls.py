
from django.urls import path
from app1.views import *
app_name='something'
urlpatterns = [
   
   path('hi/',hi,name='hi'),
   path('hello/',hello,name='hello')
]
