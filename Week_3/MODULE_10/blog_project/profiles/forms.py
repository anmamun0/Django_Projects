from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms 

class ProfileForm(UserChangeForm):
    password  = None

    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.Select(attrs={
            'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500',
        }),
        required=False,
    )
    location = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your location'
        }),
        required=False,
    )
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'YYYY-MM-DD',
            'type': 'date'
        }),
        required=False,
    )
    summary = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter a short summary about yourself',
        }),
        required=False,
    )
    website = forms.URLField(
        widget=forms.URLInput(attrs={
            'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Enter your website URL',
        }),
        required=False,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'location', 'birthday', 'summary', 'website', ]
