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

# Django Model Meta Class

## Overview
The `Meta` class in Django models provides metadata about the model, such as how it behaves in the database, how it appears in the admin panel, and other configuration options.

---

## All Operations in Meta Class

<h6> 

| **Option**                 | **Description** |
|----------------------------|-----------------|
| `verbose_name`            | Custom name for the model in Django Admin. |
| `verbose_name_plural`     | Custom plural name for the model in Django Admin. |
| `db_table`                | Custom database table name. |
| `ordering`                | Default sorting order of query results. |
| `unique_together`         | Enforces uniqueness on multiple fields together. |
| `index_together` (Deprecated) | Improves query performance on a combination of fields. *(Use `indexes` instead.)* |
| `indexes`                 | Creates database indexes for faster queries. |
| `permissions`             | Defines custom user permissions. |
| `default_permissions`     | Controls default permissions (`add`, `change`, `delete`, `view`). |
| `get_latest_by`           | Specifies a date field for `latest()` query. |
| `managed`                 | Determines if Django should manage this table (useful for existing DB tables). |
| `abstract`                | Makes a model abstract, meaning it won’t create a table but can be inherited. |
| `app_label`               | Specifies the app name if the model is in a different app. |
| `proxy`                   | Defines a proxy model that doesn’t create a new database table. |
| `default_related_name`    | Sets a default related name for reverse relationships. |

</h6>

---

## Example Usage in Django Model

```python
from django.db import models

class Books(models.Model):
    image = models.ImageField(upload_to='books/media/uploads/', null=True, blank=True, verbose_name="Book Cover")
    title = models.CharField(max_length=255, verbose_name="Book Title")
    author = models.CharField(max_length=255, verbose_name="Author Name")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN Number")  
    category = models.ManyToManyField('Category', blank=True, related_name='books', verbose_name="Categories") 
    description = models.TextField(verbose_name="Book Description") 
    copies = models.IntegerField(default=0, verbose_name="Available Copies")  

    class Meta:
        verbose_name = "Book"  # Admin model name
        verbose_name_plural = "Books"  # Plural name in Admin
        db_table = "library_books"  # Custom table name
        ordering = ['title']  # Default sorting order
        unique_together = ('title', 'author')  # Unique constraint for (title, author)
        indexes = [
            models.Index(fields=['isbn']),  # Creates an index for faster lookup
        ]
        permissions = [
            ("can_mark_returned", "Can mark book as returned"),  # Custom permission
        ]
        default_permissions = ('add', 'change', 'delete', 'view')  # Default permissions
        get_latest_by = "created_at"  # Used in `latest()` queries
        managed = True  # Django will manage the table
        default_related_name = "books_related"  # Default related name for reverse lookups

    def __str__(self):
        return f"{self.isbn} - {self.title}"
```

---

## Explanation of Common `Meta` Options

### **1. `verbose_name` and `verbose_name_plural`**
- `verbose_name = "Book"` → Changes the model’s name in the Django admin.
- `verbose_name_plural = "Books"` → Changes the plural name.

### **2. `db_table`**
- `db_table = "library_books"` → Defines a custom table name instead of the default (`appname_books`).

### **3. `ordering`**
- `ordering = ['title']` → Orders query results alphabetically by `title`.
- `ordering = ['-created_at']` → Orders by newest first.

### **4. `unique_together`**
- `unique_together = ('title', 'author')` → Ensures that the same book title cannot have the same author.

### **5. `indexes`**
- `models.Index(fields=['isbn'])` → Optimizes search queries for `isbn`.

### **6. `permissions`**
- Custom permission: `"can_mark_returned"` → Can be assigned to specific users.

### **7. `default_permissions`**
- Controls default permissions: `('add', 'change', 'delete', 'view')`.

### **8. `get_latest_by`**
- `get_latest_by = "created_at"` → Allows fetching the latest book using `latest()`.

### **9. `managed`**
- `managed = False` → Prevents Django from managing this table (useful for legacy databases).

### **10. `default_related_name`**
- `default_related_name = "books_related"` → Default related name for reverse lookups.

---

## When to Use These Options?

| **Use Case**                        | **Meta Options to Use** |
|-------------------------------------|--------------------|
| **Change admin model name**        | `verbose_name`, `verbose_name_plural` |
| **Customize database table name**   | `db_table` |
| **Enforce unique combinations**     | `unique_together` |
| **Optimize database performance**   | `indexes` |
| **Set permissions**                 | `permissions`, `default_permissions` |
| **Change default ordering**         | `ordering` |
| **Prevent Django from managing DB table** | `managed = False` |
| **Proxy models (no new table)**     | `proxy = True` |
| **Define app name explicitly**      | `app_label` |

---
 

## Meta Class in Models
- The `Meta` class defines additional options for models.
```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['title']   # Default ordering by book title
        verbose_name = "Book"   # Custom name for the model in Django Admin
        verbose_name_plural = "Books"  # Custom plural name in Admin
        db_table = "library_books"  # Custom table name in the database
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

