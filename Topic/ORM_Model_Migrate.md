# Advanced Django Models & ORM

**Summary Table:**

<h6>
 
- [Model Relationships](#model-relationships)
- [Migrations কি?](#migrations-কি)
- [Advanced ORM Queries](#advanced-orm-queries)
  
</h6>

<br>
<br>
<br>

## Model Relationships
Django তে ৩ ধরনের main relationships আছে:

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

### 3. Specific Migration File Apply
```shell
python manage.py migrate myapp 0002_auto_20250907_1234
```
- নির্দিষ্ট migration file কে apply করতে।
- Useful for rollback / test purpose।

### 4. Fake Migration
```shell
python manage.py migrate myapp --fake
```
- Database already updated আছে, কিন্তু Django কে জানাতে চাই যে migration apply হয়েছে।
- Example: Manual DB changes করলে।

### 5. Rollback / Migrate to Previous State
```shell
python manage.py migrate myapp 0001
```
- কোনো migration undo করতে।
- Example: নতুন field add করা হয়েছে কিন্তু problem দেখা দিয়েছে।

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

ORM দিয়ে আমরা Python code দিয়ে database query করতে পারি, SQL লিখার দরকার নেই।

- `objects.create()` → নতুন row add
- `objects.all()` → সব row fetch
- `objects.filter()` → condition অনুযায়ী fetch
- `objects.get()` → specific row fetch, যদি না থাকে error দিবে
- `save()` → change save করা
- `delete()` → remove record


### 2.1 Django ORM Lookups
```py
from people.models import Student

# ------------------------------
# 1️⃣ Exact / Basic Matching
# ------------------------------
# name ঠিক "Rahim" এর সমান
Student.objects.filter(name__exact="Rahim")       # Case-sensitive
Student.objects.filter(name__iexact="rahim")      # Case-insensitive

# use case: যদি তুমি শুধু ঠিক মিলানো value খুঁজতে চাও

# ------------------------------
# 2️⃣ Comparison Operators
# ------------------------------
Student.objects.filter(marks__gt=80)   # marks > 80
Student.objects.filter(marks__gte=80)  # marks >= 80
Student.objects.filter(marks__lt=50)   # marks < 50
Student.objects.filter(marks__lte=50)  # marks <= 50

# use case: নির্দিষ্ট score বা range অনুযায়ী filter করা

# ------------------------------
# 3️⃣ Null / Boolean Checks
# ------------------------------
Student.objects.filter(age__isnull=True)       # age null
Student.objects.filter(active__exact=True)     # active field True

# use case: null value খুঁজা, boolean field check করা

# ------------------------------
# 4️⃣ String Lookups
# ------------------------------
Student.objects.filter(name__contains="Rahim")       # "Rahim" substring আছে
Student.objects.filter(name__icontains="rahim")      # case-insensitive
Student.objects.filter(name__startswith="Mr.")       # name "Mr." দিয়ে শুরু
Student.objects.filter(name__istartswith="mr.")      # case-insensitive
Student.objects.filter(name__endswith="Khan")        # name "Khan" দিয়ে শেষ
Student.objects.filter(name__iendswith="khan")       # case-insensitive

# use case: search/filter text data, like search boxes

# ------------------------------
# 5️⃣ Choice / In List
# ------------------------------
Student.objects.filter(grade__in=["A", "B"])  # grade "A" বা "B"

# use case: multiple option select

# ------------------------------
# 6️⃣ Range Lookup
# ------------------------------
Student.objects.filter(marks__range=(50, 80))  # 50 <= marks <= 80

# use case: range এর মধ্যে value filter করা

# ------------------------------
# 7️⃣ Date / Time Lookups
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
# 8️⃣ Related Lookups (ForeignKey, OneToOne)
# ------------------------------
Student.objects.filter(teacher__name="Mr. Rahim") # Teacher নাম "Mr. Rahim"

# use case: join like query, relational filtering

# ------------------------------
# 9️⃣ ManyToMany Lookups
# ------------------------------
Student.objects.filter(courses__name="Math")      # "Math" course এ enrolled
Student.objects.filter(courses__name__icontains="math") # case-insensitive

# use case: M2M relation এর filter

# ------------------------------
# 🔟 Custom / Advanced Lookups
# ------------------------------
Student.objects.filter(marks__gt=F('previous_marks') + 10)  # F() used for field reference
Student.objects.annotate(total_marks=F('marks') + 5)         # annotation

# use case: calculation/query-time computation

```
 
2.1 Lookups
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

2.2 Aggregation

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

2.3 Annotation

Annotation দিয়ে query এর result এ extra calculated field add করা যায়।
```py
from django.db.models import F, Count

# add 5 marks to each student (in query)
Student.objects.annotate(new_marks=F('marks') + 5)

# Count students per teacher
Teacher.objects.annotate(student_count=Count('student'))
```

2.4 Ordering & Limiting
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








