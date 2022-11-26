from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


menu = [
    {'url': 'home', 'name': 'home'},
    {'url': 'klassy', 'name': 'klassy'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context.update({
            'is_auth': self.request.user.is_authenticated,
            'is_super': self.request.user.is_superuser,
            'menu': menu
        })
        return context


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        return redirect('home')