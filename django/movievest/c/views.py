from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, TemplateView, ListView, UpdateView
from django.db.models import Count

from .forms import SeriesForm
from .utils import SuperuserTestMixin, DataMixin
from m.models import Movie, Series

# Create your views here.
class Manage(DataMixin, SuperuserTestMixin ,TemplateView):
    template_name = 'c/manage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(
            title = 'Manage'
        ))
        return context

class AddSerial(DataMixin, SuperuserTestMixin, CreateView):
    form_class = SeriesForm
    template_name = 'c/series_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(
            title = 'Add Serial'
        ))
        return context

    def form_valid(self, form):
        serial = form.save(commit=False)
        serial.movie = Movie.objects.get(slug = self.kwargs['movie_slug'])
        serial.save()
        return redirect(reverse('c_movie', kwargs={'movie_slug': self.kwargs['movie_slug']}))


class Movies(DataMixin, SuperuserTestMixin, ListView):
    model = Movie
    template_name = 'c/movies.html'
    context_object_name = 'movies'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(
            title = 'Movies'
        ))
        return context


class ShowMovie(DataMixin, SuperuserTestMixin, ListView):
    model = Series
    template_name = 'c/movie.html'
    context_object_name = 'series'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(
            title = context['series'][0][0].movie.name
        ))
        return context

    def get_queryset(self):
        return [Series.objects.filter(movie__slug = self.kwargs['movie_slug'], season = s['season']) for s in Series.objects.values('season').annotate(s_count = Count('season'))]


class EditSerial(DataMixin, SuperuserTestMixin, UpdateView):
    template_name = 'c/series_form.html'
    form_class = SeriesForm
    context_object_name = 'movie'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(
            title = 'edit'
        ))
        return context
    
    def get_object(self):
        return Series.objects.get(movie__slug = self.kwargs['movie_slug'], season = self.kwargs['season'], serial = self.kwargs['serial'])

    def form_valid(self, form):
        form.save()
        return redirect(reverse('c_movie', kwargs={'movie_slug': self.kwargs['movie_slug']}))