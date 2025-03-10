# Django models.py Notes

## Introduction to Django Models
- In Django, models are used to define the structure of the database.
- A model is a Python class that subclasses `django.db.models.Model`.
- Each model corresponds to a table in the database.
- Fields in a model correspond to columns in a table.

## Creating a Model
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
```

## Common Field Types
- `CharField(max_length=...)` → For short text fields.
- `TextField()` → For long text.
- `IntegerField()` → For whole numbers.
- `FloatField()` → For floating-point numbers.
- `DecimalField(max_digits=..., decimal_places=...)` → For precise decimal values.
- `BooleanField(default=True/False)` → For True/False values.
- `DateField(auto_now_add=True/False, auto_now=True/False)` → For storing dates.
- `DateTimeField(auto_now_add=True/False, auto_now=True/False)` → For storing date and time.
- `EmailField()` → For email addresses.
- `URLField()` → For URLs.
- `ForeignKey(Model, on_delete=models.CASCADE)` → Defines a many-to-one relationship.
- `ManyToManyField(Model)` → Defines a many-to-many relationship.
- `OneToOneField(Model, on_delete=models.CASCADE)` → Defines a one-to-one relationship.

## Meta Class in Models
- The `Meta` class defines additional options for models.
```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"
```

### Abstract Models
- The `abstract = True` attribute in the `Meta` class makes a model abstract.
- Abstract models act as base classes that other models can inherit from but do not create database tables themselves.
```python
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
```
- Here, `Product` inherits from `BaseModel` and automatically gets `created_at` and `updated_at` fields without creating a separate `BaseModel` table.

## Model Methods
- Custom methods can be defined within a model.
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField(default=0.0)
    
    def discounted_price(self):
        return self.price - (self.price * self.discount / 100)
```

## Creating and Applying Migrations
1. Run `python manage.py makemigrations` → Creates migration files.
2. Run `python manage.py migrate` → Applies migrations to the database.

## Querying the Database
### Creating an Object
```python
book = Book.objects.create(title="Django Guide", author="AN Mamun", published_date="2023-01-01", price=19.99)
```
### Retrieving Objects
```python
books = Book.objects.all()  # Get all books
book = Book.objects.get(id=1)  # Get a specific book
books = Book.objects.filter(author="AN Mamun")  # Filter books
```
### Updating Objects
```python
book = Book.objects.get(id=1)
book.price = 24.99
book.save()
```
### Deleting Objects
```python
book = Book.objects.get(id=1)
book.delete()
```

## Model Relationships
### ForeignKey Example (Many-to-One)
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### ManyToManyField Example
```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```

### OneToOneField Example
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

## Conclusion
- `models.py` is the backbone of Django’s ORM system.
- Models define database schema and relationships.
- Querying, updating, and deleting records is simplified with Django’s ORM.
- Migrations ensure the database schema remains in sync with models.
- The `Meta` class allows setting model-specific configurations, including making a model abstract for inheritance.

