from django import forms
from .models import Task


class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
