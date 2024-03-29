from django import forms
from .models import Task

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
