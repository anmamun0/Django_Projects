
##### Django প্রজেক্টের মূল ফোল্ডারের প্রতিটি ফাইল ও অ্যাপ কী কাজ করে, তার ব্যাখ্যা নিচে দেওয়া হলো:

## 📂 Django প্রজেক্ট স্ট্রাকচার
##### আপনি যখন একটি Django প্রজেক্ট তৈরি করেন, তখন এটি সাধারণত নিম্নলিখিত স্ট্রাকচার অনুসরণ করে:

```sh
my_project/
│── manage.py
│── db.sqlite3
│── .env
│── requirements.txt
│── my_project/ (Main Project Folder)
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py (Web Server Gateway Interface)
│   │── asgi.py (Asynchronous Server Gateway Interface)
│── my_app/ (Django App)
│   │── migrations/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── tests.py
│   │── serializers.py
│   │── filters.py
│   │── permissions.py
│   │── pagination.py
│   │── forms.py
│── static/
│── templates/

```

## 🔥 Django Main Project Folder (my_project/) এর কাজ

### 1️⃣ manage.py
- 👉 প্রজেক্ট চালানো ও ম্যানেজ করার স্ক্রিপ্ট
- সার্ভার রান করা, মাইগ্রেশন চালানো, সুপার ইউজার তৈরি করা ইত্যাদির জন্য ব্যবহৃত হয়।
 

```sh 
python manage.py runserver  # সার্ভার চালু করা
python manage.py makemigrations  # মডেলের জন্য মাইগ্রেশন তৈরি করা
python manage.py migrate  # ডাটাবেজ আপডেট করা
```
### 2️⃣ settings.py

- 👉 প্রজেক্টের সকল কনফিগারেশন সেটিংস 
- ডাটাবেজ সংযোগ, ইনস্টলড অ্যাপস, স্ট্যাটিক ফাইল, মিডিয়া ফাইল, সিকিউরিটি সেটিংস ইত্যাদি সংরক্ষিত থাকে।
 

```python 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',  # কাস্টম অ্যাপ যুক্ত করা হলো
]
```

### 3️⃣ urls.py
- 👉 সার্ভার অনুরোধ (request) কোন ভিউতে যাবে তা নির্ধারণ করে
- ওয়েবসাইটের বিভিন্ন পেজের জন্য URL নির্ধারণ করা হয়।
 
```python 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),  # অ্যাপের URL অন্তর্ভুক্ত করা হলো
]
```

### 4️⃣ wsgi.py

- 👉 WSGI (Web Server Gateway Interface) সার্ভার চালানোর জন্য ব্যবহৃত হয়
- এটি প্রোডাকশনে Gunicorn বা অন্য WSGI সার্ভারের সাথে কাজ করে।
 
```python 
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

application = get_wsgi_application()
```

### 5️⃣ asgi.py
- 👉 ASGI (Asynchronous Server Gateway Interface) সার্ভারের জন্য ব্যবহৃত হয়
- Django-কে WebSockets এবং Async ফিচারের সাথে সংযুক্ত করতে ব্যবহৃত হয়।


```python 
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

application = get_asgi_application()
```


 


## 🔥 Django App Folder (my_app/) এর কাজ
##### Django অ্যাপে নিচের গুরুত্বপূর্ণ ফাইলগুলো থাকে:

সংক্ষেপে প্রতিটি ফাইলের কাজ:

<h6> 
    
| File	| কাজ | 
|------------|---------------|
| models.py	| ডাটাবেজ টেবিল তৈরি করে| 
| views.py	| API বা ওয়েব লজিক থাকে| 
| serializers.py| 	ডাটা JSON-এ কনভার্ট করে| 
| urls.py	| URL এবং ভিউ মেপিং করে| 
| admin.py	| Django Admin এ মডেল যোগ করে| 
| forms.py	| Django ফর্ম তৈরি করে| 
| signals.py	| মডেল পরিবর্তনের উপর নির্ভর করে কাজ করে| 
| filters.py	| ডাটা ফিল্টারিং করে| 
| tests.py	| Django টেস্টিং ফাইল| 
| permissions.py	| API এক্সেস কন্ট্রোল করে| 
| throttling.py	| API Request Rate Limit সেট করে| 
| pagination.py	| API pagination সেট করে| 
| authentication.py	| কাস্টম authentication তৈরি করে | 

</h6>

##### Django অ্যাপে থাকা প্রতিটি ফাইলের কাজ সংক্ষেপে নিচে দেওয়া হলো:

### 1. models.py
- 👉 ডাটাবেজের কাঠামো তৈরি করে
- এখানে Django ORM ব্যবহার করে টেবিল (Model) তৈরি করা হয়।
- প্রতিটি মডেল ক্লাসের মাধ্যমে ডাটাবেজে টেবিল তৈরি হয়।
- CharField, IntegerField, ForeignKey ইত্যাদি ফিল্ড ব্যবহার করা হয়।
 
```python 
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

### 2. views.py

- 👉 ব্যবহারকারীর অনুরোধ (request) প্রক্রিয়াকরণ করে
- এখানে API বা ওয়েবপেজের মূল লজিক থাকে।
- ফাংশন-বেইজড (FBV) বা ক্লাস-বেইজড (CBV) ভিউ ব্যবহার করা হয়।
- উদাহরণ (Function-Based View):

```python 
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Django"})
```


### 3. serializers.py (Django REST Framework)

- 👉 ডাটাবেজের ডাটা JSON বা অন্য ফরম্যাটে কনভার্ট করে
- ModelSerializer ব্যবহার করে মডেল থেকে ডাটা serialize করা হয়।
 

```python 
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

### 4. urls.py

- 👉 URL এবং ভিউ মেপিং করে
- ব্যবহারকারী যখন URL-এ কিছু লেখে, তখন সেটা কোন ভিউ চালু হবে তা নির্ধারণ করে।
 

```python 
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

### 5. admin.py

- 👉 Django Admin Panel-এ মডেল দেখানোর জন্য ব্যবহৃত হয়
- ডাটাবেজের টেবিলগুলো Django Admin Dashboard-এ দেখানোর জন্য এটি ব্যবহৃত হয়।
 

```python 
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

### 6. forms.py

- 👉 HTML ফর্মের জন্য Django ফর্ম তৈরি করা হয়
- Django এর বিল্ট-ইন ফর্ম ব্যবহার করে ইউজার ইনপুট নেওয়া হয়।
 
```python 
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
```

### 7. signals.py

- 👉 কোনো মডেলের পরিবর্তনের উপর নির্ভর করে অটোমেটিক কাজ করার জন্য
- Django এর Signal ব্যবহার করে কোনো মডেল তৈরি, আপডেট বা ডিলিট হলে বিশেষ কাজ করা যায়।

উদাহরণ:

```python 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=Student)
def student_saved(sender, instance, **kwargs):
    print(f'Student {instance.name} has been saved!')

```

### 8. filters.py (Django Filters)

- 👉 API-এর মধ্যে ডাটা ফিল্টারিং করার জন্য ব্যবহৃত হয় 
- Django Filter ব্যবহার করে সহজেই কাস্টম ফিল্টার তৈরি করা যায়।
 

```python 
import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['name']

```

### 9. tests.py

- 👉 অ্যাপের ফাংশন এবং API টেস্ট করার জন্য ব্যবহৃত হয় 
- unittest বা pytest দিয়ে Django অ্যাপ টেস্ট করা যায়।
 
```python 
from django.test import TestCase
from .models import Student

class StudentTestCase(TestCase):
    def test_student_creation(self):
        student = Student.objects.create(name="John Doe", age=20)
        self.assertEqual(student.name, "John Doe")

```

### 10. permissions.py (Django REST Framework)
- 👉 API তে অ্যাক্সেস কন্ট্রোল করার জন্য ব্যবহৃত হয়
- কোন ইউজার কোন API অ্যাক্সেস করতে পারবে তা নিয়ন্ত্রণ করে।
 

```python 
from rest_framework import permissions

class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
```

### 11. throttling.py
- 👉 API-তে Request Rate Limit সেট করতে ব্যবহৃত হয়
- কতবার একজন ইউজার API-তে রিকোয়েস্ট পাঠাতে পারবে তা কন্ট্রোল করা হয়।
 
```python 
from rest_framework.throttling import UserRateThrottle

class CustomThrottle(UserRateThrottle):
    rate = '5/min'  # প্রতি মিনিটে ৫ বার রিকোয়েস্ট করতে পারবে
```

### 12. pagination.py
- 👉 API-এর মধ্যে ডাটা pagination করার জন্য ব্যবহৃত হয়
- বড় ডাটাবেজ থেকে অল্প কিছু ডাটা একবারে দেখানোর জন্য ব্যবহৃত হয়।
 
```python 
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10

```

### 13. authentication.py
- 👉 কাস্টম অথেনটিকেশন পদ্ধতি তৈরি করার জন্য ব্যবহৃত হয়
- JWT, Token Authentication, অথবা কাস্টম অথেনটিকেশন তৈরি করা যায়।
 

```python 
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token or token != "mysecrettoken":
            raise AuthenticationFailed("Invalid token")
        return (None, None)
```


---

## 🔥 অন্যান্য গুরুত্বপূর্ণ ফোল্ডার

### 1️⃣ migrations/
- 👉 ডাটাবেজ আপডেটের জন্য ফাইল সংরক্ষণ করে

### 2️⃣ static/
- 👉 CSS, JavaScript, এবং ইমেজ সংরক্ষণ করা হয়

### 3️⃣ templates/
- 👉 HTML ফাইল সংরক্ষিত থাকে


