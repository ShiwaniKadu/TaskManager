from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status"]

    due_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
