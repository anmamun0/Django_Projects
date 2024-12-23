- [**Contents**](#table-of-contents)
 
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






--- 
# **Table Of Contents**

|      Topic               |       Linkes                   | 
|--------------------------|--------------------------------| 
| Crispy-bootstrap5        | [Go](#crispy-bootstrap5)        |  
| Static files and photos  | [Go](#static-files-and-photos)  |  
| Backend Email Controll   | [Go](#backend-email-controll)   |   


