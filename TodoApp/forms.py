from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Add task here...', 'autocomplete':'off'}))
    class Meta:
        model = Task
        fields = ['content']

class UpdateTaskForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Edit task here...', 'autocomplete':'off'}))
    class Meta:
        model = Task
        fields = '__all__'

