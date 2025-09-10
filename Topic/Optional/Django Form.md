# Form Explanation

## Views File Form Explanation

<h6>

 [Useful Form APIs Methods](#-useful-forma-apis-methods) <br>
 [Form inside Parameters](#form-inside-parameters) <br>

</h6>

### Form inside Parameters 
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
```py
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
```
1. Rendering Helpers [like](#-1-rendering-helpers) → as_p(), as_table(), as_ul(), visible_fields(), hidden_fields()
2. Validation Methods [like](#-2-validation-methods) → is_valid(), full_clean(), add_error(), cleaned_data, errors
3. State [like](#-1-rendering-helpers) → is_bound, has_changed(), changed_data
4. Field-level [like](#-1-rendering-helpers) → clean_<field>(), __getitem__()
5. Form-level [like](#-1-rendering-helpers) → clean(), non_field_errors()
 

### 1. Rendering Helpers
<h6>
| Method       | কাজ                                                                   |
| ------------ | --------------------------------------------------------------------- |
| `as_table()` | ফিল্ডগুলোকে `<tr><th>label</th><td>field</td></tr>` আকারে render করে। |
| `as_p()`     | প্রতিটি ফিল্ডকে `<p>` ট্যাগে render করে।                              |
| `as_ul()`    | প্রতিটি ফিল্ডকে `<li>` ট্যাগে render করে।                             |
| `__str__()`  | ডিফল্টভাবে `as_table()` এর মতো কাজ করে।                               |

</h6>

```py
 # ✅ Show rendering helpers output in console
            print("---- Form as table ----")
            print(form.as_table())

            print("---- Form as paragraph ----")
            print(form.as_p())

            print("---- Form as unordered list ----")
            print(form.as_ul())
```

### 2. Validation Methods
<h6>

| Method                    | কাজ                                                                  |
| ------------------------- | -------------------------------------------------------------------- |
| `is_valid()`              | form bound হলে এবং সব validation পাস করলে `True` return করে।         |
| `cleaned_data`       | একটি dict, যেখানে সব validated data থাকে (only after `is_valid()`).   |
| `errors`             | dict/list আকারে সব error messages রাখে।                               |
| `add_error(field, error)` | নির্দিষ্ট ফিল্ডে custom error add করতে ব্যবহার হয়।                   |
| `full_clean()`            | পুরো form এর validation করে (internal use, তবে override করতে পারেন)। |
| `non_field_errors()` | form-level errors (যা কোনো single field-এর সাথে যুক্ত না) return করে। |
| `is_bound`      | form POST/GET data দিয়ে bind হয়েছে কিনা (True/False)। |
| `has_changed()` | ফর্মের কোনো data পরিবর্তিত হয়েছে কিনা।                |

</h6>

**1 is_valid()**
Checks if the form has no errors and all fields pass validation.
```py
form = ContactForm(request.POST)
if form.is_valid():
    print("Form is valid!")
else:
    print(form.errors)
```

**2 cleaned_data**

After is_valid() → contains validated and cleaned data.
```py
if form.is_valid():
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    print(name, email)
```

**errors**
Gives all errors in the form in a dictionary.
```py
if not form.is_valid():
    print(form.errors)  
    # Output: {'name': ['This field is required.'], 'email': ['Enter a valid email address.']}
```

**add_error(field, message)**
Add custom errors to a field dynamically.
```py
def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        if "test" in form.cleaned_data['name']:
            form.add_error('name', 'Name cannot contain "test"')
            print(form.errors)
```

**full_clean()**
Manually run validation on the form. Usually called internally by is_valid().
```py
form = ContactForm(data)
form.full_clean()  # validates the form
print(form.errors)
```

**has_changed()**
Check if form data has changed compared to initial data.
```py
form = ContactForm(request.POST or None, initial={'name': 'Mamun'})
if form.has_changed():
    print("Form data changed:", form.changed_data)
```

**non_field_errors()**
Errors not related to any single field (from clean() method).
```py
if form.non_field_errors():
    print(form.non_field_errors())
```



### 3. Custom Validation Hooks
<h6>

| Method                | কাজ                                                  |
| --------------------- | ---------------------------------------------------- |
| `clean_<fieldname>()` | নির্দিষ্ট ফিল্ডের জন্য custom validation।            |
| `clean()`             | পুরো form-level validation (cross-field validation)। |


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




 


5️⃣ Field Access

<h6>

| Method/Attr               | কাজ                                              |
| ------------------------- | ------------------------------------------------ |
| `fields`                  | dict আকারে সব ফিল্ড।                             |
| `visible_fields()`        | renderable fields list করে (hidden বাদ দিয়ে)।    |
| `hidden_fields()`         | শুধু hidden fields return করে (যেমন CSRF token)। |
| `__getitem__(field_name)` | ফর্মের ফিল্ড object access করতে পারে।            |
| `__iter__()`              | for-loop এ ফিল্ড iterate করতে পারেন।             |

</h6>



</h6>
<h6></h6>


