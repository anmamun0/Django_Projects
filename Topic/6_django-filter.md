## Django Filters কি?
##### django-filters একটি তৃতীয় পক্ষের Django লাইব্রেরি যা Django QuerySet-কে সহজভাবে ফিল্টার করার সুবিধা দেয়। এটি সাধারণত Django REST Framework (DRF)-এর সাথে API-তে ডাটা ফিল্টার করার জন্য ব্যবহৃত হয়।

প্রথমে ইনস্টল করতে হবে:
```bash 
pip install django-filter
```

## 1. Django Filters সেটআপ করা
প্রথমে, django_filters অ্যাপটি settings.py-তে যুক্ত করতে হবে:

```python 
INSTALLED_APPS = [
    ...
    'django_filters',
]
```
## 2. একটি মডেল তৈরি করুন

ধরুন, আমাদের একটি Book মডেল আছে যেখানে আমরা বইয়ের নাম ও প্রকাশনার বছর অনুসারে ফিল্টার করতে চাই:

```python 
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title
```

## 3. ফিল্টার সেট তৈরি করা
এখন আমরা filters.py নামে একটি নতুন ফাইল তৈরি করে ফিল্টার সেট তৈরি করবো:

```python 
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # নাম আংশিক অনুসন্ধান
    published_year = django_filters.NumberFilter()  # সঠিক বছর অনুসারে ফিল্টার

    class Meta:
        model = Book
        fields = ['title', 'published_year']
```

## 4. ফিল্টার ব্যবহার করা Django View-তে
এখন, আমরা views.py-তে django_filters ব্যবহার করে ফিল্টার অ্যাপ্লাই করবো:

```python 
from django.shortcuts import render
from .models import Book
from .filters import BookFilter

def book_list(request):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)  # ফিল্টার করা কুয়েরি
    return render(request, 'book_list.html', {'filter': book_filter})
```
    
## 5. টেমপ্লেটে ফিল্টার যোগ করা
book_list.html ফাইলটি আপডেট করুন:

```html 
<form method="GET">
    {{ filter.form.as_p }}
    <button type="submit">ফিল্টার করুন</button>
</form>

<ul>
    {% for book in filter.qs %}
        <li>{{ book.title }} - {{ book.published_year }}</li>
    {% endfor %}
</ul>
```
Django REST Framework-এর সাথে ব্যবহার করা
আপনি যদি DRF API-তে ফিল্টার ব্যবহার করতে চান, তাহলে নিচের মতো সেটআপ করতে পারেন:

```python 
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'published_year']
```

## উপসংহার
django-filters আপনাকে সহজেই Django এবং Django REST Framework-এর মধ্যে ফিল্টার যুক্ত করার সুবিধা দেয়। এটি ব্যবহার করলে QuerySet-এর ডাটা ফিল্টার করা সহজ হয়ে যায় এবং API-তে ডাটা রিফাইন করতে সহায়ক হয়। 🚀


<br>
<br>
<br>
<br>

--- 


###### ?event_date=2025-01-18&status=Ongoing&blood=A+

### Model.py

```python
from django.db import models
from django.contrib.auth.models import User

from .constraint import DONER_CHOICE ,STATUS_CHOICES
from accounts.constraint import BLOOD_GROUP
from django.core.exceptions import ValidationError

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='events')
    doner = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='doner')
    doner_message = models.TextField(blank=True,null=True,default=None)

    title = models.CharField(max_length=27)
    location = models.CharField(max_length=50,null=True)
    blood = models.CharField(max_length=10,choices=BLOOD_GROUP)
    description = models.TextField()
    event_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ongoing')
    event_time = models.TimeField() 
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
            return self.title
    def clean(self):
        # Ensure user and doner are not the same
        if self.user and self.doner and self.user == self.doner:
            raise ValidationError("The user and doner cannot be the same person.")
```


##### Filters.py

```python
import django_filters
from django_filters import FilterSet
from .models import Event

from .constraint import STATUS_CHOICES

class EventFilter(FilterSet):
    event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='exact')
    status = django_filters.ChoiceFilter(choices= STATUS_CHOICES, lookup_expr='exact')
    blood = django_filters.CharFilter(field_name='blood', lookup_expr='exact')

    class Meta:
        model = Event
        fields = ['event_date', 'status', 'blood']

     
    # def filter_blood(self, queryset, name, value):
    #     # Convert the user input value (e.g., 'bNeg') to the correct database value (e.g., 'B-')
    #     mapped_value = BLOOD_GROUP_MAPPING.get(value.lower(), None)
        
    #     if mapped_value:
    #         # Filter events based on the mapped blood group value
    #         return Event.objects.filter(blood=mapped_value)
    #     else:
    #         # If no match is found, return the original queryset (or handle as per your logic)
    #         return queryset

```
 
##### Views.py

```python
from django.shortcuts import render ,get_object_or_404
from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime

 
from django_filters import rest_framework 
from .filters import EventFilter
 



class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = EventFilter

    def get_queryset(self): 
        queryset = super().get_queryset()
        user = self.request.query_params.get('user')
        doner = self.request.query_params.get('doner')
        status = self.request.query_params.get('status')
        blood = self.request.query_params.get('blood')
        if user:
            queryset = queryset.filter(user_id=user)
        if doner:
            queryset = queryset.filter(doner_id=doner)
        if blood:
            queryset = queryset.filter(blood=blood) 
    
        return queryset

```

# Lookup Expressions in Django Filters

The `lookup_expr` is used in Django filters to specify how the filter should match the data in the database. It determines the type of comparison or query to be applied to the field.

## Common Lookup Expressions

### 1. `exact`
- Matches the field value exactly (equality comparison: `field = value`).

```python
status = django_filters.ChoiceFilter(field_name='status', lookup_expr='exact')
```
This filters events where the status is exactly equal to the provided value.

### 2. `iexact`
- Case-insensitive version of `exact`.

```python
status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
```
This filters events where the status matches the provided value, ignoring case.

### 3. `contains`
- Checks if the field contains the provided value (partial match, similar to SQL `LIKE '%value%'`).

```python
description = django_filters.CharFilter(field_name='description', lookup_expr='contains')
```
This filters events where the description contains the specified substring.

### 4. `icontains`
- Case-insensitive version of `contains`.

```python
description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
```
Filters events where the description contains the substring, ignoring case.

### 5. `gt` (Greater Than)
- Filters for values greater than the provided value.

```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='gt')
```
Filters events where the event_date is greater than the specified date.

### 6. `gte` (Greater Than or Equal To)
- Filters for values greater than or equal to the provided value.

```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='gte')
```
Filters events where the event_date is greater than or equal to the specified date.

### 7. `lt` (Less Than)
- Filters for values less than the provided value.

```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='lt')
```
Filters events where the event_date is less than the specified date.

### 8. `lte` (Less Than or Equal To)
- Filters for values less than or equal to the provided value.

```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='lte')
```
Filters events where the event_date is less than or equal to the specified date.

### 9. `in`
- Checks if the field's value is within the given list or tuple.

```python
status = django_filters.ChoiceFilter(field_name='status', lookup_expr='in')
```
Filters events where the status is in the provided list.

### 10. `isnull`
- Checks if the field is `NULL` in the database.

```python
status = django_filters.BooleanFilter(field_name='status', lookup_expr='isnull')
```
Filters events where the status field is `NULL`.

### 11. `range`
- Filters the field within a given range (e.g., for dates or numeric values).

```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='range')
```
Filters events where the event_date is within a specified date range.

### 12. `startswith`
- Filters for values that start with the given value.

```python
location = django_filters.CharFilter(field_name='location', lookup_expr='startswith')
```
Filters events where the location field starts with the specified string.

### 13. `istartswith`
- Case-insensitive version of `startswith`.

```python
location = django_filters.CharFilter(field_name='location', lookup_expr='istartswith')
```
Filters events where the location starts with the specified string, ignoring case.

### 14. `endswith`
- Filters for values that end with the given value.

```python
location = django_filters.CharFilter(field_name='location', lookup_expr='endswith')
```
Filters events where the location ends with the specified string.

### 15. `iendswith`
- Case-insensitive version of `endswith`.

```python
location = django_filters.CharFilter(field_name='location', lookup_expr='iendswith')
```
Filters events where the location ends with the specified string, ignoring case.

### 16. `date`
- Used for filtering date fields by year, month, or day.

```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='date')
```
Filters the event_date field by a specific date value.

### 17. `time`
- Used for filtering time fields.

```python
event_time = django_filters.TimeFilter(field_name='event_time', lookup_expr='time')
```
Filters the event_time field by a specific time value.

## Examples

### 1. Exact Match:
```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='exact')
```
Filters events where `event_date` is exactly equal to the provided date.

### 2. Greater Than:
```python
event_date = django_filters.DateFilter(field_name='event_date', lookup_expr='gt')
```
Filters events where `event_date` is greater than the provided date.

### 3. Contains (Partial Match):
```python
description = django_filters.CharFilter(field_name='description', lookup_expr='contains')
```
Filters events where `description` contains the provided substring.

### 4. Case-Insensitive Start With:
```python
location = django_filters.CharFilter(field_name='location', lookup_expr='istartswith')
```
Filters events where `location` starts with the provided string, ignoring case.

### 5. In a List of Values:
```python
status = django_filters.ChoiceFilter(field_name='status', lookup_expr='in')
```
Filters events where `status` is one of the values in the provided list.

## Summary of Lookup Expressions

- `exact`, `iexact` — Equality checks (exact match, case-insensitive).
- `contains`, `icontains` — Checks if a field contains a value (partial match, case-insensitive).
- `gt`, `gte`, `lt`, `lte` — Comparisons (greater than, less than).
- `in` — Checks if a field is in a given list of values.
- `isnull` — Checks for `NULL` values.
- `range` — Filters by range (e.g., dates or numbers).
- `startswith`, `istartswith`, `endswith`, `iendswith` — Checks for matching prefixes or suffixes (case-sensitive or insensitive).
- `date`, `time` — Filters for specific dates or times.

You can use any of these depending on the type of filter you want to apply to your query.

Let me know if you need further details!
