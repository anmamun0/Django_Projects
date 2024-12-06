from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User Name: ")
    email = forms.EmailField(label= "User Email: ")

    age = forms.IntegerField(
            min_value=0, 
            max_value=120, 
            label="Your Age"
        )


    salary = forms.FloatField(
            required=True, 
            label="Your Salary"
        )

    agree = forms.BooleanField(
            required=True, 
            label="I agree to the terms and conditions"
        )

    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        required=True, 
        label="Gender"
    )


    HOBBY_CHOICES = [
            ('reading', 'Reading'),
            ('traveling', 'Traveling'),
            ('gaming', 'Gaming')
        ]
    hobbies = forms.MultipleChoiceField(
        choices=HOBBY_CHOICES, 
        widget=forms.CheckboxSelectMultiple, 
        label="Your Hobbies"
    )



    event_date = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}), 
            label="Event Date"
        )


    meeting_time = forms.TimeField(
            widget=forms.TimeInput(attrs={'type': 'time'}), 
            label="Meeting Time"
        )


    appointment = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
            label="Appointment Date & Time"
        )


    website = forms.URLField(label="Your Website")


    file = forms.FileField(label="Upload File")



    profile_picture = forms.ImageField(label="Upload Profile Picture")



    username = forms.RegexField(
        regex=r'^[a-zA-Z0-9_]+$', 
        label="Username"
    )


    slug = forms.SlugField(label="Blog Slug")

    settings = forms.JSONField(label="Settings JSON")