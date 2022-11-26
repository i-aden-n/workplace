from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Klass, ExamTable, Marks


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phonenumber', 'balance', 'balance', 'klass','password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class KlassForm(forms.ModelForm):
    class Meta:
        model = Klass
        fields = ('name', 'level')


class ExamTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['for_klass'].empty_label = 'Klass not choosen'
    
    class Meta:
        model = ExamTable
        fields = ('for_klass', )


MarksFormset = modelformset_factory(Marks, fields = ('student', 'grammar', 'writing', 'listening', 'speaking'), extra=0)