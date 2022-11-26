from django.urls import path

from .views import *


urlpatterns = [
    path('', Manage.as_view(), name='manage'),
    path('movies/', Movies.as_view(), name = 'c_movies'),
    path('<slug:movie_slug>', ShowMovie.as_view(), name = 'c_movie'),
    path('<slug:movie_slug>/add', AddSerial.as_view(), name = 'add_serial'),
    path('<slug:movie_slug>/season-<int:season>/serial-<int:serial>/edit', EditSerial.as_view(), name = 'edit_serial')
]