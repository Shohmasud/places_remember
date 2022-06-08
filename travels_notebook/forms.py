from django import forms
from django.core.exceptions import ValidationError

from travels_notebook.models import Places


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['slug', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class SearchForms(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }
