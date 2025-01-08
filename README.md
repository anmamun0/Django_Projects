- [**Contents**](#table-of-contents)

## Django Commands

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
## Crispy-bootstrap5 
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
## Static files and photos
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
## Dynamic Media File Management

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
## Backend Email Controll

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
## Cookie Management

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
## Session Management


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
### Class Base View (CBv) 
*[Copyed](https://ccbv.co.uk/)*

```
django.contrib.auth.views import Auth-Views
django.views.generic import Generic-Base, Edit, Details, List, Dates
```

| *Auth Views* [?](#auth-views)| *Generic base* [?](#generic-base)| *Generic edit* [?](#generic-edit)| *Generic detail* [?](#generic-detail)| *Generic list* [?](#generic-list)| *Generic dates* [?](#generic-dates) | 
|---------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|   
| LoginView                 | RedirectView                 | CreateView                   | DetailView                   | ListView                     | ArchiveIndexView             | 
| PasswordChangeDoneView    | TemplateView                 | DeleteView                   |                              |                              | DateDetailView               | 
| PasswordChangeView        | View                         | FormView                     |                              |                              |  DayArchiveView              | 
| PasswordResetCompleteView |                              | UpdateView                   |                              |                              | MonthArchiveView             | 
| PasswordResetConfirmView  |                              |                              |                              |                              | TodayArchiveView             | 
| PasswordResetDoneView     |                              |                              |                              |                              | WeekArchiveView              | 
| PasswordResetView         |                              |                              |                              |                              | YearArchiveView              |  


 
 ### Auth Views
[-](#class-base-view-cbv)   
<h5>1. LoginView</h5>
<h6>
  <b>Purpose:</b> Handles user login. <br>
  <b>When to Use:</b> <br>
  • To render a login form and authenticate users. <br>
  • To log users in and redirect them to a specified page. <br>
  • <b>Attributes:</b> <code>template_name</code>, <code>redirect_authenticated_user</code>, <code>authentication_form</code>, <code>next_page</code>, <code>get_success_url()</code> <br>
</h6>

<h5>2. LogoutView</h5>
<h6>
  <b>Purpose:</b> Logs out the user and redirects them to a specified page. <br>
  <b>When to Use:</b> <br>
  • To log users out. <br>
  • To clear session data. <br>
  • <b>Attributes:</b> <code>next_page</code>, <code>template_name</code>, <code>get_next_page()</code> <br>
</h6>

<h5>3. PasswordChangeView</h5>
<h6>
  <b>Purpose:</b> Allows authenticated users to change their password. <br>
  <b>When to Use:</b> <br>
  • To let logged-in users update their passwords. <br>
  • <b>Attributes:</b> <code>template_name</code>, <code>form_class</code>, <code>success_url</code>, <code>get_success_url()</code> <br>
</h6>

<h5>4. PasswordChangeDoneView</h5>
<h6>
  <b>Purpose:</b> Confirms that the password has been changed successfully. <br>
  <b>When to Use:</b> <br>
  • To show a success message after the password is changed. <br>
  • <b>Attributes:</b> <code>template_name</code> <br>
</h6>

<h5>5. PasswordResetView</h5>
<h6>
  <b>Purpose:</b> Allows users to request a password reset via email. <br>
  <b>When to Use:</b> <br>
  • To initiate the password reset process. <br>
  • Sends an email to the user with a reset link. <br>
  • <b>Attributes:</b> <code>template_name</code>, <code>email_template_name</code>, <code>subject_template_name</code>, <code>form_class</code>, <code>success_url</code>, <code>get_success_url()</code> <br>
</h6>

<h5>6. PasswordResetDoneView</h5>
<h6>
  <b>Purpose:</b> Displays a confirmation that the password reset email was sent. <br>
  <b>When to Use:</b> <br>
  • After a user requests a password reset. <br>
  • <b>Attributes:</b> <code>template_name</code> <br>
</h6>

<h5>7. PasswordResetConfirmView</h5>
<h6>
  <b>Purpose:</b> Allows users to set a new password using a reset link. <br>
  <b>When to Use:</b> <br>
  • After the user clicks the link in the password reset email. <br>
  • <b>Attributes:</b> <code>template_name</code>, <code>form_class</code>, <code>success_url</code>, <code>get_success_url()</code> <br>
</h6>

<h5>8. PasswordResetCompleteView</h5>
<h6>
  <b>Purpose:</b> Confirms that the password reset process is complete. <br>
  <b>When to Use:</b> <br>
  • After a user successfully resets their password. <br>
  • <b>Attributes:</b> <code>template_name</code> <br>
</h6>

<h5>9. LogoutThenLoginView (Optional)</h5>
<h6>
  <b>Purpose:</b> Logs out the user and redirects them to the login page. <br>
  <b>When to Use:</b> <br>
  • To provide "logout and redirect to login" functionality in one step. <br>
  • <b>Attributes:</b> <code>template_name</code>, <code>next_page</code>, <code>get_redirect_url()</code> <br>
</h6>



---
### Generic Base
[-](#class-base-view-cbv)   
<h5>1. View</h5>
<h6>
  <b>Purpose:</b> Base class for all views. It doesn't perform any specific actions by itself but provides a foundation for building views. <br>
  <b>When to Use:</b> <br>
  • When you need full control over logic. <br>
  • It is the most customizable option for creating views. <br>
  • Use it when you want to define your own logic for handling requests and responses. <br>
  • It provides hooks like <code>dispatch()</code>, <code>get()</code>, <code>post()</code> for handling HTTP methods. <br> 
</h6>

<h5>2. TemplateView</h5>
<h6>
  <b>Purpose:</b> Render a template. <br>
  <b>When to Use:</b> <br>
  • For static or minimally dynamic pages. <br>
  • Simplifies rendering templates without requiring custom logic. <br>
  • Use it when your view needs only to serve static data or simple dynamic content using templates. <br>
  <b>Attributes:</b> <code>template_name</code>, <code>get_context_data()</code>
</h6>

<h5>3. RedirectView</h5>
<h6>
  <b>Purpose:</b> Perform HTTP redirects. <br>
  <b>When to Use:</b> <br>
  • To redirect users to another URL. <br>
  • Use it when you want to redirect users to another URL (either static or dynamic). <br>
  • Handles permanent (<code>301</code>) and temporary (<code>302</code>) redirects. <br>
  <b>Attributes:</b> <code>url</code>, <code>pattern_name</code>, <code>permanent</code>
</h6>





---
### Generic Edit
[-](#class-base-view-cbv)   
<h5>1. CreateView</h5>
<h6>
  <b>Purpose:</b> Handles the creation of new objects in the database. <br>
  <b>When to Use:</b> <br>
  • When you want to display a form for creating an object. <br>
  • Automatically saves valid form data to the database. <br>
  • Simplifies object creation with default implementation. <br>
  <b>Attributes:</b> <code>template_name</code>, <code>form_class</code>, <code>model</code>, <code>fields</code>, <code>success_url</code>, <code>get_success_url()</code> <br>
</h6>

<h5>2. DeleteView</h5>
<h6>
  <b>Purpose:</b> Handles the deletion of objects from the database. <br>
  <b>When to Use:</b> <br>
  • When you need a confirmation page for deleting an object. <br>
  • Automatically deletes the object when confirmed. <br>
  <b>Attributes:</b> <code>template_name</code>, <code>model</code>, <code>success_url</code>, <code>object</code> <br>
</h6>

<h5>3. FormView</h5>
<h6>
  <b>Purpose:</b> Handles form processing without being tied to a specific model. <br>
  <b>When to Use:</b> <br>
  • When you want to handle forms with custom logic (not linked to a model). <br>
  • Useful for forms that perform non-database actions (e.g., search forms, contact forms). <br>
  <b>Attributes:</b> <code>template_name</code>, <code>form_class</code>, <code>success_url</code>, <code>get_success_url()</code> <br>
</h6>

<h5>4. UpdateView</h5>
<h6>
  <b>Purpose:</b> Handles updating existing objects in the database. <br>
  <b>When to Use:</b> <br>
  • When you need to display a form for updating an existing object. <br>
  • Automatically saves the updated data to the database. <br>
  <b>Attributes:</b> <code>template_name</code>, <code>form_class</code>, <code>fields</code>, <code>success_url</code>, <code>get_success_url()</code> <br>
</h6>



---
### Generic Detail
[-](#class-base-view-cbv)   
<h5>1. DetailView</h5>
<h6>
  <b>Purpose:</b> Displays detailed information about a specific object from the database. <br>
  <b>When to Use:</b> <br>
  • When you want to display detailed information about a single object (e.g., a product, blog post, or user profile). <br>
  • To fetch an object from the database based on its primary key or slug and render it using a template. <br>
  • <b>Attributes:</b> <code>model</code>, <code>template_name</code>, <code>context_object_name</code>, <code>slug_field</code>, <code>slug_url_kwarg</code>, <code>pk_url_kwarg</code>, <code>get_context_data()</code> <br>
</h6>


 


---
### Generic List
[-](#class-base-view-cbv)   
<h5>2. ListView</h5>
<h6>
  <b>Purpose:</b> Displays a list of objects from a database model. <br>
  <b>When to Use:</b> <br>
  • When you want to display a list of objects, such as blog posts, products, or any other model-based items. <br>
  • Automatically handles pagination for large datasets. <br>
  • It can filter and order results using query parameters. <br>
  • <b>Attributes:</b> <code>model</code>, <code>template_name</code>, <code>context_object_name</code>, <code>paginate_by</code>, <code>ordering</code>, <code>get_queryset()</code> <br>
</h6>


 


---
### Generic Dates 
[-](#class-base-view-cbv)   
<h5>1. ArchiveIndexView</h5>
<h6>
  <b>Purpose:</b> This view is used for displaying a list of archived objects based on a particular time period (e.g., all objects from a certain year, month, or day). It provides a starting point for time-based views like year-based, month-based, etc. <br>
  <b>When to Use:</b> <br>
  • When you want to show a list of archived data organized by date. <br>
  • Typically used when displaying all objects in a particular time range (e.g., all blog posts published in a year). <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>template_name</code>, <code>context_object_name</code> <br>
</h6>

<h5>2. DateDetailView</h5>
<h6>
  <b>Purpose:</b> This view is used to display a detail view for a particular object within a specified date range (such as an object published on a specific day). <br>
  <b>When to Use:</b> <br>
  • When you need to show a single object that corresponds to a specific date (e.g., a blog post published on a particular day). <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>template_name</code>, <code>context_object_name</code> <br>
</h6>

<h5>3. DayArchiveView</h5>
<h6>
  <b>Purpose:</b> This view is used for displaying all objects that were published on a specific day. <br>
  <b>When to Use:</b> <br>
  • When you want to display a list of objects published on a particular day (e.g., a list of blog posts for a specific date). <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>month_format</code>, <code>template_name</code> <br>
</h6>

<h5>4. MonthArchiveView</h5>
<h6>
  <b>Purpose:</b> This view is used for displaying all objects published within a specific month and year. <br>
  <b>When to Use:</b> <br>
  • When you need to display a list of objects for a particular month (e.g., blog posts published in January). <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>template_name</code>, <code>month_format</code> <br>
</h6>

<h5>5. TodayArchiveView</h5>
<h6>
  <b>Purpose:</b> This view is used for displaying all objects published today. <br>
  <b>When to Use:</b> <br>
  • When you want to show objects created or published today. <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>template_name</code> <br>
</h6>

<h5>6. WeekArchiveView</h5>
<h6>
  <b>Purpose:</b> This view is used for displaying all objects that were published within a specific week. <br>
  <b>When to Use:</b> <br>
  • When you want to show a list of objects published within a particular week (e.g., blog posts published between Monday and Sunday of a week). <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>template_name</code> <br>
</h6>

<h5>7. YearArchiveView</h5>
<h6>
  <b>Purpose:</b> This view is used for displaying all objects published in a particular year. <br>
  <b>When to Use:</b> <br>
  • When you want to show a list of objects published within a specific year (e.g., all blog posts from 2023). <br>
  • <b>Attributes:</b> <code>date_field</code>, <code>template_name</code> <br>
</h6>










---
## Connect Django to PostgreSQL Database 

**<h6> Install in terminal</h6>**

```
pip install psycopg2
```

**<h6> setting.py</h6>**

``` 
import dj_database_url 
import environ

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://libzone-app.onrender.com','https://*.127.0.0.1']
```

**<h6> .env</h6>**

```
SECRET_KEY=django-insecure-kyh%asdfqrysd245e^b2e5lu0f68_vt2345asdfa370%$5n&7
DB_NAME=libzone
DB_USER=postgres
DB_PASSWORD=1223
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=almamun20044@gmail.com
EMAIL_HOST_PASSWORD=xdsblb-jfpt-wxqaeh #next

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
| Class Base View (CBv)                     | [Go](#class-base-view-cbv)           |    
| Connect Django to PostgreSQL Database     | [Go](#connect-django-to-postgresql-database )           | 


