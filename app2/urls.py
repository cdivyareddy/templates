from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('divya/',divya,name='divya'),
    path('login/',login,name='login'),
    
]