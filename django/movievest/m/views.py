from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import DetailView, ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .models import User, Movie, Series
from .forms import *

# Create your views here.
class Home(TemplateView):
    template_name = 'm/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Home'
        })
        return context


class LogUser(LoginView):
    form_class = AuthUser
    template_name = 'm/auth.html'


class RegisterUser(CreateView):
    form_class = CreateUser
    template_name = 'm/auth.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Watch(DetailView):
    model = Series
    template_name = 'm/player.html'
    context_object_name = 'series'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': context['series'].movie.name
        })
        return context
    
    def get_object(self):
        return Series.objects.get(movie__slug = self.kwargs['movie_slug'], season = self.kwargs['season'], serial = self.kwargs['serial'])