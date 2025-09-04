# Django admin.py Notes


### Topic of Summary:  

<h6>

| Topic | Description |
|-------|-------------|
| [Auto-Generating Slugs](#1-auto-generating-slugs) | Automatically create URL-friendly slugs from model fields like title or name. Useful for SEO-friendly URLs. |
| [Inline Model Administration](#2-inline-model-administration) | Allows editing related models directly within the parent model in the admin panel. Improves admin workflow. |
| [Customizing the Admin Panel Header](#3-customizing-the-admin-panel-header) | Lets you change the admin site title, header, and index page text for branding purposes. |
| [Adding Custom Actions](#4-adding-custom-actions) | Enables defining custom actions in the admin list view to perform bulk operations on selected objects. |
| [Customizing Form Fields in Admin](#5-customizing-form-fields-in-admin) | Allows overriding default form fields, adding widgets, or making fields read-only for better data control. |
| [Filtering and Search](#6-filtering-and-search) | Adds list filters and search fields to the admin interface to quickly locate objects in large datasets. |
| [Key Attributes and Methods in ModelAdmin](#7-key-attributes-and-methods-in-modeladmin) | Explains important ModelAdmin attributes like `list_display`, `list_filter`, `search_fields`, and methods for customizing admin behavior. |

</h6>

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

<br>
<br>
<br>
<br>

# 1. Auto-Generating Slugs
[Home](#topic-of-summary)

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

<br>
<br>
<br>
<br>

# 2. Inline Model Administration
[Home](#topic-of-summary)

```python
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]

admin.site.register(Book, BookAdmin)
```
- `TabularInline` and `StackedInline` allow editing related objects within the parent model’s admin page.

```py
# models.py
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
```

```python
# admin.py
from django.contrib import admin
from .models import Product, Category

class ProductInline(admin.TabularInline):
    model = Product
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [ProductInline]
```
####  TabularInline কি?

Django admin-এ যখন আপনি একটি related model (one-to-many relationship) কে parent model-এর page-এ inline হিসেবে দেখাতে চান, তখন InlineModelAdmin ব্যবহার করা হয়।

- দুইটি প্রকারের Inline:
 - TabularInline → Table style (row-column) display করে।
 - StackedInline → Vertical stacked box style display করে।
<h6>
    
| Attribute | Explanation                                                        |
| --------- | ------------------------------------------------------------------ |
| `model`   | কোন model inline হিসেবে দেখানো হবে। এখানে `Product`।               |
| `extra`   | কতগুলো empty forms দেখানো হবে নতুন Product add করার জন্য। এখানে 2। |

</h6>

```python
class ProductInline(admin.TabularInline):
    model = Product               # Required: Inline model
    extra = 2                     # 2 empty forms for adding new Products
    max_num = 10                  # Max 10 products allowed in inline
    min_num = 1                   # Minimum 1 product required
    can_delete = True             # Allow deletion of inline products
    fk_name = 'category'          # ForeignKey field to link Category
    readonly_fields = ('created_at', 'updated_at')  # Read-only fields
    fields = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Show only these
    formset = ProductInlineFormSet  # Custom validation formset
    show_change_link = True        # Show link to go to product change page
    ordering = ('-price',)         # Order products by price descending
    verbose_name = "Product Item"
    verbose_name_plural = "Products List"
    template = "admin/edit_inline/tabular.html"  # Default template (can customize)
```


<br>
<br>
<br>
<br>



# 3. Customizing the Admin Panel Header
[Home](#topic-of-summary)

```python
admin.site.site_header = "My Bookstore Admin"
admin.site.site_title = "Bookstore Admin Portal"
admin.site.index_title = "Welcome to the Bookstore Admin"
```

- Bangla Expl.:
 - `site_header` → Browser tab ও top bar এ show হবে।
 - `site_title` → Browser tab title হবে।
 - `index_title` → Dashboard page (home) এ মূল heading।

<br>
<br>
<br>
<br>


# 4. Adding Custom Actions
[Home](#topic-of-summary)

- Admin actions হলো এমন ফিচার যা Django admin list view থেকে multiple objects select করে একসাথে operation perform করতে দেয়।
- Define a custom action to update multiple records at once:
  
- `modeladmin` → এই function কোন ModelAdmin class এর জন্য ব্যবহার হচ্ছে।
- `request` → বর্তমান HTTP request।
- `queryset` → admin list থেকে যেসব row/objects select করা হয়েছে তাদের queryset।
- 
```py
from django.contrib import admin
from .models import Product

@admin.action(description="Mark selected products as published")
def make_published(modeladmin, request, queryset):
    queryset.update(stock=0)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    actions = [make_published]
```

- `queryset.update(...)` → একসাথে multiple row update।
- `@admin.action(description="...")` → dropdown এ দেখানো text।
- `actions list` → ModelAdmin এ add করতে হবে।
- `queryset.update(stock=0)` → এখানে আপনার action যেসব selected products আছে, তাদের stock field কে 0 করে দিবে।


#### 2. Action with Confirmation Page

Django by default একটা confirmation page দেখায় যদি action পরিবর্তন করে data।
```
@admin.action(description="Delete selected products safely")
def safe_delete(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete()
```
Selection → Choose `Safe Delete` → Confirm → Deleted

  
```python
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'total_amount')
    actions = ['mark_as_shipped']

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='Shipped')
    mark_as_shipped.short_description = "Mark selected orders as shipped"

admin.site.register(Order, OrderAdmin)
```

#### 3. Action Returning Response (Redirect or Download)
```python
from django.http import HttpResponse
import csv
 
@admin.action(description="Export selected products to CSV")
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Price'])
    for obj in queryset:
        writer.writerow([obj.id, obj.name, obj.price])
    return response

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    actions = [export_to_csv]
```
 
Action থেকে response return করলে browser এ redirect, download বা অন্য page open করতে পারো।

#### 4. Action with Conditions
```python
@admin.action(description="Apply discount 10% to expensive products")
def discount_expensive(modeladmin, request, queryset):
    for product in queryset:
        if product.price > 100:
            product.price *= 0.9
            product.save()

```
Conditional logic ব্যবহার করে specific objects modify করা যায়।

#### 5. Action for Related Models
```python
@admin.action(description="Mark related category as featured")
def mark_category_featured(modeladmin, request, queryset):
    for product in queryset:
        product.category.is_featured = True
        product.category.save()
```

Related objects (ForeignKey/ManyToMany) modify করা সম্ভব।

#### 6. Using Decorator with Short Description (Old Style)
```python
def make_draft(modeladmin, request, queryset):
    queryset.update(status='draft')
make_draft.short_description = "Mark selected products as draft"
```

পুরানো Django version এ ব্যবহার হয়।

#### 🔹 Summary Table of Action Types

<h6> 

| Action Type       | Example                               | Notes                           |
| ----------------- | ------------------------------------- | ------------------------------- |
| Basic Update      | `queryset.update(status='published')` | Simple field update             |
| Delete            | `queryset.delete()`                   | Deletes selected rows           |
| Download / Export | CSV/Excel export                      | Return `HttpResponse` with file |
| Conditional       | Only modify if condition              | Use `if` inside loop            |
| Related Model     | Modify foreign key or m2m             | Affects related table           |
| Old Style         | `short_description`                   | Compatible with older Django    |

</h6>


<br>
<br>
<br>
<br>



# 5. Customizing Form Fields in Admin
- Use `formfield_overrides` to change widget styles:
```python
from django.forms import Textarea

class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

admin.site.register(Product, ProductAdmin)
```


<br>
<br>
<br>
<br>


# 6. Filtering and Search
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



# 7. Key Attributes and Methods in ModelAdmin

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

