from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    details = forms.CharField(widget=forms.TextInput(),required=False)
    class Meta:
        model = Brand 
        fields = "__all__"
