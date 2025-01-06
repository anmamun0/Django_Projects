from django import forms 
from .models import StudentProfile
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class RegistraionForm(UserCreationForm):
    registration_id = forms.CharField(max_length=20)
    roll = forms.CharField(max_length=10)
    department = forms.CharField(max_length=100)
    session = forms.CharField(max_length=20) 

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','registration_id','roll','department','session', 'password1', 'password2', ]
    
    def save(self,commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
 
            registration_id = self.cleaned_data.get('registration_id')
            roll = self.cleaned_data.get('roll')
            department = self.cleaned_data.get('department')
            session = self.cleaned_data.get('session') 

            StudentProfile.objects.create(
                user = our_user,
                registration_id = registration_id,
                roll = roll,
                department = department,
                session = session,
            )
        return our_user
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })



