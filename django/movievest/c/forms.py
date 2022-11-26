from django import forms

from m.models import *


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('serial', 'season', 'path', )
        widgets = {
            'serial': forms.NumberInput(attrs = {'class': 'field__input'}),
            'season': forms.NumberInput(attrs = {'class': 'field__input'}),
            'path': forms.FileInput(attrs = {'id': 'file_input'})
        }