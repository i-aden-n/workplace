from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperuserTestMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        return redirect('home')


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context.update({
            'options': [
                {'url': 'manage', 'name': 'Manage'},
                {'url': 'c_movies', 'name': 'Movies'},
            ],
        })
        return context