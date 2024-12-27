- [**Contents**](#table-of-contents)

# Django Commands

This section lists commonly used commands when working with Django projects.


```
--
1. Create a Django Project 
     $ django-admin startproject project_1

2. Create a Django App
     $ django-admin app first_app

3. Run the Django Development Server 
     $ python manage.py runserver

4. Convert Python Models to SQL Schema 
     $ python manage.py makemigrations

5. Apply Migrations to the Database
     $ python manage.py migrate

6. Create Admin
     $ python manage.py createsuperuser
--
```
 
 
 
 
# Crispy-bootstrap5 
*Bootstrap5 template pack for django-crispy-forms* [Go](https://github.com/django-crispy-forms/crispy-bootstrap5/) 


####  Installation  
```
$ pip install crispy-bootstrap5
```
#### *setting.py*
```
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
    ...
)
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```
#### templates | *home.html*
```
{% load crispy_forms_tags %}
{%  form | crispy %}
```



# Static files and photos
*Used to configure how Django handles static files like CSS, JavaScript, and images.* 

####  setting.py  
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR/'static',
]
```

####  *home.html*
```
{% load static %}
<src href="{% static 'photo.png' %}">
```

# Backend Email Controll

#### *setting.py* 
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # For Gmail
EMAIL_PORT = 587
EMAIL_HOST_USER = 'anmamun0@gmail.com'
EMAIL_HOST_PASSWORD = 'xdsb--appPassword--wxqaeh'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```




# Decorator @login_required
*is used to ensure that a view can only be accessed by authenticated (logged-in) users. If a user is not logged in and tries to access a view that is decorated with @login_required, they are redirected to the login page.* 

####  setting.py  
```
LOGIN_URL = '/user/login/'
```

####  *view.html*
```
from django.contrib.auth.decorators import login_required
@login_required(login_url='/user/login/')
@login_required
```

--- 
# **Table Of Contents**

|      Topic                 |       Linkes                         | 
|----------------------------|--------------------------------------| 
| Django Commands            | [Go](#django-commands)               |  
| Crispy-bootstrap5          | [Go](#crispy-bootstrap5)             |  
| Static files and photos    | [Go](#static-files-and-photos)       |  
| Backend Email Controll     | [Go](#backend-email-controll)        |   
| Decorator @login_required  | [Go](#decorator-@login-required)     |   


