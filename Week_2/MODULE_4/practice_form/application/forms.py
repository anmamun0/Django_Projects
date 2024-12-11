from django import forms
from django.core import validators 

class Application_Form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name',}),label='First Name') 
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Last name',}),label='Last Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ex: example@gmail.com',}),label='E-mail')

    phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '000 0000 000 ',}),label="Phone Number")

    SELECT_POSSITION = [
        ('','Select Option'),
        ('SE','Software Engineer'),
        ('BC','Block Chain'),
        ('DS','Data Science'),
    ]
    possition = forms.ChoiceField(choices=SELECT_POSSITION,label='What position are you applying for?')

     
    job_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),label="Available start date"
    ) 


    SELECT_SATUS = [
        ('employed','Employed'),
        ('selfemployed','Self-Employeed'),
        ('unemployed','Unemployeed'),
        ('student','Student'), 
    ]
    employee_status = forms.ChoiceField(choices=SELECT_SATUS,widget=forms.RadioSelect , label="What is your Current employment status?")

    SELECT_RESUME = [
        ('file','Uploadd File'),
        ('url','Provide URL'), 
    ]
    submit_resume_type = forms.ChoiceField(choices=SELECT_SATUS,widget=forms.RadioSelect , label="How do you prefer to submit your resume?")

    cv = forms.FileField(label="Upload Your CV",validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="should it pdf file")])
 


