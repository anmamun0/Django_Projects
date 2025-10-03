# Django models py Notes


Model.py
- [Django Models Fields](#django-models-fields) 
- [Meta Class](#django-model-meta-class) 
- [All Methods in model](#all-methods-in-model)
- [Abstract Models](#abstract-models)


Others File 
- [Model Query the Database](#querying-the-database)
- [Django Model _meta & Field Attributes and Methods](#django-model-_meta-field-attributes-and-methods)

<br>
<br>

# Django Models Fields
[up](#django-models-py-notes)

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

---
<br>
<br>
<br>
<br>
<br>



# Django Model Meta Class
[Home](#django-models-py-notes)

## Overview
The `Meta` class in Django models provides metadata about the model, such as how it behaves in the database, how it appears in the admin panel, and other configuration options.

---

## All Attribute in Meta Class

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

### Example Usage in Django Model

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
 

### Explanation of Common `Meta` Options

**1. `verbose_name` and `verbose_name_plural`**
- `verbose_name = "Book"` → Changes the model’s name in the Django admin.
- `verbose_name_plural = "Books"` → Changes the plural name.
<br>

**2. `db_table`**
- `db_table = "library_books"` → Defines a custom table name instead of the default (`appname_books`).
<br>

**3. `ordering`**
- `ordering = ['title']` → Orders query results alphabetically by `title`.
- `ordering = ['-created_at']` → Orders by newest first.
<br>

**4. `unique_together`**
- `unique_together = ('title', 'author')` → Ensures that the same book title cannot have the same author.
<br>

**5. `indexes`**
- `models.Index(fields=['isbn'])` → Optimizes search queries for `isbn`.
<br>

**6. `permissions`**
- Custom permission: `"can_mark_returned"` → Can be assigned to specific users.
<br>

**7. `default_permissions`**
- Controls default permissions: `('add', 'change', 'delete', 'view')`.
<br>

**8. `get_latest_by`**
- `get_latest_by = "created_at"` → Allows fetching the latest book using `latest()`.
<br>

**9. `managed`**
- `managed = False` → Prevents Django from managing this table (useful for legacy databases).
<br>

**10. `default_related_name`**
- `default_related_name = "books_related"` → Default related name for reverse lookups.
<br>


---
<br>
<br>
<br>
<br>
<br>
<br>



# All Methods in model
[Home](#django-models-py-notes)

| Method                  | বাংলা ব্যাখ্যা                    |
| ----------------------- | --------------------------------- |
| `__str__()`             | human-readable string রিটার্ন     |
| `save()`                | object ডাটাবেজে সংরক্ষণ করে       |
| `delete()`              | object ডাটাবেজ থেকে মুছে ফেলে     |
| `clean()`               | custom validation যুক্ত করার জন্য |
| `clean_fields()`        | প্রতিটি ফিল্ডের validation চালায়  |
| `validate_unique()`     | unique constraint গুলা চেক করে    |
| `full_clean()`          | সব validation একসাথে চালায়        |
| `refresh_from_db()`     | ডাটাবেজ থেকে রিফ্রেশ করে          |
| `get_deferred_fields()` | কোন ফিল্ড lazy-loaded তা বলে দেয়  |

 

```python
from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # __str__(): object কে human-readable string এ রিটার্ন করে
        return f"{self.name} - {self.price}৳"

    def save(self, *args, **kwargs):
        # save(): ডাটাবেজে object save করে
        print("Saving the product...")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # delete(): ডাটাবেজ থেকে object মুছে ফেলে
        print("Deleting the product...")
        super().delete(*args, **kwargs)

    def clean(self):
        # clean(): custom validation এখানে করা হয়
        print("Running clean() validation...")
        if self.price < 0:
            raise ValidationError("দাম ঋণাত্মক হতে পারে না।")
        if self.quantity < 0:
            raise ValidationError("পরিমাণ ঋণাত্মক হতে পারে না।")

    def clean_fields(self, exclude=None):
        # clean_fields(): ফিল্ড-লেভেল validation
        print("Running clean_fields()...")
        super().clean_fields(exclude=exclude)

    def validate_unique(self, exclude=None):
        # validate_unique(): unique constraint গুলা চেক করে
        print("Checking validate_unique()...")
        super().validate_unique(exclude=exclude)

    def full_clean(self, exclude=None, validate_unique=True):
        # full_clean(): সব validation একসাথে চালায়: clean_fields(), clean(), validate_unique()
        print("Running full_clean()...")
        super().full_clean(exclude=exclude, validate_unique=validate_unique)

    def refresh_from_db(self, using=None, fields=None):
        # refresh_from_db(): ডাটাবেজ থেকে আবার object রিফ্রেশ করে
        print("Refreshing object from database...")
        super().refresh_from_db(using=using, fields=fields)

    def get_deferred_fields(self):
        # get_deferred_fields(): কোন ফিল্ড lazy loaded হয়েছে তা দেখায়
        print("Getting deferred fields...")
        return super().get_deferred_fields()

    class Meta:
        ordering = ['name']  # ডিফল্ট অর্ডারিং name দিয়ে
        verbose_name = "Product"
        verbose_name_plural = "Products"
```

---
<br>
<br>
<br>
<br>
<br>
<br>

# Abstract Models
[Home](#django-models-py-notes)

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

---
<br>
<br>
<br>
<br>
<br>
<br>




# Querying the Database
[Home](#django-models-py-notes)

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
 

---
<br>
<br>
<br>
<br>
<br>


 
 
# Django Model _meta Field Attributes and Methods
[Home](#django-models-py-notes)

- [Model _meta Attributes and Methods](#model-_meta-attributes-and-methods)
- [meta.get_fields() Field Attributes and Methods](#field-attributes-and-methods)
- [Django Model _meta Summary ](#django-model-_meta-summary)

---
<br>
<br>
<br>


# Model _meta Attributes and Methods
[Up](#django-model-_meta-field-attributes-and-methods)

<br>

`blog = Blog.objects.all().first()`
<h6>

| Attribute / Method      | কাজ (বাংলায়)                     | Example                                     |
| ----------------------- | -------------------------------- | ------------------------------------------- |
| **app_label**           | কোন app এর model সেটা বলে        | `blog._meta.app_label  # 'blog'`            |
| **model_name**          | model এর নাম lowercase এ         | `blog._meta.model_name  # 'blog'`           |
| **object_name**         | class নাম                        | `blog._meta.object_name  # 'Blog'`          |
| **db_table**            | database এ table এর নাম          | `blog._meta.db_table`                       |
| **verbose_name**        | singular human-readable নাম      | `blog._meta.verbose_name  # 'blog'`         |
| **verbose_name_plural** | plural নাম                       | `blog._meta.verbose_name_plural  # 'blogs'` |
| **label**               | Full label (app_label.ModelName) | `blog._meta.label  # 'blog.Blog'`           |
| **pk**                  | Primary key field object         | `blog._meta.pk`                             |
| **fields**              | সব field list (basic)            | `blog._meta.fields`                         |
| **get_fields()**        | সব field + relation field সহ     | `blog._meta.get_fields()`                   |
| **concrete_fields**     | শুধু direct field                |                                             |
| **local_fields**        | শুধুমাত্র model-এর ফিল্ড         |                                             |
| **many_to_many**        | সব many-to-many ফিল্ড            |                                             |
| **ordering**            | default ordering                 | `Blog._meta.ordering`                       |
| **unique_together**     | কোন field গুলো unique একসাথে     |                                             |
| **indexes**             | database indexes                 |                                             |
| **constraints**         | database constraints             |                                             |
| **db_tablespace**       | Tablespace নাম                   |                                             |
 
</h6>

```py
 সবচেয়ে ব্যবহৃত Meta Attributes 

blog = Blog.object.all().first()
pythonBlog._meta.get_fields()        # সব fields
blog._meta.get_field('title')  # নির্দিষ্ট field
blog._meta.fields              # local fields
blog._meta.model_name          # model নাম
blog._meta.app_label           # app নাম
blog._meta.db_table            # table নাম
blog._meta.verbose_name        # display নাম
blog._meta.pk                  # primary key field
 
blog._meta.many_to_many        # M2M fields
blog._meta.ordering            # default order
blog._meta.indexes             # indexes
blog._meta.constraints         # constraints
blog._meta.permissions         # custom permissions
blog._meta.default_manager     # default manager
 
blog._meta.abstract            # abstract model check
blog._meta.proxy               # proxy model check
blog._meta.managed             # Django manages table
blog._meta.db_tablespace       # tablespace
blog._meta.parents             # parent models
```
 
<br>

```py
blog = Blog.objects.all().first()

blog._meta.get_fields()       # সব fields সহ (ForeignKey, ManyToMany ইত্যাদি)
# [<Field: Blog.id>, <Field: Blog.title>, <Field: Blog.content>, <Field: Blog.image>, <ManyToManyField: Blog.likes>, <ManyToOneRel: Comment.blog>, ...]

blog._meta.get_field('title') # নির্দিষ্ট field object
# <django.db.models.fields.CharField: title>

blog._meta.fields             # শুধুমাত্র local fields (direct fields, relation ছাড়া)
# [<Field: Blog.id>, <Field: Blog.title>, <Field: Blog.content>, <Field: Blog.image>]

blog._meta.model_name         # model নাম
# 'blog'

blog._meta.app_label          # app নাম
# 'blog'

blog._meta.db_table           # database table নাম
# 'blog_blog'

blog._meta.verbose_name       # human-readable singular নাম
# 'blog'

blog._meta.pk                 # primary key field
# <django.db.models.fields.AutoField: id>

blog._meta.many_to_many       # সব Many-to-Many fields
# [<ManyToManyField: Blog.likes>]

blog._meta.ordering           # default ordering (model Meta class এ defined)
# []

blog._meta.indexes            # সব indexes
# []

blog._meta.constraints        # সব constraints
# []

blog._meta.permissions        # custom permissions
# []

blog._meta.default_manager    # default manager
# <django.db.models.manager.Manager object at 0x000001234ABCD>

blog._meta.abstract           # abstract model কিনা
# False

blog._meta.proxy              # proxy model কিনা
# False

blog._meta.managed            # Django এই table manage করছে কিনা
# True

blog._meta.db_tablespace      # কোন DB tablespace ব্যবহার হচ্ছে
# ''

blog._meta.parents            # parent models (in case of model inheritance)
# {} (empty হলে no parent)

```


---
<br>
<br>
<br>


 
#  Field Attributes and Methods
[Up](#django-model-_meta-field-attributes-and-methods)

`blog = Blog.objects.all().first()`
`field = blog.meta.get_fields()[0]` 

<h6>

| Attribute / Method      | কাজ (বাংলায়)                           | Example                                    |
| ----------------------- | -------------------------------------- | ------------------------------------------ |
| **name**                | ফিল্ডের নাম                            | `field.name`                               |
| **verbose_name**        | human readable নাম                     | `field.verbose_name`                       |
| **get_internal_type()** | field এর ধরন                           | `field.get_internal_type()  # 'CharField'` |
| **null**                | DB তে null allow করবে কিনা             | `field.null`                               |
| **blank**               | form এ ফাঁকা রাখা যাবে কিনা            | `field.blank`                              |
| **default**             | default মান                            | `field.default`                            |
| **choices**             | select/dropdown option এর জন্য choices | `field.choices`                            |
| **max_length**          | max length (CharField/TextField)       | `field.max_length`                         |
| **primary_key**         | primary key কিনা                       | `field.primary_key`                        |
| **unique**              | unique constraint আছে কিনা             | `field.unique`                             |
| **is_relation**         | relation field কিনা                    | `field.is_relation`                        |
| **related_model**       | কোন model এর সাথে relation             | `field.related_model`                      |
| **editable**            | admin বা form এ editable কিনা          | `field.editable`                           |
| **help_text**           | ফিল্ডের জন্য extra description         | `field.help_text`                          |
| **auto_created**        | auto তৈরি field কিনা (e.g. M2M)        |                                            |
| **db_index**            | database index আছে কিনা                | `field.db_index`                           |
| **db_column**           | database এ column নাম                  | `field.db_column`                          |
| **attname**             | attribute name (ORM এ)                 | `field.attname`                            |
 
</h6>

```py
    blogs = Blog.objects.all().order_by('-created_at')
    blog = Blog.objects.all().first()
    # Model এর meta তথ্য
    meta = blog._meta

    print("Model Name:", meta.model_name)
    print("App Label:", meta.app_label)
    print("DB Table:", meta.db_table)
    print("Object Name:", meta.object_name)
    print("Verbose Name:", meta.verbose_name)
    print("Verbose Name Plural:", meta.verbose_name_plural)
    print("Label:", meta.label)
    print("Label Lower:", meta.label_lower)

    print("\nAll Fields:")
    for field in meta.get_fields():
        print(f"  {field.name} ({field.get_internal_type()})")
    
    print("\nAll Fields with details:--------------------------\n")
    for field in meta.get_fields():
        print(f"\nField Name: {field.name}")
        print(f"  Type: {field.get_internal_type()} (এই ফিল্ডের ধরন)")
        print(f"  Column: {getattr(field, 'column', None)} (DB column নাম)")
        print(f"  Verbose Name: {field.verbose_name} (Admin panel এ ব্যবহার হয়)")
        print(f"  Help Text: {field.help_text} (User কে বোঝানোর জন্য)")
        print(f"  Primary Key: {field.primary_key} (এইটা কি primary key?)")
        print(f"  Null: {field.null} (DB তে NULL allow?)")
        print(f"  Blank: {field.blank} (Form এ ফাকা allow?)")
        print(f"  Default: {field.default} (User কিছু না দিলে default মান)")
        print(f"  Unique: {field.unique} (মান unique হতে হবে?)")
        print(f"  Choices: {field.choices} (নির্দিষ্ট option লিস্ট)")
        print(f"  Is Relation: {field.is_relation} (Relation field?)")
        print(f"  Related Model: {field.related_model} (যদি relation থাকে)")
    print("\n --------------------------\n") 
```

---
<br>
<br>
<br>
<br>
<br>
 
# Django Model _meta Summary 
[Up](#django-model-_meta-field-attributes-and-methods)

1. Field সংক্রান্ত
<h6> 
 
| Attribute / Method        | Returns                                | Use Case                                      |
| ------------------------- | -------------------------------------- | --------------------------------------------- |
| `get_fields()`            | সব fields (Local + Relation + Reverse) | Field inspection                              |
| `get_field('field_name')` | নির্দিষ্ট field object                 | Field details (type, max_length, null, blank) |
| `fields`                  | Local fields (direct DB columns)       | Basic field list                              |
| `local_fields`            | Directly defined fields                | Similar to fields                             |
| `concrete_fields`         | DB column fields (ManyToMany বাদ)      | Column inspection                             |
| `many_to_many`            | ManyToMany fields                      | Relationship check                            |
| `related_objects`         | Reverse relations                      | Other models pointing to this model           |
| `private_fields`          | Internal/private fields                | Rarely used                                   |

</h6>

2. Model Info
<h6> 
 
| Attribute             | Returns                    | Use Case                       |
| --------------------- | -------------------------- | ------------------------------ |
| `model_name`          | Model নাম lowercase        | Dynamic queries, introspection |
| `object_name`         | Model class নাম            | Code reference                 |
| `verbose_name`        | Human-readable singular    | UI, admin labels               |
| `verbose_name_plural` | Human-readable plural      | UI, admin labels               |
| `label`               | Full label `app.ModelName` | Identification                 |
| `label_lower`         | Lowercase full label       | Identification                 |
| `app_label`           | App name                   | App identification             |
| `app_config`          | AppConfig object           | App metadata                   |
| `db_table`            | Table name                 | Raw SQL queries                |

</h6>
 
3. Model Configuration
<h6> 
 
| Attribute              | Returns                       | Use Case                          |
| ---------------------- | ----------------------------- | --------------------------------- |
| `ordering`             | Default ordering              | Query ordering                    |
| `get_latest_by`        | Field name for `latest()`     | Latest object query               |
| `unique_together`      | Unique field combinations     | Constraint validation             |
| `indexes`              | List of indexes               | DB optimization                   |
| `constraints`          | List of constraints           | Validation, DB integrity          |
| `permissions`          | Custom permissions            | Admin / custom roles              |
| `default_permissions`  | Default permissions           | 'add', 'change', 'delete', 'view' |
| `default_related_name` | Reverse relation default name | Related field naming              |

</h6>

4. Primary Key & Manager
   
<h6> 
 
| Attribute         | Returns                    | Use Case               |
| ----------------- | -------------------------- | ---------------------- |
| `pk`              | Primary key field object   | Key info               |
| `auto_field`      | Auto increment field       | PK / AutoField check   |
| `default_manager` | Default manager object     | `objects` access       |
| `base_manager`    | Base manager               | Related lookups        |
| `managers`        | List of managers           | Custom managers        |
| `managers_map`    | Dict name → Manager object | Lookup manager by name |

</h6>

5. Model Structure
<h6> 
 
| Attribute                  | Returns                | Use Case                    |
| -------------------------- | ---------------------- | --------------------------- |
| `abstract`                 | Boolean                | Abstract model check        |
| `proxy`                    | Boolean                | Proxy model check           |
| `swapped`                  | Model swapped name     | Replacement check           |
| `managed`                  | Boolean                | Django DB migration control |
| `proxy_for_model`          | Original model         | Proxy reference             |
| `parents`                  | Parent models dict     | Inheritance check           |
| `get_parent_list()`        | List of parent models  | Inheritance chain           |
| `get_ancestor_link(model)` | Link field to ancestor | Parent relationship         |

</h6>


6. Database & Schema
<h6> 
 
| Attribute                 | Returns                        | Use Case            |
| ------------------------- | ------------------------------ | ------------------- |
| `db_tablespace`           | DB tablespace name             | DB optimization     |
| `required_db_features`    | Required DB features           | Compatibility check |
| `required_db_vendor`      | DB vendor requirement          | Compatibility check |
| `db_returning`            | RETURNING support (PostgreSQL) | DB query support    |
| `can_migrate(connection)` | Boolean                        | Migration check     |

</h6>
 


