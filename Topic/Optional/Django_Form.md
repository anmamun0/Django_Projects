# Form Explanation


[From.py File Form Explanation](#From-py-File-Form-Explanation)
- [ModelForm এর Meta class](#ModelForm-এর-Meta-class)
- [Custom Methods](#Custom-Methods)
<br>

[View.py File Form Explanation](#View-py-File-Form-Explanation)
  
- [Form inside Parameters form = ContactForm(parametters)](#Form-inside-Parameters)
- [Useful Form APIs Methods ](#useful-forma-apis-methods) <br>
- [Validation Methods is_valid(), cleaned_data ](#2-Validation-Methods) 

[Template File Form usecase](#template-rendering) 


# From.py File Form Explanation  
# ModelForm Methods (Meta class-এর বাইরে)

<h6>

| Method                            | Purpose / Comment                                                |
| --------------------------------- | ---------------------------------------------------------------- |
| `__init__(self, *args, **kwargs)` | Form initialize করার সময় extra customization করতে।              |
| `add_prefix(field_name)`          | Field name-এর prefix add করে।                                    |
| `add_error(field, error)`         | কোনো field এর validation error manually add করতে।                |
| `full_clean()`                    | Form clean এবং validate করে।                                     |
| `clean()`                         | Form level validation করতে।                                      |
| `clean_<fieldname>()`             | Field level validation করতে।                                     |
| `errors`                          | Form validation error dict access করতে।                          |
| `has_changed()`                   | Form data original instance থেকে change হয়েছে কি না check করতে। |
| `changed_data`                    | কোন fields change হয়েছে তার list।                               |
| `is_valid()`                      | Form validate করে boolean return করে।                            |
| `is_bound`                        | True হলে form bind করা হয়েছে (data পাঠানো হয়েছে)               |
| `prepare_value(field, value)`     | Field এর value HTML rendering এর জন্য prepare করে।               |
| `save(commit=True)`               | Form থেকে model instance save করে।                               |
| `validate_unique()`               | Model unique constraints validate করতে।                          |

</h6>

```py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# ModelForm
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    # Form initialization
    def __init__(self, *args, **kwargs):
        # initial, prefix, data, files, instance etc use করা হয়েছে
        self.initial_data = kwargs.get("initial", {})  # initial value
        self.prefix_name = kwargs.get("prefix", None)  # prefix
        self.instance_obj = kwargs.get("instance", None)  # instance
        self.bound_data = kwargs.get("data", None)  # POST/GET data
        self.bound_files = kwargs.get("files", None)  # file data
        super().__init__(*args, **kwargs)

        # HTML attribute customization
        for field in self.fields.values():
            field.widget.attrs["class"] = "border rounded p-2 w-full"
            field.required = True

      return render(request, "profile.html", {"form": form})

```

---
<br>
<br>
<br>


## ModelForm এর Meta class
[Home](#form-explanation)

<h6>

| **Attribute**        | **Purpose / Use Case**                                                                       |
| -------------------- | -------------------------------------------------------------------------------------------- |
| `model`              | যে Model এর সাথে Form link হবে। **অবশ্যই দিতে হয়।**                                          |
| `fields`             | Model এর কোন fields Form-এ ব্যবহার হবে তা নির্ধারণ। যেমন `["name", "email"]` বা `"__all__"`। |
| `exclude`            | কোন fields Form-এ **exclude** করা হবে। `fields` এর সাথে exclusive।                           |
| `widgets`            | কোন field-এর জন্য custom widget সেট করা। যেমন `forms.Textarea(attrs={'rows':3})`।            |
| `labels`             | Field label কাস্টমাইজ করা। যেমন `{'username':'Your Username'}`।                              |
| `help_texts`         | Field-এর জন্য হেল্প টেক্সট। যেমন `{'password':'Must be 8+ chars'}`।                          |
| `error_messages`     | Field-specific custom error messages। যেমন `{'email': {'required':'Email is required'}}`।    |
| `field_classes`      | Field-এর জন্য custom Field class। যেমন `{'name': forms.CharField}`।                          |
| `localized_fields`   | কোন field locale-specific হবে।                                                               |
| `readonly_fields`    | শুধুমাত্র Django Admin এ read-only fields।                                                   |
| `formfield_callback` | Field creation customize করার জন্য callback function।                                        |
| `validators`         | ModelForm লেভেলে custom validation।                                                          |

</h6>

 

```py
from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Required: কোন model এর সাথে Form কাজ করবে
        fields = ['name', 'price', 'description', 'stock', 'category']  # Required: কোন fields show হবে
        exclude = []  # Optional: কোন fields exclude করতে চাও, fields এর সাথে use করা যায় না
        labels = {  # Optional: custom label for each field
            'name': 'Product Name',
            'price': 'Product Price',
        }
        help_texts = {  # Optional: each field এর help text
            'stock': 'Enter number of items available in stock.'
        }
        error_messages = {  # Optional: custom error messages
            'name': {
                'required': 'Product name is mandatory!',
                'max_length': 'Name is too long!'
            }
        }
        widgets = {  # Optional: customize HTML widget
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 20, 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
        field_classes = {  # Optional: custom field class
            'price': forms.DecimalField,
        }
        localized_fields = ('price',)  # Optional: localize specific fields (like number format)
        labels = {'stock': 'Available Stock'}  # Another way to set label
        error_class = forms.utils.ErrorList  # Optional: customize error display class

```

 ---

 <br>
 <br>
 <br>
 <br>


## Custom Methods
[Home](#form-explanation)

<h6>


| Method / Attribute                | Purpose / Use Case                                                           |
| --------------------------------- | ---------------------------------------------------------------------------- |
| `__init__(self, *args, **kwargs)` | ফর্ম ইনিশিয়ালাইজেশনের সময় ফিল্ড কাস্টমাইজ বা dynamic modification।         |
| `add_prefix(self, field_name)`    | ফিল্ডের HTML `name` attribute পরিবর্তন করতে ব্যবহার হয়।                      |
| `prepare_value(self, value)`      | ফিল্ডে প্রদর্শনের আগে value কাস্টমভাবে modify করার জন্য।                     |
| `clean_<fieldname>(self)`         | নির্দিষ্ট ফিল্ডের ভ্যালিডেশন ও modification।                                 |
| `clean(self)`                     | ফর্ম লেভেলের ভ্যালিডেশন বা ফিল্ডগুলোর কাস্টম চেক।                            |
| `add_error(self, field, error)`   | কাস্টমভাবে error যোগ করার জন্য।                                              |
| `full_clean(self)`                | ফর্মের সব ফিল্ড ভ্যালিডেট এবং clean করে।                                     |
| `save(self, commit=True)`         | instance তৈরি/সেভ করার জন্য; override করে কাস্টম save logic ব্যবহার করা যায়। |
| `has_changed(self)`               | ফর্মে কোন ভ্যালু চেঞ্জ হয়েছে কিনা।                                          |
| `changed_data`                    | কোন কোন ফিল্ড চেঞ্জ হয়েছে তা তালিকা আকারে।                                  |
| `errors`                          | ফিল্ড-ভিত্তিক error dictionary।                                              |
| `non_field_errors()`              | ফর্ম লেভেলের error (যেমন clean())।                                           |
| `hidden_fields()`                 | ফর্মের hidden fields।                                                        |
| `visible_fields()`                | ফর্মের visible fields।                                                       |
| `as_p() / as_table() / as_ul()`   | HTML রেন্ডারিং।                                                              |

</h6>


Custom ফিল্ড পরিবর্তনের workflow:
- `__init__ →  ফিল্ড attribute modify (placeholder, CSS class, required, etc.)
- `clean_<field>` → field-specific validation / modify value
- `clean` → multiple field validation / add custom errors
- `prepare_value` → display value before rendering
- `add_prefix` → change HTML name prefix
- `save` → instance save করার আগে custom modify / logic


```py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock']

    # Field-level validation for 'price'
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0")  # Why: ensure price is positive
        return price

    # Field-level validation for 'stock'
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative")  # Why: stock cannot be negative
        return stock

    # Custom prefix for form fields
    def add_prefix(self, field_name):
        # Why: useful when multiple forms in same page to avoid field name collision
        return f"product_{field_name}"

    # Prepare value before rendering in form
    def prepare_value(self, value):
        # Why: convert string values to uppercase for better UI consistency
        if isinstance(value, str):
            return value.upper()
        return value

    # Override save method to add custom logic before saving instance
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Why: automatically add "(Verified)" text to description
        if instance.description:
            instance.description += " (Verified)"
        else:
            instance.description = "No description"
        if commit:
            instance.save()
            self.save_m2m()  # Why: save many-to-many relationships if any
        return instance

    # Check if form fields have changed
    def has_changed(self):
        changed = super().has_changed()
        print("Fields changed:", self.changed_data)  # Why: useful for logging or conditional processing
        return changed

    # Add custom errors manually
    def custom_validation(self):
        # Why: show error for forbidden names
        if self.cleaned_data.get('name') == "Forbidden":
            self.add_error('name', "This name is not allowed")  # add_error lets you attach custom errors to fields

```


**clean_<fieldname>()**
Field-level custom validation.
```py
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if "admin" in name.lower():
            raise forms.ValidationError("Name cannot contain 'admin'")
        return name
```
**clean()**
Form-level custom validation (validate multiple fields together).
```py
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    confirm_email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')

        if email != confirm_email:
            raise forms.ValidationError("Emails do not match!")
```



---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## View py File Form Explanation

[Home](#form-explanation)

<h6>

- [Form inside Parameters form = ContactForm(parametters)](#Form-inside-Parameters)
- [Useful Form APIs Methods ](#useful-forma-apis-methods) <br> 

</h6>

--- 
<br>
<br>

# Form inside Parameters 
[up](#view-py-file-form-explanation)

*views.py*
```py
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
```

```py
form = ContactForm(
    data=None,        # request.POST বা request.GET
    files=None,       # request.FILES (যদি file upload থাকে) যদি শুধু request.POST দেন কিন্তু request.FILES না দেন → file fields সবসময় empty ধরা হবে।
    auto_id='id_%s',  # field input এর জন্য HTML id pattern
    prefix=None,      # multiple forms differentiate করার জন্য | যখন একই page-এ একাধিক একই Form থাকে, তখন differentiate করার জন্য ব্যবহার হয়।
    initial=None,     # initial/default মান | form = ContactForm(initial={'name': 'Mamun', 'email': 'anmamun0@gmail.com'})
    error_class=...,  # custom error rendering class
    label_suffix=None,# label এর শেষে colon (:) এর মতো suffix | form = ContactForm(label_suffix=" →")
    empty_permitted=False # True হলে empty form ও valid হতে পারে
)
```

<h6>

| Parameter         | কবে ব্যবহার করবেন                              |
| ----------------- | ---------------------------------------------- |
| `data`            | form submit হয়েছে (request.POST / request.GET) |
| `files`           | file upload handle করার সময় (request.FILES)    |
| `auto_id`         | HTML input-এর জন্য custom id prefix দরকার হলে  |
| `prefix`          | একই form multiple বার ব্যবহার করলে             |
| `initial`         | default মান pre-fill করতে হলে                  |
| `error_class`     | custom error styling দরকার হলে                 |
| `label_suffix`    | label এর পরে colon `:` customize করতে হলে      |
| `empty_permitted` | form optional করতে হলে                         |

</h6>


---
<br>
<br>
<br>
<br>
<br>
<br>






## Useful Form APIs Methods
[up](#view-py-file-form-explanation)
 
```py
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email'] 
```

1. Rendering Helpers [like](#1-rendering-helpers) → `as_p()`, `as_table()`, `as_ul()`, `visible_fields()`, `hidden_fields()`
2. Field-level Access [like](#1-field-access-in-django-forms) →`fields` , `visible_fields()` , `hidden_fields()`  , `__getitem__(field_name)`, `__iter__()`
3. State [like](##3-validation-methods) →  `is_bound`, `has_changed()`, `changed_data`
4. Validation Methods [like](#3-validation-methods) → `is_valid()`,`save()`, `full_clean()`, `errors`, `add_error()`, `cleaned_data`, errors
5. Override Field Error  [like](#5-override-field-error) → `clean_<field>()` ,`clean()`, 



 
### 1. Rendering Helpers
[Up](#useful-form-apis-methods)


<h6>

| Method       | কাজ                                                                   |
| ------------ | --------------------------------------------------------------------- |
| `as_table()` | ফিল্ডগুলোকে `<tr><th>label</th><td>field</td></tr>` আকারে render করে terminal এ। |
| `as_p()`     | প্রতিটি ফিল্ডকে `<p>` ট্যাগে render করে।                              |
| `as_ul()`    | প্রতিটি ফিল্ডকে `<li>` ট্যাগে render করে।                             |
| `__str__()`  | ডিফল্টভাবে `as_table()` এর মতো কাজ করে।                               |

</h6>

```py
 # Show rendering helpers output in console
form = BlogForm(request.POST)

print("---- Form as table ----")
print(form.as_table())
print("---- Form as paragraph ----")
print(form.as_p())
print("---- Form as unordered list ----")
print(form.as_ul())
```

---
<br>
<br>
<br>


# 2. Field Access in Django Forms
[Up](#useful-form-apis-methods)

<h6>

| Method/Attr               | কাজ                                              |
| ------------------------- | ------------------------------------------------ |
| `fields`                  | list/ Form এর সব field dictionary আকারে দেয়, যেখানে key = field name, value = Field object|
| `visible_fields()`        | renderable fields list করে (hidden বাদ দিয়ে)।    |
| `hidden_fields()`         | শুধু hidden fields return করে (যেমন CSRF token)। |
| `__getitem__(field_name)` | ফর্মের ফিল্ড object access করতে পারে।            |
| `__iter__()`              | for-loop এ ফিল্ড iterate করতে পারেন।             |

</h6>

<br>

**fields**
- Form এর সব field dictionary আকারে দেয়, যেখানে key = field name, value = Field object
```py
form = BlogForm()
print(form.fields)  
# Output: {'title': <django.forms.fields.CharField>, 'content': <django.forms.fields.CharField>}

```
<br>

**visible_fields()**
- কী কাজ করে: Form এর hidden field বাদ দিয়ে সব renderable fields return করে।
```
for field in form.visible_fields():
    print(field.name)
# Output: title, content  (hidden field যেমন CSRF বাদ দিয়ে)

```
<br>

**hidden_fields()**
- কী কাজ করে: শুধু hidden fields return করে। যেমন CSRF token বা hidden input fields।
```py
for field in form.hidden_fields():
    print(field.name)
# Output: csrfmiddlewaretoken
```
<br>

** __getitem__(field_name)**
- কী কাজ করে: Form এর কোনো specific field access করতে পারে।
```py
title_field = form['title']
print(title_field)  # Field object, template এ render করা যায়

# Field access
field = form['title']

# Properties
field.name              # 'title'
field.label             # 'শিরোনাম'
field.html_name         # 'title' or 'prefix-title'
field.id_for_label      # 'id_title'
field.value()           # Current value
field.errors            # Field errors
field.help_text         # Help text
field.is_hidden         # Hidden field কিনা
field.auto_id           # Auto-generated ID
field.field             # Original Field object
field.form              # Parent form object
field.initial           # Initial value
```
<br>

** __iter__()**
- Form কে for-loop দিয়ে iterate করা যায়।
```
for field in form:
    print(field.name, field.value())
```

<br>
<br>
<br>
<br>
<br>


# 3. Validation Methods 
[Up](#useful-form-apis-methods)

<h6>

| Method                    | কাজ                                                                  |
| ------------------------- | -------------------------------------------------------------------- |
| `save(commit=True/False)`  | form save করা       |
| `is_valid()`              | form bound হলে এবং সব validation পাস করলে `True` return করে।         |
| `cleaned_data`       | একটি dict, যেখানে সব validated data থাকে (only after `is_valid()`).   |
| `errors`             | dict/list আকারে সব error messages রাখে।                               |
| `add_error(field, error)` | নির্দিষ্ট ফিল্ডে custom error add করতে ব্যবহার হয়।                   |
| `full_clean()`            | পুরো form এর validation করে (internal use, তবে override করতে পারেন)। |
| `non_field_errors()` | form-level errors (যা কোনো single field-এর সাথে যুক্ত না) return করে। |
| `is_bound`      | form POST/GET data দিয়ে bind হয়েছে কিনা (True/False)। |
| `has_changed()` | ফর্মের কোনো data পরিবর্তিত হয়েছে কিনা।                |
| `changed_data` | list/  কোন fields এর value change হয়েছে তা list হিসেবে দেয় উদাহরণ: ['title', 'content'] | 

</h6>
<br>

**save()**

```py
form = BlogForm(request.POST, request.FILES)
blog = form.save(commit=False)
blog.author = request.user  # কোনো field modify করা যায়
blog.save()                 # এবার save হয় database-এ
```
<br>

**1 is_valid()**
- Checks if the form has no errors and all fields pass validation.
```py
form = ContactForm(request.POST)
if form.is_valid():
    print("Form is valid!")
else:
    print(form.errors)
```
<br>

**2 cleaned_data**

- After is_valid() → contains validated and cleaned data.
```py
if form.is_valid():
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    print(name, email)
```
<br>

**errors**
- Gives all errors in the form in a dictionary.
```py
if not form.is_valid():
    print(form.errors)  
    # Output: {'name': ['This field is required.'], 'email': ['Enter a valid email address.']}
```
<br>

**add_error(field, message)**
- Add custom errors to a field dynamically.
```py
def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        if "test" in form.cleaned_data['name']:
            form.add_error('name', 'Name cannot contain "test"')
            print(form.errors)
```
<br>

**full_clean()**
- Manually run validation on the form. Usually called internally by is_valid().
```py
form = ContactForm(data)
form.full_clean()  # validates the form
print(form.errors)
```
<br>

**non_field_errors()**
- Errors not related to any single field (from clean() method).
```py
if form.non_field_errors():
    print(form.non_field_errors())
# ['Title and content cannot be the same'] # list return করে।
```
<br>

**is_bound**
- Bound মানে ফর্মে data পাঠানো হয়েছে (POST/GET), unbound মানে শুধু empty form
```py
form = BlogForm(request.POST)
if form.is_bound:
    print(form.has_changed())        # True/False
```

**has_changed()**
- Check if form data has changed compared to initial data. True/False
```py
form = ContactForm(request.POST or None, initial={'name': 'Mamun'})
if form.has_changed():
    print("Form data changed:", form.changed_data)
```

<br>

**changed_data()**
- যেই field গুলোর data different সেই field name উল্লেখ করবে।
```py
form = BlogForm(request.POST)
if form.is_bound:
    print(form.has_changed())        # True/False
    print(form.changed_data)        # ['title', 'content']

```

```py
form = BlogForm(request.POST, request.FILES)

# Bound form কিনা (data আছে কিনা)
form.is_bound  # True যদি data pass করা হয়

# Raw submitted data
form.data      # QueryDict: {'title': 'My Blog', 'content': '...'}
form.files     # MultiValueDict: {'image': <InMemoryUploadedFile>}

# Cleaned data (validation এর পরে)
if form.is_valid():
    form.cleaned_data  # {'title': 'My Blog', 'content': '...', 'views': 100}

# Errors
form.errors    # {'title': ['This field is required.']}
form.errors.as_json()  # JSON format এ errors
form.errors.as_text()  # Text format এ errors

# Non-field errors (form level validation errors)
form.non_field_errors()

# Has errors?
form.has_error('title')  # True/False
form.has_error('__all__')  # Form level errors

# Changed data (যে fields change হয়েছে)
form.changed_data  # ['title', 'content']
form.has_changed()  # True/False

# Form এর সব fields
form.fields  # OrderedDict of all form fields

# Base fields (class level definition)
form.base_fields

# Field prefixes
form.prefix  # 'blog1' (যদি set করা থাকে)

# Initial data
form.initial  # {'title': 'Default'}
form.get_initial_for_field(field, field_name)

# Auto ID pattern
form.auto_id  # 'id_%s'

# Label suffix
form.label_suffix  # ':'

# Media (CSS/JS dependencies)
form.media  # CSS and JS files needed by widgets
```

 <br>
 <br>
 <br>
 <br>

 

# 5. Override Field Error
[Up](#useful-form-apis-methods)

<br>

**clean_<field>()**

- Purpose: কোনো specific field এর validation করতে use হয়।
- Automatic call: form validation এর সময় Django নিজে call করে।
- Return value: cleaned (validated) value।
  
```py
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

    # title field validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "badword" in title.lower():
            raise forms.ValidationError("Title contains inappropriate word!")
        return title
```
- এখানে শুধু title field validate হচ্ছে। 
- যদি অন্য field validate করতে চাও → আলাদা clean_<field>() method বানাতে হবে।
<br>

**clean()**
- Purpose: Form-level validation, যেখানে একাধিক field একসাথে check করা হয়।
- Automatic call: form validation এর সময় Django নিজে call করে।
- Return value: cleaned_data dict।

```py
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title == content:
            raise forms.ValidationError("Title and content cannot be the same")
        return cleaned_data
```

- এখানে title এবং content একসাথে validate করা হচ্ছে।
- Error form.non_field_errors() এ যাবে।

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
 
6. Template Rendering 
[Up](#useful-form-apis-methods)
<br>

```html
{% if form.non_field_errors %}
    <ul class="text-red-500">
        {% for error in form.non_field_errors %}
            <li>{{ error }}</li>
        {% endfor %}
    </ul>
{% endif %}
```

```html
# Template এ
{{ form.title }}           # Field এর widget (input tag)
{{ form.title.label }}     # Field এর label
{{ form.title.help_text }} # Help text
{{ form.title.errors }}    # Field errors
{{ form.title.value }}     # Current value
{{ form.title.id_for_label }} # Field এর ID
```


```html
<h2>Create Blog</h2>

<!-- Form-level / Non-field errors -->
{% if form.non_field_errors %}
    <ul class="text-red-500">
    {% for error in form.non_field_errors %}
        <li>{{ error }}</li>
    {% endfor %}
    </ul>
{% endif %}

<form method="post" enctype="multipart/form-data">
    {% csrf_token %}

    <!-- Loop through visible fields -->
    {% for field in form.visible_fields %}
        <div>
            {{ field.label_tag }}<br>
            {{ field }}<br>

            <!-- Field errors -->
            {% if field.errors %}
                <ul class="text-red-500">
                {% for error in field.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
                </ul>
            {% endif %}

            <!-- Help text -->
            {% if field.help_text %}
                <small>{{ field.help_text }}</small>
            {% endif %}
        </div>
    {% endfor %}

    <!-- Hidden fields -->
    {% for hidden in form.hidden_fields %}
        {{ hidden }}
    {% endfor %}

    <button type="submit">Submit</button>
</form>

<!-- Debugging / State info -->
<p>Form is bound: {{ form.is_bound }}</p>
<p>Changed fields: {{ form.changed_data }}</p>

```