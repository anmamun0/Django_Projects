from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title','description','assign_date','category']
        widgets = {
            'assign_date':forms.DateInput(attrs={'type':'date'})
        }
