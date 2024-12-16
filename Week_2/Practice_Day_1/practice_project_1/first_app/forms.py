from django import forms
from django.forms.widgets import NumberInput

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=200)
    email = forms.EmailField()

class DjangoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField() 
  
    # first_name = forms.CharField(max_length = 200) 
    # last_name = forms.CharField(max_length = 200) 
    # roll_number = forms.IntegerField( 
    #                  help_text = "Enter 6 digit roll number"
    #                  ) 
    # password = forms.CharField(widget = forms.PasswordInput())
	# comment = forms.CharField(widget=forms.Textarea)

    # email = forms.EmailField()

    # agree = forms.BooleanField()

    # date = forms.DateField()

    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982'] 
    
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    # value = forms.DecimalField()

    # email_address = forms.EmailField(label="Please enter your email address",)

    # first_name = forms.CharField(initial='Your name')

    # agree = forms.BooleanField(initial=True)

#     FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]
 
#     favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)


    # FAVORITE_COLORS_CHOICES = [
    #     ('blue', 'Blue'),
    #     ('green', 'Green'),
    #     ('black', 'Black'),
    # ]

    # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    # FAVORITE_COLORS_CHOICES = [
    # ('blue', 'Blue'),
    # ('green', 'Green'),
    # ('black', 'Black'),
    # ]

    # favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
 



