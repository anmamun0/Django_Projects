<img width="1012" height="205" alt="image" src="https://github.com/user-attachments/assets/6fe5a8d3-81b4-4fa3-b0f6-23d9a2f683e8" /> 

# Advanced Django Models & ORM

**Summary Table:**
 
- [Model Relationships](#model-relationships)
- [Migrations কি?](#migrations-কি)
- [Advanced ORM Queries](#advanced-orm-queries)
<br>

*For makde that anCoder*
- [Django Serise ORM ](#django-orm)
   
<br>
<br>

 
# Model Relationships
[Home](#advanced-django-models--orm)

Django তে ৩ ধরনের main relationships আছে:
<br>

### 1. One-to-Many (ForeignKey)

- একটি parent object এর সাথে অনেক child object যুক্ত থাকে।
- Example: একজন teacher এর অনেক student আছে
  
```python
class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
``` 
- `on_delete=models.CASCADE` → Teacher delete হলে তার students ও delete হবে
- `student.teacher` → student এর teacher access
- `teacher.student_set.all()` → teacher এর সব student access
  
Forward access:
```python
student = Student.objects.get(id=1)
student.teacher  # Student এর Teacher কে access করা
```

Reverse access (Teacher থেকে তার students):
```python
teacher = Teacher.objects.get(id=1)
teacher.student_set.all()  # এই teacher এর সব students
```
<br>

## 2. One-to-One (OneToOneField)

- একটি object আরেকটি object এর সাথে একভাবে linked।
- Example: User এবং Profile
```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```
 
- প্রতিটি User এর শুধু একটি Profile থাকবে
- `user.profile` → profile access
- `profile.user` → user access
<br>

## 3. Many-to-Many (ManyToManyField)

একটি object অনেক objects এর সাথে যুক্ত হতে পারে।
Example: Student এবং Course

```python
class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
```
 
- `student.courses.all()` → student এর সব courses
- `course.student_set.all()` → course এ enrolled students

Forward:
```py
student = Student.objects.get(id=1)
student.courses.all()  # student এর সব courses
```

Reverse (Course থেকে students):
```py
course = Course.objects.get(id=1)
course.student_set.all()  # course এ enrolled সব students
```
<br>

- `_set` হলো Django default reverse relation accessor।
- ForeignKey বা ManyToManyField এ forward access direct field name দিয়ে হয়।
- Reverse access এ _set ব্যবহার হয় যদি তুমি `related_name` define না করো।
- Custom name দিতে পারো `related_name='...'` দিয়ে, তখন `_set` দরকার হয় না।

---
<br>
<br>
<br>
<br>
<br>
<br>


## Migrations কি?
[Home](#advanced-django-models--orm)

- Migrations হলো Database changes track এবং apply করার system।
- যখন আমরা নতুন model বা field add করি, database এ reflect করতে migration তৈরি করতে হয়।
- Migration হলো Python file যা ডাটাবেসে SQL commands execute করে।
  
```shell
# মডেল পরিবর্তন detect করা
$ python manage.py makemigrations

# migration apply করা
$ python manage.py migrate
```




### 2. Specific App Migration
```shell
python manage.py makemigrations myapp
python manage.py migrate myapp
```
- যদি project এ অনেক apps থাকে, শুধু একটি app এর মাইগ্রেশন করতে চাইলে।
<br>

### 3. Specific Migration File Apply
```shell
python manage.py migrate myapp 0002_auto_20250907_1234
```
- নির্দিষ্ট migration file কে apply করতে।
- Useful for rollback / test purpose।
<br>

### 4. Fake Migration
```shell
python manage.py migrate myapp --fake
```
- Database already updated আছে, কিন্তু Django কে জানাতে চাই যে migration apply হয়েছে।
- Example: Manual DB changes করলে।
<br>

### 5. Rollback / Migrate to Previous State
```shell
python manage.py migrate myapp 0001
```
- কোনো migration undo করতে।
- Example: নতুন field add করা হয়েছে কিন্তু problem দেখা দিয়েছে।
<br>

### 6. SQL Preview
```
python manage.py sqlmigrate myapp 0002
```
- মাইগ্রেশন file execute হলে কোন SQL হবে সেটা দেখতে।
- Debugging এবং optimization এর জন্য খুব useful।


 

--- 

<br>
<br>
<br>


## Advanced ORM Queries
[Home](#advanced-django-models--orm)

ORM দিয়ে আমরা Python code দিয়ে database query করতে পারি, SQL লিখার দরকার নেই।

- `objects.create()` → নতুন row add
- `objects.all()` → সব row fetch
- `objects.filter()` → condition অনুযায়ী fetch
- `objects.get()` → specific row fetch, যদি না থাকে error দিবে
- `save()` → change save করা
- `delete()` → remove record
<br>

[`1 Lookups`](#21-lookups)
 | [`2 Aggregation`](#22-aggregation)
 | [`3 Annotation`](#23-annotation)
 | [`4 Ordering & Limiting`](#24-ordering--limiting)
 | [`Q objects`](#django-q-objects)


### 2.1 Lookups 
Django ORM অনেক ধরনের lookups support করে।
```py
from people.models import Student

# greater than or equal
Student.objects.filter(marks__gte=80)

# less than
Student.objects.filter(marks__lt=50)

# contains (text search)
Student.objects.filter(name__icontains="rahim")

# exact match
Student.objects.filter(roll__exact=1)
```
<br>

### 2.1 Django ORM Lookups Example
```py
from people.models import Student

# ------------------------------
# 1. Exact / Basic Matching
# ------------------------------
# name ঠিক "Rahim" এর সমান
Student.objects.filter(name__exact="Rahim")       # Case-sensitive
Student.objects.filter(name__iexact="rahim")      # Case-insensitive

# use case: যদি তুমি শুধু ঠিক মিলানো value খুঁজতে চাও

# ------------------------------
# 2. Comparison Operators
# ------------------------------
Student.objects.filter(marks__gt=80)   # marks > 80
Student.objects.filter(marks__gte=80)  # marks >= 80
Student.objects.filter(marks__lt=50)   # marks < 50
Student.objects.filter(marks__lte=50)  # marks <= 50

# use case: নির্দিষ্ট score বা range অনুযায়ী filter করা

# ------------------------------
# 3. Null / Boolean Checks
# ------------------------------
Student.objects.filter(age__isnull=True)       # age null
Student.objects.filter(active__exact=True)     # active field True

# use case: null value খুঁজা, boolean field check করা

# ------------------------------
# 4. String Lookups
# ------------------------------
Student.objects.filter(name__contains="Rahim")       # "Rahim" substring আছে
Student.objects.filter(name__icontains="rahim")      # case-insensitive
Student.objects.filter(name__startswith="Mr.")       # name "Mr." দিয়ে শুরু
Student.objects.filter(name__istartswith="mr.")      # case-insensitive
Student.objects.filter(name__endswith="Khan")        # name "Khan" দিয়ে শেষ
Student.objects.filter(name__iendswith="khan")       # case-insensitive

# use case: search/filter text data, like search boxes

# ------------------------------
# 5. Choice / In List
# ------------------------------
Student.objects.filter(grade__in=["A", "B"])  # grade "A" বা "B"

# use case: multiple option select

# ------------------------------
# 6. Range Lookup
# ------------------------------
Student.objects.filter(marks__range=(50, 80))  # 50 <= marks <= 80

# use case: range এর মধ্যে value filter করা

# ------------------------------
# 7. Date / Time Lookups
# ------------------------------
from datetime import date
Student.objects.filter(joined__year=2025)         # joined date এর year 2025
Student.objects.filter(joined__month=8)           # month August
Student.objects.filter(joined__day=7)             # day 7
Student.objects.filter(joined__week_day=1)        # Sunday (1) to Saturday(7)
Student.objects.filter(joined__date=date(2025,9,7)) # exact date
Student.objects.filter(joined__lte=date.today())  # <= today

# use case: date-based filtering, reports, analytics

# ------------------------------
# 8. Related Lookups (ForeignKey, OneToOne)
# ------------------------------
Student.objects.filter(teacher__name="Mr. Rahim") # Teacher নাম "Mr. Rahim"

# use case: join like query, relational filtering

# ------------------------------
# 9. ManyToMany Lookups
# ------------------------------
Student.objects.filter(courses__name="Math")      # "Math" course এ enrolled
Student.objects.filter(courses__name__icontains="math") # case-insensitive

# use case: M2M relation এর filter

# ------------------------------
# 10. Custom / Advanced Lookups
# ------------------------------
Student.objects.filter(marks__gt=F('previous_marks') + 10)  # F() used for field reference
Student.objects.annotate(total_marks=F('marks') + 5)         # annotation

# use case: calculation/query-time computation

```
<br>


### 2.2 Aggregation

ORM দিয়ে data summary করতে পারি।
```py
from django.db.models import Avg, Max, Min, Sum

# Average marks
Student.objects.aggregate(Avg('marks'))

# Max marks
Student.objects.aggregate(Max('marks'))

# Total marks
Student.objects.aggregate(Sum('marks'))
```
<br>

### 2.3 Annotation

Annotation দিয়ে query এর result এ extra calculated field add করা যায়।
```py
from django.db.models import F, Count

# add 5 marks to each student (in query)
Student.objects.annotate(new_marks=F('marks') + 5)

# Count students per teacher
Teacher.objects.annotate(student_count=Count('student'))
```
<br>

### 2.4 Ordering & Limiting
```py
# Order by marks descending
Student.objects.all().order_by('-marks')

# Top 5 students
Student.objects.all().order_by('-marks')[:5]

2.5 Related Lookups
# Get all students of teacher "Mr. Rahim"
Student.objects.filter(teacher__name="Mr. Rahim")

# Get all courses of student "Karim"
Student.objects.get(name="Karim").courses.all()
```
<br>

### Django Q objects

Basic OR Query
```py
from django.db.models import Q

# Example: marks > 80 OR grade = 'A'
students = Student.objects.filter(Q(marks__gt=80) | Q(grade='A'))
```
- যখন তুমি চাইছ যে একটার বেশি condition এর মধ্যে যেকোনো একটিও satisfy করলে data আনবে।
- Normally .filter() সব condition কে AND ধরে, কিন্তু OR এর জন্য Q objects লাগবে।

Basic AND Query
```py
# marks > 50 AND active=True
students = Student.objects.filter(Q(marks__gt=50) & Q(active=True))
```
- .filter() already AND করে, কিন্তু Q objects দিয়ে logical grouping করলে complex AND conditions বানানো সহজ হয়।
- বিশেষ করে nested OR/AND এর জন্য।

### NOT / Exclude Query
NOT active students
```py
students = Student.objects.filter(~Q(active=True))
```
- কোনো condition exclude / negate করতে চাইলে।
- ~Q(condition) দিয়ে negate করা হয়।


### Nested / Grouped Conditions
```py
# (marks > 80 OR grade='A') AND active=True
students = Student.objects.filter(
    (Q(marks__gt=80) | Q(grade='A')) & Q(active=True)
)
```

- যখন multiple logical conditions একসাথে লাগাতে হবে।
- parentheses দিয়ে grouping করলেই complex queries readable হয়।

### Combining with normal filter
```py
# marks > 80 OR grade='A' AND active=True
students = Student.objects.filter(Q(marks__gt=80) | Q(grade='A')).filter(active=True)
```

- Q objects এবং normal filters একসাথে ব্যবহার করা যায়।
- Logical clarity ধরে রাখা সহজ হয়।

### Lookup with Relationships
```py
# Teacher name is "Mr. Rahim" OR student grade = 'A'
students = Student.objects.filter(Q(teacher__name="Mr. Rahim") | Q(grade='A'))
```
- Related field এর উপর logical conditions লাগাতে।
- ForeignKey, OneToOne, ManyToMany relationships handle করতে পারো।

### Multiple OR Conditions
```py
# marks > 90 OR marks < 40 OR grade='C'
students = Student.objects.filter(
    Q(marks__gt=90) | Q(marks__lt=40) | Q(grade='C')
)
```

- Comment / Use Case:
- একাধিক OR condition একসাথে লাগানোর জন্য।
- Normal filter দিয়ে সম্ভব নয়।

  
---
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


 
# Django ORM
[Home](#advanced-django-models--orm)

### ORM Summary 

- `CRUD Operations`[Go](#1-crud-operations) →   Create → নতুন record তৈরি করা।Read → data পড়া, filter করা।Update → data modify করা।Delete → data remove করা।
- `Lookups & Filters`[Go](#2-django-lookups-filters) → Filter দিয়ে specific data বের করা যায়।
- `Indexing in PostgreSQL`[Go](#3-indexing-in-postgresql) → Index হল DB performance বাড়ানোর জন্য structure।
- `Aggregate`[Go](#4-aggregate) → Aggregate দিয়ে summary বা grouped calculation করা যায়।
- `Annotate`[Go](#5-annotate) → Annotate দিয়ে queryset এর individual object এ extra calculation attach করা যায়।
- `Ordering & Limiting`[Go](#6-ordering-limiting) → Sorting এবং pagination করা সহজ।
- `Expression`[Go](#7-django-orm-expressions) → Expression দিয়ে dynamic field calculation, F( ) এবং functions ব্যবহার করা হয়।
- `Complex Query`[Go](#8-complex-query) →  Q objects দিয়ে OR / AND / NOT logic তৈরি করা যায়।  
 
<br>
<br>

## 1. CRUD Operations
[Home](#orm-summary)

[`Create`](#create-new-data-record-তৈরি-করা) | [`Read`](#read-query-methods) | [`Update`](#update-methods) | [`Delete`](#delete-methods)

## Create (new data record তৈরি করা) 
[Up](#1-crud-operations) 

- `create()`           # নতুন object তৈরি করে এবং auto save করে
- `save()`             # object তৈরি করে save করা
- `bulk_create()`      # একসাথে multiple objects তৈরি করে
- `get_or_create()`    # object খুঁজে পায় না থাকলে create করে
- `update_or_create()` # object আছে কিনা check করে, update বা create 

```py
from blog.models import Blog

# 1. create() - নতুন object তৈরি করে এবং সাথে সাথেই save করে
blog1 = Blog.objects.create(title="First Blog", content="This is my first blog.")
# OUTPUT: Blog object saved in DB
# Blog.objects.all() => [<Blog: First Blog>]


# 2. save() - object তৈরি করে পরে save() call করতে হয়
blog2 = Blog(title="Second Blog", content="Saved using save() method.")
blog2.save()
# OUTPUT: Blog.objects.all() => [<Blog: First Blog>, <Blog: Second Blog>]


# 3. bulk_create() - একসাথে multiple objects তৈরি করা
blogs = [
    Blog(title="Third Blog", content="Bulk create example 1"),
    Blog(title="Fourth Blog", content="Bulk create example 2"),
]
Blog.objects.bulk_create(blogs)
# OUTPUT: Blog.objects.all() => 
# [<Blog: First Blog>, <Blog: Second Blog>, <Blog: Third Blog>, <Blog: Fourth Blog>]


# 4. get_or_create() - object খুঁজে, না পেলে create করে
blog3, created = Blog.objects.get_or_create(
    title="Unique Blog", defaults={"content": "Created if not exists"}
)
# যদি আগে না থাকে → created=True, নতুন Blog তৈরি হবে
# যদি আগে থাকে → created=False, আগেরটা return করবে
# OUTPUT Example: blog3=<Blog: Unique Blog>, created=True


# 5. update_or_create() - object খুঁজে update করে, না থাকলে create করে
blog4, created = Blog.objects.update_or_create(
    title="Update Blog",
    defaults={"content": "Updated or created content"}
)
# যদি "Update Blog" আগে থাকে → content update হবে, created=False
# যদি না থাকে → নতুন record create হবে, created=True
# OUTPUT Example: blog4=<Blog: Update Blog>, created=True

``` 
## Read Query Methods  
[up](#1-crud-operations)
- `all()`, 	# সব objects return করে     
- `get()` 		# single object return করে
- `filter()` 	# queryset return করে
- `exclude()` 	# filter এর inverse
- `values()`,`values_list()` # queryset কে dict বা tuple হিসেবে fetch করতে, only selected fields
- `order_by()`  	# dict বা tuple return
- `annotate()`  	# queryset এর individual object এ extra calculation
- `aggregate()`  # queryset summary return 

```py
from blog.models import Blog
from django.db.models import Count, Sum, Avg, Max, Min

# কিছু data তৈরি করি
Blog.objects.create(title="First Blog", views=10)
Blog.objects.create(title="Second Blog", views=20)
Blog.objects.create(title="Third Blog", views=30)
Blog.objects.create(title="Fourth Blog", views=40)
Blog.objects.create(title="Fifth Blog", views=50)


# 1. all() → সব object return করে
all_blogs = Blog.objects.all()
# OUTPUT: <QuerySet [<Blog: First Blog>, <Blog: Second Blog>, <Blog: Third Blog>, <Blog: Fourth Blog>, <Blog: Fifth Blog>]>


# 2. get() → single object return করে (match না পেলে DoesNotExist error দিবে)
single_blog = Blog.objects.get(id=1)
# OUTPUT: <Blog: First Blog>


# 3. filter() → শর্ত অনুযায়ী queryset return করে
filtered_blogs = Blog.objects.filter(views__gte=30)
# OUTPUT: <QuerySet [<Blog: Third Blog>, <Blog: Fourth Blog>, <Blog: Fifth Blog>]>


# 4. exclude() → filter এর বিপরীত, শর্ত বাদ দিয়ে দেয়
excluded_blogs = Blog.objects.exclude(views__gte=30)
# OUTPUT: <QuerySet [<Blog: First Blog>, <Blog: Second Blog>]>


# 5. values() → dict আকারে fields return করে
values_qs = Blog.objects.values("id", "title")
# OUTPUT: <QuerySet [{'id': 1, 'title': 'First Blog'}, {'id': 2, 'title': 'Second Blog'}, ...]>


# 6. values_list() → tuple আকারে fields return করে
values_list_qs = Blog.objects.values_list("id", "title")
# OUTPUT: <QuerySet [(1, 'First Blog'), (2, 'Second Blog'), ...]>


# 7. order_by() → data সাজায়
ordered_blogs = Blog.objects.order_by("-views")  
# OUTPUT: <QuerySet [<Blog: Fifth Blog>, <Blog: Fourth Blog>, <Blog: Third Blog>, <Blog: Second Blog>, <Blog: First Blog>]>


# 8. annotate() → প্রতিটি object এ extra calculation যোগ করে
annotated = Blog.objects.values("title").annotate(title_length=Count("title"))
# OUTPUT: <QuerySet [{'title': 'First Blog', 'title_length': 1}, {'title': 'Second Blog', 'title_length': 1}, ...]>


# 9. aggregate() → পুরো queryset এর summary calculation return করে
agg_data = Blog.objects.aggregate(
    total_views=Sum("views"), 
    avg_views=Avg("views"), 
    max_views=Max("views"), 
    min_views=Min("views")
)
# OUTPUT: {'total_views': 150, 'avg_views': 30.0, 'max_views': 50, 'min_views': 10}

```


## Update Methods
[up](#1-crud-operations)
- `save()` 		# object modify করে save
- `update()` 		# queryset এর উপর bulk update
- `F() expression` 	# dynamic field update | field values arithmetic করতে 			যেমন: stock=F('stock')+5
<br>

```py
from shop.models import Product
from django.db.models import F

# কিছু demo data তৈরি করি
Product.objects.create(name="Laptop", stock=10)
Product.objects.create(name="Mobile", stock=20)
Product.objects.create(name="Tablet", stock=30)


# 1. save() → নির্দিষ্ট object modify করে save করা
product = Product.objects.get(name="Laptop")
product.stock = 15
product.save()
# OUTPUT: Laptop এর stock এখন 15


# 2. update() → queryset এর উপর bulk update (loop ছাড়াই)
Product.objects.filter(name="Mobile").update(stock=25)
# OUTPUT: Mobile এর stock এখন 25


# 3. F() expression → field এর value কে arithmetic operation দিয়ে update
Product.objects.filter(name="Tablet").update(stock=F("stock") + 5)
# OUTPUT: Tablet এর stock আগের থেকে 5 বেড়ে এখন 35

```
<br>
 
##  Delete Methods 
[up](#1-crud-operations)
- `delete()` 	# single row delete , 
- 		# multiple row delete , 
- 		# bulk delete, signal fired 

```py
1. Single Row Delete
product = Product.objects.get(name="Laptop")
product.delete()
# OUTPUT: (1, {'shop.Product': 1})
# Laptop delete হয়ে গেলো

2. Multiple Rows Delete
Product.objects.filter(stock__lt=25).delete()
# OUTPUT: (1, {'shop.Product': 1})
# stock 25 এর কম যেগুলো ছিলো (Mobile), সেগুলো delete হয়ে গেলো

3. Bulk Delete (all rows একসাথে)
Product.objects.all().delete()
# OUTPUT: (1, {'shop.Product': 1})
# এখন সব Products delete হয়ে গেলো
```
---
<br>
<br>
<br>
<br>


# 2. Django Lookups & Filters
[Home](#orm-summary)

- Exact / Basic Matching Lookups
- Comparison Operations Lookups
- Boolean Checks Lookups
- String Lookups
- In List Lookups
- Range Lookup
- Date/Time Lookups
- Related Lookups (ForeignKey/ OneToOne)
- ManyToMany Lookups
- Custom / Advanced Lookups
  
<h6>

| 🔢 Category                         | 🔍 Lookup                    | ✅ Use / Meaning                | 📝 Example                                               | 📤 Output                               |                   |
| ----------------------------------- | ---------------------------- | ------------------------------ | -------------------------------------------------------- | --------------------------------------- | ----------------- |
| **1. Exact / Basic Matching**       | `__exact`                    | Exact match                    | `Book.objects.filter(title__exact="Python")`             | শুধু `"Python"` নামের book              |                   |
|                                     | `__iexact`                   | Case-insensitive exact match   | `Book.objects.filter(title__iexact="python")`            | `"Python", "PYTHON", "python"` সব match |                   |
| **2. Comparison Operations**        | `__lt`                       | Less than (`<`)                | `Book.objects.filter(price__lt=300)`                     | 300 টাকার নিচের বই                      |                   |
|                                     | `__lte`                      | Less than or equal (`<=`)      | `Book.objects.filter(price__lte=500)`                    | 500 বা তার কম দামের বই                  |                   |
|                                     | `__gt`                       | Greater than (`>`)             | `Book.objects.filter(price__gt=500)`                     | 500 টাকার বেশি দামের বই                 |                   |
|                                     | `__gte`                      | Greater than or equal (`>=`)   | `Book.objects.filter(price__gte=1000)`                   | 1000 বা তার বেশি দামের বই               |                   |
|                                     | `exclude()`                  | Not equal (`!=`)               | `Book.objects.exclude(price=500)`                        | 500 বাদে সব                             |                   |
| **3. Boolean Checks**               | `__isnull`                   | Field is NULL or not           | `Book.objects.filter(published_date__isnull=True)`       | যাদের তারিখ নাই                         |                   |
|                                     | `__in`                       | Value in list                  | `Book.objects.filter(id__in=[1,3,5])`                    | শুধু id 1,3,5 এর বই                     |                   |
|                                     | Boolean field                | True / False                   | `Book.objects.filter(is_active=True)`                    | active books                            |                   |
| **4. String Lookups**               | `__contains`                 | Case-sensitive contains        | `Book.objects.filter(title__contains="Python")`          | Title-এ "Python" আছে                    |                   |
|                                     | `__icontains`                | Case-insensitive contains      | `Book.objects.filter(title__icontains="python")`         | "python", "PYTHON" সব                   |                   |
|                                     | `__startswith`               | Starts with (case-sensitive)   | `Book.objects.filter(title__startswith="D")`             | "Django", "Data"                        |                   |
|                                     | `__istartswith`              | Starts with (case-insensitive) | `Book.objects.filter(title__istartswith="d")`            | "django", "Data"                        |                   |
|                                     | `__endswith`                 | Ends with (case-sensitive)     | `Book.objects.filter(title__endswith="ing")`             | "Learning", "Programming"               |                   |
|                                     | `__iendswith`                | Ends with (case-insensitive)   | `Book.objects.filter(title__iendswith="ING")`            | "learning", "PROGRAMMING"               |                   |
|                                     | `__regex`                    | Regex match                    | `Book.objects.filter(title__regex=r'^[A-Z]')`            | যেগুলো capital letter দিয়ে শুরু         |                   |
| **5. Range / List Lookups**         | `__range`                    | Between start & end            | `Book.objects.filter(price__range=(200,500))`            | 200-500 দামের বই                        |                   |
|                                     | `__in`                       | Value in list                  | `Book.objects.filter(title__in=["Python","C"])`          | শুধু এই নামগুলো                         |                   |
| **6. Date / Time Lookups**          | `__year`                     | Year match                     | `Book.objects.filter(published_date__year=2025)`         | 2025 সালের বই                           |                   |
|                                     | `__month`                    | Month match                    | `Book.objects.filter(published_date__month=10)`          | অক্টোবর মাসে প্রকাশিত                   |                   |
|                                     | `__day`                      | Day match                      | `Book.objects.filter(published_date__day=5)`             | মাসের ৫ তারিখে প্রকাশিত                 |                   |
|                                     | `__week`                     | Week number                    | `Book.objects.filter(published_date__week=40)`           | 40তম সপ্তাহে                            |                   |
|                                     | `__date`                     | Exact date                     | `Book.objects.filter(published_date__date="2025-10-04")` | ঐ দিনে প্রকাশিত                         |                   |
|                                     | `__hour, __minute, __second` | Time part                      | `Book.objects.filter(created_at__hour=10)`               | সকাল ১০টায় তৈরি                         |                   |
| **7. Related / ForeignKey Lookups** | `__fieldname`                | Follow foreign key             | `Book.objects.filter(author__name="Mamun")`              | Mamun এর সব বই                          |                   |
|                                     | `__id`                       | Filter by related object's id  | `Book.objects.filter(author__id=1)`                      | id=1 author এর বই                       |                   |
| **8. ManyToMany Lookups**           | `__fieldname`                | Related M2M objects            | `Book.objects.filter(tags__name="Science")`              | যাদের tag=Science                       |                   |
|                                     | `distinct()`                 | Remove duplicates              | `Book.objects.filter(tags__name="Science").distinct()`   | Duplicate ছাড়া                          |                   |
| **9. Custom / Advanced Lookups**    | `F()`                        | Field-to-field comparison      | `Book.objects.filter(stock__gt=F('price'))`              | Stock > price                           |                   |
|                                     | `Q()`                        | Complex OR / AND / NOT         | `Book.objects.filter(Q(price__lt=300)                    | Q(stock__gt=50))`                       | Condition combine |

 
</h6>
 
---
<br>
<br>
<br>
<br>


# 3. Indexing in PostgreSQL


---
<br>
<br>
<br>
<br>


# 4. Aggregate 
[Home](#orm-summary)

- `Count` →  `Count('field')` → মোট rows বা related objects গণনা করতে
- `Sum`   →  `Sum('field')` → numeric field এর total যোগফল বের করতে
- `Avg ` →  `Avg('field')` → numeric field এর average বের করতে
- `Max`  →  `Max('field')` → field এর সর্বোচ্চ value বের করতে
- `Min`  → ` Min('field')` → field এর সর্বনিম্ন value বের করতে
- `Multiple Aggregates` → একবারে একাধিক summary বের করতে

```py
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Product

# Count → মোট objects সংখ্যা গণনা
total_products = Product.objects.count()  
# বা Count field দিয়ে
total_stock_items = Product.objects.aggregate(total=Count('stock'))

# Sum → stock এর মোট যোগফল
total_stock = Product.objects.aggregate(total=Sum('stock'))

# Avg → average price বের করা
average_price = Product.objects.aggregate(avg=Avg('price'))

# Max → সর্বোচ্চ price বের করা
max_price = Product.objects.aggregate(max_price=Max('price'))

# Min → সর্বনিম্ন stock বের করা
min_stock = Product.objects.aggregate(min_stock=Min('stock'))

# Multiple Aggregates একসাথে
summary = Product.objects.aggregate(
    total_products=Count('id'),
    total_stock=Sum('stock'),
    avg_price=Avg('price'),
    max_price=Max('price'),
    min_price=Min('price'),
)

print("Total Products:", total_products)
print("Total Stock Items:", total_stock_items)
print("Total Stock:", total_stock)
print("Average Price:", average_price)
print("Max Price:", max_price)
print("Min Stock:", min_stock)
print("Summary:", summary)

```
```py
Total Products: 4
Total Stock Items: {'total': 4}
Total Stock: {'total': 320}
Average Price: {'avg': 1250.00}
Max Price: {'max_price': 2200.00}
Min Stock: {'min_stock': 20}
Summary: {
    'total_products': 4,
    'total_stock': 320,
    'avg_price': 1250.00,
    'max_price': 2200.00,
    'min_price': 500.00
}

```

---
<br>
<br>
<br>
<br>

# 5. Annotate 
[Home](#orm-summary)

- `Count('field')` → প্রতিটি object এর সাথে related items count attach করতে
- `Sum('field')` → প্রতিটি object এর সাথে numeric field এর যোগফল attach করতে
- `Avg('field')` → প্রতিটি object এর সাথে average value attach করতে
- `Max('field')` → প্রতিটি object এর সাথে maximum value attach করতে
- `Min('field')` → প্রতিটি object এর সাথে minimum value attach করতে
- `F() expressions` → প্রতিটি object এর field-to-field calculation attach করতে
- `Multiple annotate()` → একসাথে multiple calculation attach করতে

```py
from django.db.models import Count, Sum, Avg, Max, Min, F
from .models import Author, Book

# 1. Count → প্রতিটি author এর সাথে কতগুলো বই আছে
authors_with_book_count = Author.objects.annotate(total_books=Count('books'))

# 2. Sum → প্রতিটি author এর বইগুলোর মোট price
authors_with_total_price = Author.objects.annotate(total_price=Sum('books__price'))

# 3. Avg → প্রতিটি author এর বইগুলোর average price
authors_with_avg_price = Author.objects.annotate(avg_price=Avg('books__price'))

# 4. Max → প্রতিটি author এর সবচেয়ে দামি বই
authors_with_max_price = Author.objects.annotate(max_price=Max('books__price'))

# 5. Min → প্রতিটি author এর সবচেয়ে সস্তা বই
authors_with_min_price = Author.objects.annotate(min_price=Min('books__price'))

# 6. F() expression → প্রতিটি বই এর discounted price (১০% discount)
books_with_discount = Book.objects.annotate(discounted_price=F('price') * 0.9)

# 7. Multiple annotate() একসাথে
authors_with_summary = Author.objects.annotate(
    total_books=Count('books'),
    total_pages=Sum('books__pages'),
    avg_price=Avg('books__price'),
)

```

```py
# 1. Count
for a in authors_with_book_count:
    print(a.name, a.total_books)

# Output:
# "J.K. Rowling"  5
# "George Orwell" 2
# "Humayun Ahmed" 3


# 2. Sum
for a in authors_with_total_price:
    print(a.name, a.total_price)

# Output:
# "J.K. Rowling"  5200.00
# "George Orwell" 1700.00
# "Humayun Ahmed" 2400.00


# 6. F() expression (discount)
for b in books_with_discount:
    print(b.title, b.price, b.discounted_price)

# Output:
# "Harry Potter 1" 1200.00  1080.00
# "Harry Potter 2" 1000.00   900.00
# "1984"           800.00    720.00

```

---
<br>
<br>
<br>
<br>

# 5. Ordering & Limiting 
[Home](#orm-summary)

- `order_by('field')` → Queryset কে ascending বা descending order এ sort করতে
- `order_by('-field')` → descending order এ sort করতে
- `reverse()` → পূর্বে order_by করা Queryset এর order উল্টে দিতে
- `latest('field')` → date/time field অনুযায়ী newest object fetch করতে
- `earliest('field')` → date/time field অনুযায়ী oldest object fetch করতে
- `first()` → queryset থেকে প্রথম object fetch করতে
- `last()` → queryset থেকে শেষ object fetch করতে
- `Slicing` / `[:n]` → queryset এর limit set করতে, pagination এর জন্য
- `Slicing` / `[start:end]` → queryset এর subset fetch করতে 

```py
from .models import Blog

# 1. order_by('field') → ascending order
blogs = Blog.objects.order_by('views')
# Output: blogs will be sorted from lowest views to highest
# e.g. ["Blog C (50 views)", "Blog A (120 views)", "Blog B (300 views)"]

# 2. order_by('-field') → descending order
blogs = Blog.objects.order_by('-views')
# Output: ["Blog B (300 views)", "Blog A (120 views)", "Blog C (50 views)"]

# 3. reverse() → order_by এর উল্টো
blogs = Blog.objects.order_by('views').reverse()
# Output: ["Blog B (300 views)", "Blog A (120 views)", "Blog C (50 views)"]

# 4. latest('field') → সর্বশেষ publish হওয়া post
latest_blog = Blog.objects.latest('published_at')
# Output: "Blog B (Published: 2025-10-02)"

# 5. earliest('field') → সবচেয়ে পুরোনো publish হওয়া post
oldest_blog = Blog.objects.earliest('published_at')
# Output: "Blog C (Published: 2024-01-10)"

# 6. first() → queryset এর প্রথম object
first_blog = Blog.objects.order_by('views').first()
# Output: "Blog C (50 views)"

# 7. last() → queryset এর শেষ object
last_blog = Blog.objects.order_by('views').last()
# Output: "Blog B (300 views)"

# 8. Slicing [:n] → limit করা
top_2 = Blog.objects.order_by('-views')[:2]
# Output: ["Blog B (300 views)", "Blog A (120 views)"]

# 9. Slicing [start:end] → subset
subset = Blog.objects.order_by('views')[1:3]
# Output: ["Blog A (120 views)", "Blog B (300 views)"]

```
---
<br>
<br>
<br>
<br>

# 7. Django ORM Expressions
 
[Home](#orm-summary)

- `F()` → field arithmetic / comparison
- `ExpressionWrapper` → complex calculation
- `Q()` → logical conditions (OR, AND, NOT)

<br>

### 1. F() → field arithmetic / comparison

F() ব্যবহার করা হয় model field এর value কে update বা compare করার জন্য।
```py
from django.db.models import F
from .models import Product

# Example: stock 5 বাড়ানো
Product.objects.update(stock=F('stock') + 5)
# Output: প্রতিটি product এর stock 5 করে বেড়ে যাবে

# Example: discount কে price এর সমান করা
Product.objects.update(discount=F('price'))
# Output: discount field এ price এর value বসে যাবে

# Example: filter condition
expensive = Product.objects.filter(price__gt=F('discount'))
# Output: সব product যেগুলোর price > discount
```
<br>

### 2. ExpressionWrapper → complex calculation 
যখন calculation এর সাথে datatype নির্দিষ্ট করতে হয় তখন ExpressionWrapper ব্যবহার হয়।
```
from django.db.models import F, ExpressionWrapper, DecimalField

# Example: final price = price - discount
products = Product.objects.annotate(
    final_price=ExpressionWrapper(F('price') - F('discount'), output_field=DecimalField())
)

for p in products:
    print(p.name, p.final_price)
# Output:
# iPhone 1200.00
# Laptop 800.00
```
<br>

### 3. Q() → logical conditions (OR, AND, NOT) 
Q() ব্যবহার করা হয় complex query filter বানাতে (OR / AND / NOT)।
```
from django.db.models import Q

# Example: price 1000 এর বেশি OR stock 50 এর বেশি
products = Product.objects.filter(Q(price__gt=1000) | Q(stock__gt=50))
# Output: ["iPhone", "Laptop", "Monitor"]

# Example: price 500 এর কম AND stock 10 এর বেশি
products = Product.objects.filter(Q(price__lt=500) & Q(stock__gt=10))
# Output: ["Keyboard", "Mouse"]

# Example: NOT condition
products = Product.objects.filter(~Q(stock__lt=5))
# Output: সব products যাদের stock >= 5
```

---
<br>
<br>
<br>
<br>


#  8. Complex Query
[Home](#orm-summary)

`Q() / ~Q()`  → `OR / AND / NOT` logical queries করতে
- use: multiple conditions combine করতে বা inverse filter করতে

`F()` → `field-to-field comparison বা arithmetic করতে
- Use: এক field কে অন্য field এর সাথে compare বা calculate করতে

`annotate() + aggregate` → per object calculated field attach করতে
- Use: object-wise summary বা report generate করতে

`select_related()` → ForeignKey / OneToOne prefetch করতে
- Use: related object access করার সময় DB query কমাতে

`prefetch_related()` → ManyToMany বা reverse FK prefetch করতে
- Use: related objects access করার সময় multiple query reduce করতে

`Subquery + OuterRef` → nested বা correlated subquery করতে
- Use: subquery এর result per object attach করতে

`values()` / `values_list()` → queryset কে dict বা tuple হিসেবে fetch করতে
- Use: only selected fields নিতে, memory optimize করতে

`union()` / `intersection()` / `difference()` → multiple querysets combine করতে
- Use: different queryset results একত্রিত বা filter করতে



### 1. Q() / ~Q() → OR / AND / NOT 
Multiple conditions combine করার জন্য।
```py
from django.db.models import Q

# Price > 500 OR Stock > 20
Book.objects.filter(Q(price__gt=500) | Q(stock__gt=20))
# Output: ["Django Book", "Python Deep Dive"]

# Price < 300 AND Stock > 5
Book.objects.filter(Q(price__lt=300) & Q(stock__gt=5))
# Output: ["C Programming", "Algorithms"]

# NOT: stock < 10
Book.objects.filter(~Q(stock__lt=10))
# Output: ["Python Deep Dive", "Data Science"]
```
<br>
 
### 2. F() → Field-to-field comparison
```py
from django.db.models import F

# Stock = price field এর সমান
Book.objects.filter(stock=F('price'))
# Output: []

# Discount: stock কে price এর সাথে যোগ
Book.objects.update(stock=F('stock') + 5)
# Output: সব book এর stock 5 বেড়ে যাবে
```
<br>

### 3. annotate() + aggregate() 
```py
from django.db.models import Count, Avg, Sum

# প্রতিটি author এর book সংখ্যা
Author.objects.annotate(book_count=Count('books'))
# Output: {"Mamun": 5, "Rahim": 3}

# সব book এর average price
Book.objects.aggregate(Avg('price'))
# Output: {"price__avg": 450.75}
```
<br>

### 4. select_related() → ForeignKey / OneToOne
 Normal Query (N+1 problem)
```py
books = Book.objects.all()
for b in books:
    print(b.author.name)  # প্রত্যেকবার আলাদা query চলবে

# Optimized Query
books = Book.objects.select_related('author')
for b in books:
    print(b.author.name)  # একবারেই author fetch হবে
```
<br>

### 5. prefetch_related() → ManyToMany / Reverse FK
 Normal Query (multiple queries per loop)
```py
authors = Author.objects.all()
for a in authors:
    print([book.title for book in a.books.all()])

# Optimized Query
authors = Author.objects.prefetch_related('books')
for a in authors:
    print([book.title for book in a.books.all()])
```
<br>

### 6. Subquery + OuterRef → Nested Query
```py
from django.db.models import OuterRef, Subquery

latest_book = Book.objects.filter(author=OuterRef('pk')).order_by('-id')
authors = Author.objects.annotate(
    latest_book=Subquery(latest_book.values('title')[:1])
)

for a in authors:
    print(a.name, a.latest_book)
# Output:
# Mamun → "Django Advanced"
# Rahim → "Data Science 101"
```
<br>

### 7. values() / values_list()
 Dict format
```py
Book.objects.values('title', 'price')
# Output: [{'title': 'Python', 'price': 500}, {'title': 'C Prog', 'price': 250}]

# Tuple format
Book.objects.values_list('title', 'price')
# Output: [('Python', 500), ('C Prog', 250)]
```
<br>

### 8. union() / intersection() / difference()
```py
qs1 = Book.objects.filter(price__gt=500).values_list('title')
qs2 = Book.objects.filter(stock__gt=10).values_list('title')

# Union → combine results
qs1.union(qs2)
# Output: ["Python", "Data Science", "Django"]

# Intersection → common results
qs1.intersection(qs2)
# Output: ["Python"]

# Difference → only qs1 not in qs2
qs1.difference(qs2)
# Output: ["Django Advanced"]
```


---
<br>
<br>
<br>
<br>
