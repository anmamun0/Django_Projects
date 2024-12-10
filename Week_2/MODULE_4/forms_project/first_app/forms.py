from django import forms

from django.core import validators 



# class StudentForm(forms.Form):
#     name = forms.CharField(label="User Name")
#     email = forms.EmailField(label="User Email")
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10 :
#     #         raise forms.ValidationError("Enter a Name with at least 10 char")
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your Email must .com")
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10 :
#             raise forms.ValidationError("Enter a Name with at least 10 char")
  
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your Email must .com")
def custom_check(value):
    if len(value) <10:
        raise forms.ValidationError("Enter a value at least 10 char")
      
class StudentForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message="Enter a Name with at least 10 char")])
    email = forms.EmailField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid Email")])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"), validators.MinValueValidator(24,message="age must be at least 24")])

    file =  forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="File extension must be inded with pdf")])

    text = forms.CharField(widget=forms.TextInput,validators=[custom_check])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']

        if len(val_name) < 10:
            raise forms.ValidationError("Name must be at least 15 char!")

        if val_pass != con_pass:
            raise forms.ValidationError("Password does'nt mathch")
    

class contactForm(forms.Form):
    name = forms.CharField(label="User Name: ")
    email = forms.EmailField(label= "User Email: ")
    file = forms.FileField()

    # age = forms.IntegerField(
    #         min_value=0, 
    #         max_value=120, 
    #         label="Your Age"
    #     )

    # salary = forms.FloatField(
    #         required=True, 
    #         label="Your Salary"
    #     )

    # agree = forms.BooleanField(
    #         required=True, 
    #         label="I agree to the terms and conditions"
    #     )

    # GENDER_CHOICES = [
    #         ('M', 'Male'),
    #         ('F', 'Female'),
    #         ('O', 'Other')
    #     ]
    # gender = forms.ChoiceField(
    #     choices=GENDER_CHOICES, 
    #     required=True, 
    #     label="Gender"
    # )


    # HOBBY_CHOICES = [
    #         ('reading', 'Reading'),
    #         ('traveling', 'Traveling'),
    #         ('gaming', 'Gaming')
    #     ]
    # hobbies = forms.MultipleChoiceField(
    #     choices=HOBBY_CHOICES, 
    #     widget=forms.CheckboxSelectMultiple, 
    #     label="Your Hobbies"
    # )




    # event_date = forms.DateField(
    #         widget=forms.DateInput(attrs={'type': 'date'}), 
    #         label="Event Date"
    #     )


    # meeting_time = forms.TimeField(
    #         widget=forms.TimeInput(attrs={'type': 'time'}), 
    #         label="Meeting Time"
    #     )


    # appointment = forms.DateTimeField(
    #         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
    #         label="Appointment Date & Time"
    #     )


    # website = forms.URLField(label="Your Website")


    # file = forms.FileField(label="Upload File")



    # profile_picture = forms.ImageField(label="Upload Profile Picture")



    # username = forms.RegexField(
    #     regex=r'^[a-zA-Z0-9_]+$', 
    #     label="Username"
    # )


    # slug = forms.SlugField(label="Blog Slug")

    # settings = forms.JSONField(label="Settings JSON")





