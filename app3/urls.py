from django.urls import path
from app3.views import *
app_name='something'
urlpatterns=[
    path('bottle/',bottle,name='bottle'),
    path('reg/',reg,name='reg'),
]