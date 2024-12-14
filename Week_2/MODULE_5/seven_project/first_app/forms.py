from django import forms

from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll']
        # exclude = ['roll']

        # labels = {
        #     'name':'Student Name',
        #     'roll':'Roll No'
        # }
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'bg-primary'}),
        #     # 'roll':forms.PasswordInput()
        # }
        # help_texts = {
        #     'name':'Write your Full Name.',
        # }
        # error_messages = {
        #     'name':{'required':"Your Name is required"}
        # }

