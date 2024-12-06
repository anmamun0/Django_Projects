from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User Name: ")
    email = forms.EmailField(label= "User Email: ")