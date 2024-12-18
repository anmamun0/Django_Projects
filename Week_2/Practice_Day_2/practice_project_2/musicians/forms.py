from django import forms
from .models import Musician
class MusicianForm(forms.ModelForm):
    
    
    class Meta:
        model = Musician
        fields = "__all__"
        widgets = { 
            'first_name':forms.TextInput(attrs={'placeholder':"Enter Your First Name"}),
            'last_name':forms.TextInput(attrs={'placeholder':"Enter Your Last Name"}),
            'email':forms.TextInput(attrs={'placeholder':"example@gmail.com"}),
            'phone':forms.TextInput(attrs={'placeholder':"000 000 000 "}),

        }
        