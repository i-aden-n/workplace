from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *


class AuthUser(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2',)