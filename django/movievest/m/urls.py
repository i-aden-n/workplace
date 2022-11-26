from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('register', RegisterUser.as_view(), name = 'register'),
    path('login', LogUser.as_view(), name ='login'),
    path('watch/<slug:movie_slug>/season-<int:season>/serial-<int:serial>', Watch.as_view(), name='watch'),
]