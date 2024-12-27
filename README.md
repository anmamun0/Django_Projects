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
  
 ---
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


---
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

 ---
# Dynamic Media File Management

### setting.py
```
# URL to access media files in development
MEDIA_URL = '/media/'

# The directory on your server where media files are stored.
MEDIA_ROOT = BASE_DIR / 'media'
```


### url.py
```
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



### models.py
```
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')  # Files will be stored in MEDIA_ROOT/documents/
```


### forms.py 

```
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
```



### views.py

```
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_file.html', {'form': form})


def file_list(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})
```


### upload_file.html
```
<h1>Upload File</h1>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

### file_list.html
```
<h1>Uploaded Files</h1>
<ul>
    {% for document in documents %}
    <li>
        {{ document.title }} - <a href="{{ document.file.url }}">Download</a>
    </li>
    {% endfor %}
</ul>
```


 ---
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
# Decorator login_required
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
# Cookie Management

### Setting a Cookie
```
def set_cookie_view(request):
    //  response = HttpResponse("Cookie Set")

    response = render(request,'home.html')
    response.set_cookie('username', 'AN_Mamun', max_age=3600)  # Expires in 1 hour
    return response
```

### Reading a Cookie
```
def read_cookie_view(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Hello, {username}!")
```

### Deleting a Cookie
```
def delete_cookie_view(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('username')
    return response
```
```
Methods : .keys(), .values(), items(), 
```


---
# Session Management


### Session Settings : settings.py

```
SESSION_ENGINE                   : Backend to use (e.g., database, file-based, cache).
SESSION_COOKIE_NAME              : Name of the session cookie.
SESSION_COOKIE_AGE               : Expiry age of the session cookie (default: 1209600 seconds or 2 weeks).
SESSION_EXPIRE_AT_BROWSER_CLOSE  : Boolean; if True, the session expires when the browser is closed.
SESSION_SAVE_EVERY_REQUEST       : Boolean; if True, the session is saved to the database on every request.
```



### Common Session Methods : *request.session.*

```
['key']                   : Set a session value.
get('key', default=None)  : Get a session value with an optional default.
pop('key', default=None)  : Remove a session key and return its value.
clear()                   : Clears expired sessions from the database.
flush()                   : Remove the session and create a new empty session (useful for logout).
modified                  : Set this to True to force a session save.
clear_expired()           : Remove expired sessions.

set_test_cookie()	     : Sets a test cookie to check browser cookie support.
set_expiry(value)	     : Sets the session expiry time.

exists(session_key)           : Check if a session key exists.
get_session_cookie_age()      : Returns the session cookie's age in seconds.
get_expiry_date()	          : Returns the expiry date and time of the session as a datetime object.
get_expiry_age()	          : Returns the number of seconds until the session expires.
get_expire_at_browser_close()	: Returns True if the session expires when the browser closes.

test_cookie_worked()	:Return boolean , Checks if the test cookie works.
delete_test_cookie()	:Deletes the test cookie.
```




### views.py
```
last_activity = request.session.get('last_activity')
 
# Set session expiry to 1 hour (3600 seconds)

def set_session_expiry(request):
    request.session.set_expiry(3600)  # Expires after 1 hour
    return render(request, 'home.html')

--

# cookie will expire in 7 days from when the user visits the page.

def home(request):
    response = render(request,'home.html')
    // response.set_cookie('name','AN_Mamun',max_age=60)

    response.set_cookie('name','AN_Mamun',expires=datetime.utcnow()+timedelta(days=7))
    return response
```


--- 
# **Table Of Contents**

|      Topic                                |       Linkes                         | 
|-------------------------------------------|--------------------------------------| 
| Django Commands                           | [Go](#django-commands)               |  
| Crispy-bootstrap5                         | [Go](#crispy-bootstrap5)             |  
| Static files and photos                   | [Go](#static-files-and-photos)       | 
| Dynamic Media File Management             | [Go](#dynamic-media-file-management) |
| Backend Email Controll                    | [Go](#backend-email-controll)        |   
| Decorator @login_required                 | [Go](#decorator-login_required)      |   
| Cookie Management                         | [Go](#cookie-management)             |   
| Session Management                        | [Go](#session-management)            |   


