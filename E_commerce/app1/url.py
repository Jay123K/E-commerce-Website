from django.urls import path
from app1.views import Home
urlpatterns = [
    path('',Home,name='')
    
]
