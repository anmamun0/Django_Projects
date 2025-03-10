# Django admin.py Notes

## Introduction to Django Admin
- The Django admin site provides a built-in interface for managing models.
- It is enabled by default in Django projects.
- The `admin.py` file is used to register models and customize the admin interface.

## Enabling the Admin Site
- Ensure `django.contrib.admin` is included in `INSTALLED_APPS` in `settings.py`.
- Run migrations to create admin-related tables:
```sh
python manage.py migrate
```

## Accessing the Admin Panel
- Create a superuser:
```sh
python manage.py createsuperuser
```
- Log in at `http://127.0.0.1:8000/admin/`.

## Registering Models in Admin
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```
- This makes the `Book` model accessible in the admin panel.

## Customizing the Admin Interface
### Using `Admin` Classes
```python
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price')
    search_fields = ('title', 'author')
    list_filter = ('published_date', 'price')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Book, BookAdmin)
```
### Explanation of Admin Options
- `list_display`: Fields to show in the list view.
- `search_fields`: Enables a search bar.
- `list_filter`: Adds filter options.
- `ordering`: Default sorting.
- `prepopulated_fields`: Auto-generates values for slug fields.
- `readonly_fields`: Prevents editing of certain fields.



## Custom Method in Django Admin (`list_display`)

### How to Use a Custom Method in `list_display`?
1. Define a **method** inside the `ModelAdmin` class.
2. Use `obj.related_field.field_name` to access related data.
3. Set `short_description` to customize the column header.

### Example: Displaying Book Title in `TransactionAdmin`

###### admin.py
```python
from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'book_title', 'borrow_date', 'due_date', 'status']

    def book_title(self, obj):
        return obj.book.title  # Fetch book title from related Book model

    book_title.short_description = "Book Title"  # Custom column name

admin.site.register(Transaction, TransactionAdmin)
```

models.py
```py
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
```

---

### Explanation
| Feature | Description |
|---------|------------|
| `def book_title(self, obj):` | Defines a method to fetch `book.title`. |
| `return obj.book.title` | Accesses the `title` field from the related `Book` model. |
| `book_title.short_description = "Book Title"` | Customizes the column name in Django Admin. |
| `list_display = [...]` | Includes the method name (`book_title`) instead of `book.title`. |

---



## Auto-Generating Slugs
- A slug is a URL-friendly identifier derived from another field.
- Use `prepopulated_fields` in `ModelAdmin`:

```python
from .models import Category,Books

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)
```

- Alternatively, use `slugify` in the model:
```python
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
```

## Inline Model Administration
```python
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]

admin.site.register(Book, BookAdmin)
```
- `TabularInline` and `StackedInline` allow editing related objects within the parent model’s admin page.

## Customizing the Admin Panel Header
```python
admin.site.site_header = "My Bookstore Admin"
admin.site.site_title = "Bookstore Admin Portal"
admin.site.index_title = "Welcome to the Bookstore Admin"
```

## Adding Custom Actions
- Define a custom action to update multiple records at once:
```python
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'total_amount')
    actions = ['mark_as_shipped']

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='Shipped')
    mark_as_shipped.short_description = "Mark selected orders as shipped"

admin.site.register(Order, OrderAdmin)
```

## Customizing Form Fields in Admin
- Use `formfield_overrides` to change widget styles:
```python
from django.forms import Textarea

class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

admin.site.register(Product, ProductAdmin)
```

## Filtering and Search
### Filtering
- `list_filter`: Adds filter options to the right sidebar for quick filtering.
- Example:
```python
class PostAdmin(admin.ModelAdmin):
    list_filter = ('published_date', 'category')
```
- This allows filtering posts by `published_date` and `category`.

- `date_hierarchy`: Adds a date-based filter navigation at the top of the admin page:
```python
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
```
- This creates a drill-down date filter (Year > Month > Day).

### Search
- `search_fields`: Enables a search bar to look for specific field values.
- Example:
```python
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author__name')
```
- This enables searching by post `title` and `author` name.
- Use double underscores `__` to search related models.

## Custom Model Admin Templates
- Override admin templates by creating `templates/admin/model_name/change_form.html`.
- Example: Customize the form for a model:
```html
{% extends "admin/change_form.html" %}
{% block content %}
    <h2>Custom Content Here</h2>
    {{ block.super }}
{% endblock %}
```



## Key Attributes and Methods in ModelAdmin

<h6> 

| Attribute/Method         | Description |
|-------------------------|-------------|
| `list_display` | Specifies fields to display in the list view. |
| `list_display_links` | Fields that link to the detail page. |
| `search_fields` | Enables search functionality on specified fields. |
| `list_filter` | Adds filters to the right sidebar. |
| `ordering` | Defines the default ordering of objects. |
| `prepopulated_fields` | Auto-fills fields (e.g., slugs from titles). |
| `readonly_fields` | Makes certain fields read-only. |
| `date_hierarchy` | Adds hierarchical navigation based on a date field. |
| `inlines` | Allows editing related models in the same form. |
| `actions` | Defines custom admin actions for batch updates. |
| `fieldsets` | Groups fields into sections in the form view. |
| `formfield_overrides` | Changes default widget styles. |
| `get_queryset(self, request)` | Customizes the queryset shown in the admin. |
| `get_list_display(self, request)` | Dynamically modifies `list_display`. |
| `get_readonly_fields(self, request, obj)` | Dynamically sets read-only fields. |

</h6>

## Custom Methods for `list_display`
Instead of displaying related object IDs, you can use custom methods to show related data in the admin list view:

```python
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book_name', 'borrow_date', 'due_date', 'status')
    
    def book_name(self, obj):
        return obj.book.title
    book_name.admin_order_field = 'book__title'  # Enables sorting
    book_name.short_description = 'Book Title'  # Sets column name

admin.site.register(Transaction, TransactionAdmin)
```



## Conclusion
- `admin.ModelAdmin` provides extensive customization options for the Django Admin.
- You can modify list views, filters, search functionality, actions, and more.
- Custom methods improve readability by displaying meaningful data instead of raw IDs.
- The admin panel branding can be personalized for better user experience.

This note should help you master Django's `admin.ModelAdmin`. 🚀 Let me know if you need more details!



## Conclusion
- `admin.py` allows easy management of database models.
- The admin interface can be customized using `ModelAdmin` options.
- Inline administration simplifies managing related models.
- The admin panel branding can be customized with `site_header`, `site_title`, and `index_title`.
- Auto-slug generation can be done via `prepopulated_fields` or `slugify`.
- Custom actions allow batch updates.
- Custom forms and widgets improve UI/UX.
- Admin templates can be overridden for full customization.

