
from django.urls import path
from . import views
urlpatterns = [
    path('contact/',views.contact,name = 'contact'),
    path('form/',views.submit_form, name='submit_form'),
    path('django_form/',views.DjangoForm, name='django_form'),
    path('student_form/',views.studentForm, name ='student_form'),
    path('pass_valid/',views.PasswordValidation,name='pass_valid')
]
 