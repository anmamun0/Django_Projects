
# Django Serializers Explanation !Note

### Table of Contents


<h6> 

- [1. Serializer](#1-serializer)  
- [2. ModelSerializer](#2-modelserializer)  
- [3. ModelSerializer এর Attribute ও Field Types](#modelserializer-এর-attribute-ও-field-types)  
- [4. ModelSerializer-এর Meta Class](#modelserializer-এর-meta-class)
- [5. ModelSerializer-এর Override Methods](#modelserializer-এর-override-methods)

</h6>



Django REST Framework Serializers - বিস্তারিত ব্যাখ্যা
... 
[->](#django-rest-framework-serializers---বিস্তারিত-ব্যাখ্যা)

<h6> 
    
- [1. Basic Serializer Example (পাইথন ডাটাকে JSON-এ রূপান্তর করা)](#1-basic-serializer-example-পাইথন-ডাটাকে-json-এ-রূপান্তর-কর)
- [2. Model Serializer (Django মডেল থেকে Serializer তৈরি করা)](#2-model-serializer-django-মডেল-থেকে-serializer-তৈরি-কর)
- [3. ডাটা ভ্যালিডেশন (Validation) in Serializers](#3-ডাটা-ভ্যালিডেশন-validation-in-serializers)
- [4. Serializer দিয়ে মডেল Data Create/Update করা](#4-serializer-দিয়ে-মডেল-data-createupdate-কর)
- [5. Serializer for Nested Data](#5-serializer-for-nested-data)
- [6. Serializer দিয়ে Queryset হ্যান্ডেল করা](#6-serializer-দিয়ে-queryset-হ্যান্ডেল-কর)
- [7. Serializer Fields](#7-serializer-fields)
- [8. ModelSerializer-এ Custom Method Field](#8-modelserializer-এ-custom-method-field)
- [9. Serializer Context ব্যবহার করা](#9-serializer-context-ব্যবহার-কর)
- [10. ModelSerializer এর Common Methods](#10-modelserializer-এর-common-methods)
- 
</h6>



## serializers.ModelSerializer এবং serializers.Serializer এর Different
[Home](#table-of-contents)

Django REST Framework (DRF)-এ serializers.ModelSerializer এবং serializers.Serializer দুইটি গুরুত্বপূর্ণ সিরিয়ালাইজার ক্লাস, তবে এদের কাজ এবং ব্যবহারিক পার্থক্য রয়েছে। নিচে বিস্তারিত ব্যাখ্যা করা হলো:
-  from rest_framework import serializers


ModelSerializer এর গুরুত্বপূর্ণ বিষয়
- Automatic Fields  -  মডেলের উপর ভিত্তি করে ফিল্ড তৈরি হয়
- Customizable Fields	 - extra_kwargs দিয়ে কাস্টমাইজ করা যায়
- Relations Handling	 - StringRelatedField, PrimaryKeyRelatedField, SlugRelatedField, HyperlinkedRelatedField ইত্যাদি
- Validation - ইনবিল্ট ভ্যালিডেশন ও কাস্টম ভ্যালিডেশন সাপোর্ট করে
- Nested Serializers - একাধিক মডেল একসাথে সিরিয়ালাইজ করা যায়
- Authentication Support - CurrentUserDefault ব্যবহার করে ইউজার সেট করা যায়


<br>
<br>
<br>



## 1. Serializer
[Home](#table-of-contents)
- Serializer 👉 ফ্লেক্সিবল ও কাস্টমাইজড (কমপ্লেক্স ডাটা ও কাস্টম ভ্যালিডেশনের জন্য উপযুক্ত)।
  
<h6> 
📌 সংক্ষিপ্ত পরিচিতি:
- এটি pure Python serializer, অর্থাৎ মডেলের সাথে সরাসরি লিঙ্কড নয়।
- ম্যানুয়ালি ফিল্ড ডিফাইন করতে হয় এবং create() ও update() মেথড লিখতে হয়।
- সম্পূর্ণ কাস্টমাইজ করা যায়, তাই এটি ফ্লেক্সিবল।

📌 যখন ব্যবহার করবেন:
- মডেলের সাথে সরাসরি সম্পর্ক ছাড়াই কাস্টম ডাটা সিরিয়ালাইজ করতে হলে।
- যদি কাস্টম ভ্যালিডেশন বা কমপ্লেক্স লজিক দরকার হয়।
- একাধিক মডেলের ডাটা একত্রে সিরিয়ালাইজ করতে হলে।

 
---

<br>
<br>
<br>
<br>



## 2. ModelSerializer
[Home](#table-of-contents)
ModelSerializer 👉 সহজ ও অটোমেটেড (CRUD-এর জন্য উপযুক্ত)।
<h6> 
    
 📌 সংক্ষিপ্ত পরিচিতি:
- এটি Django Model এর উপর ভিত্তি করে কাজ করে।
- কম কোডে স্বয়ংক্রিয়ভাবে সিরিয়ালাইজার তৈরি করা যায়।
- Meta ক্লাসের মাধ্যমে মডেলের সব ফিল্ড সংজ্ঞায়িত করা হয়।
  
📌 যখন ব্যবহার করবেন:
- যখন আপনি একটি Django Model থেকে সরাসরি সিরিয়ালাইজার তৈরি করতে চান।
- CRUD অপারেশন সহজ করতে চাইলে এটি বেস্ট অপশন।
 
```python
from rest_framework import serializers
from .models import Book  # ধরে নিই আমাদের একটি Book মডেল আছে

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # মডেলের নাম উল্লেখ করতে হবে
        fields = '__all__'  # সব ফিল্ড সিরিয়ালাইজ করতে চাই
```
 
- মডেলের উপর ভিত্তি করে স্বয়ংক্রিয়ভাবে সিরিয়ালাইজার তৈরি হয়।
- কোড সংক্ষিপ্ত ও সহজ হয়।
- কম্প্লেক্স লজিক প্রয়োজন না হলে এটি ব্যবহার করা ভালো।
- 
</h6>

  <br>
  <br>
  <br>

```python
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    published_date = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
```
 
- পূর্ণ কাস্টমাইজেশন সম্ভব।
- মডেলের উপর নির্ভরশীল নয়।
- কমপ্লেক্স লজিক ম্যানুয়ালি লিখতে হয়।

</h6>

 

---
<br>
<br>
<br>
<br>

### ModelSerializer এর Attribute ও Field Types
[Home](#table-of-contents)

<h6> 

| Attribute/Field	| ব্যাখ্যা | 
|-------------------|---------| 
| CharField	| টেক্সট ফিল্ড, যেমন: নাম, ঠিকানা ইত্যাদি। | 
| CharField	| Django মডেলের choices অথবা কাস্টম লিস্ট থেকে নির্দিষ্ট অপশন সীমাবদ্ধ করতে ব্যবহার হয়। | 
| IntegerField| 	সংখ্যা গ্রহণ করে (যেমন: বয়স, দাম)। | 
| BooleanField	| True বা False স্টোর করে।| 
| DateField	| তারিখ সংরক্ষণ করে (YYYY-MM-DD ফরম্যাট)।
| DateTimeField| 	তারিখ এবং সময় সংরক্ষণ করে (YYYY-MM-DD HH:MM:SS)। | 
| EmailField| 	ইমেইল ঠিকানা সংরক্ষণ করে এবং ভ্যালিডেশন করে। | 
| SlugField	| স্লাগ (URL-friendly string) সংরক্ষণ করে।  | 
| URLField| 	পূর্ণ ওয়েব ঠিকানা (URL) সংরক্ষণ করে। | 
| UUIDField| 	ইউনিক আইডেন্টিফায়ার (UUID) সংরক্ষণ করে। | 
| FileField| 	ফাইল আপলোড করতে ব্যবহৃত হয়। | 
| ImageField| 	ছবি আপলোড করার জন্য ব্যবহৃত হয়। | 
| JSONField	JSON | ফরম্যাটে ডাটা সংরক্ষণ করতে ব্যবহৃত হয়। | 

</h6>


### 1. StringRelatedField 
[UP](#modelserializer-এর-Attribute-ও-field-types)

- এটি ForeignKey বা ManyToManyField সম্পর্কিত অবজেক্টের __str__() মেথডের আউটপুট রিটার্ন করে।
- ডাটাবেজ আইডি পাঠানোর পরিবর্তে রিডেবল নাম পাঠায়।

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Author এর __str__() রিটার্ন করবে

    class Meta:
        model = Book
        fields = ['title', 'author']
```

### 2. PrimaryKeyRelatedField
[UP](#modelserializer-এর-Attribute-ও-field-types)

- এটি ForeignKey বা ManyToManyField ফিল্ডের জন্য Primary Key (ID) রিটার্ন করে।

```python
class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['title', 'author']
```

### 3. SlugRelatedField 
[UP](#modelserializer-এর-Attribute-ও-field-types)

- এটি ForeignKey সম্পর্কিত মডেলের নির্দিষ্ট স্লাগ ফিল্ড রিটার্ন করে। 
```python
class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='username')

    class Meta:
        model = Book
        fields = ['title', 'author']
```

### 4. HyperlinkedIdentityField 
[UP](#modelserializer-এর-Attribute-ও-field-types)

- এটি প্রতিটি অবজেক্টের ডিটেইল URL লিংক তৈরি করে।
- HyperlinkedModelSerializer-এর সাথে ব্যবহার করা হয়।
  

```python
class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
```

### 5. HyperlinkedRelatedField 
[UP](#modelserializer-এর-Attribute-ও-field-types)

- এটি Related Object-এর লিংক রিটার্ন করে।

```python
class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author']
```

### 6. CurrentUserDefault 
[UP](#modelserializer-এর-Attribute-ও-field-types)

- এটি বর্তমান লগইনকৃত ইউজারকে স্বয়ংক্রিয়ভাবে ফিল্ডে সেট করতে ব্যবহার করা হয়।
```python 
class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
``` 
- author ফিল্ড স্বয়ংক্রিয়ভাবে লগইন করা ইউজার দ্বারা পূরণ হবে।


---

<br>
<br>
<br>
<br>
<br>



# ModelSerializer এর Meta Class
[Home](#table-of-contents)

- Meta class হলো serializer এর configuration layer, যেখানে আমরা ModelSerializer কে বলে দেই:
- কোন model এর উপর serializer বানাতে হবে
- কোন fields include বা exclude করতে হবে
 
### Meta Class Attribute ও Field Types
<h6>
    
| Attribute| 	ব্যাখ্যা| 
|------------| -------| 
| fields| 	সিরিয়ালাইজ করার জন্য ফিল্ড লিস্ট নির্ধারণ করে। __all__ দিলে সব ফিল্ড অন্তর্ভুক্ত হয়। [see more](#1-fields-attribute)   | 
| exclude| 	নির্দিষ্ট কিছু ফিল্ড অপসারণ করতে ব্যবহার করা হয়। [see more](#2-exclude-attribute) | 
| read_only_fields| GET only, POST/PATCH accept করবে না [see more](#3-read_only_fields-attribute)   | 
| write_only_fields| 	POST/PATCH only, GET এ show হবে না (extra_kwargs এও করা যায়) [3. read_only_fields Attribute](#3-read_only_fields-attribute)   | 
| extra_kwargs	| নির্দিষ্ট ফিল্ডের জন্য অতিরিক্ত কনফিগারেশন যোগ করতে ব্যবহৃত হয় , যেমন read_only, write_only, validators, error_messages [see more](#5-extra_kwargs-attribute)	 | 
| depth| 	Nested relationships কত level depth show করবে (ডিফল্ট: 0) [see more](#6-depth-attribute)  | 
| validators | 	কাস্টম ভ্যালিডেশন ফাংশন সংযোজন করা যায়। | 
 
</h6>


```py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # কোন Django model এর data serialize করবে

        # Serializer এ কোন fields include করতে চাই
        # '__all__' দিলে model এর সব field include হবে
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_staff']

        # GET এ দেখানো হবে কিন্তু POST/PATCH এ accept হবে না
        read_only_fields = ['id', 'is_staff']

        # Extra keyword arguments দিয়ে individual field customize করতে পারি
        extra_kwargs = {
            'password': {
                'write_only': True,  # password POST/PATCH only, GET এ show হবে না
                'min_length': 8,     # minimum length validation
                'error_messages': {  # custom error messages
                    'min_length': 'Password must be at least 8 characters'
                }
            },
            'email': {
                'required': True,    # email field POST/PATCH এ বাধ্যতামূলক
                'allow_blank': False,
                'error_messages': {
                    'required': 'Email লাগবেই!'  # custom error message
                }
            },
        }

        # Nested relationships কত level depth show করবে
        # যদি User model এর কোন foreign key থাকে, সেটা automatic nested show হবে
        depth = 1

        # Serializer level custom validators (optional)
        validators = [
            # Example: unique together username + email (DRF automatically User model এ enforce করে)
        ]

```


## 1. **fields** Attribute
[UP](#Meta-class-attribute-ও-field-types)

- `fields = ['username', 'email', 'password']`  # শুধুমাত্র এই field গুলো serializer handle করবে
- `fields = '__all__'` # এটি model এর সব field serializer এ দেখাবে।

## 2. **exclude** Attribute
[UP](#Meta-class-attribute-ও-field-types)

- `exclude = ['last_login', 'is_superuser']`  # এই field গুলো serializer এ দেখাবে না
- exclude = ['password']  # password বাদ, বাকি সব field include <br>
        `extra_kwargs = {'password': {'write_only': True}}`  # password POST এর জন্য write_only

## 3. **read_only_fields** Attribute
[UP](#Meta-class-attribute-ও-field-types)

- `read_only_fields = ['id', 'last_login']`  # এই field update বা create করা যাবে না


## 4. **write_only_fields** Attribute
[UP](#Meta-class-attribute-ও-field-types)

- `write_only_fields = ['password']`  # password GET এ দেখাবে না, Post এ দেখবে
 
## 5. **extra_kwargs** Attribute
[UP](#Meta-class-attribute-ও-field-types)

<h6> 

| Key              | Use Case                                                                               |
| ---------------- | -------------------------------------------------------------------------------------- |
| `read_only`      | Field GET এ দেখাবে কিন্তু POST/PUT/PATCH এ accept করবে না                              |
| `write_only`     | Field POST/PUT/PATCH এ accept করবে কিন্তু GET এ show করবে না (password এর জন্য common) |
| `required`       | Field compulsory কিনা (default=True)                                                   |
| `allow_null`     | Null value accept করবে কিনা                                                            |
| `allow_blank`    | CharField / TextField এ খালি string accept করবে কিনা                                   |
| `default`        | Field missing হলে default value দিতে                                                   |
| `validators`     | Custom validator functions provide করতে                                                |
| `error_messages` | Field-specific validation error message customize করতে                                 |
| `help_text`      | API docs বা serializer documentation এর জন্য help text provide করতে                    |

</h6>
 
*syntex*
```py
extra_kwargs = {
    "field_name": {
        # field-specific options
    },
    "another_field": {
        # options
    }
}
# ------
extra_kwargs = {
    "field_name": {
        "read_only": True,
        "write_only": True,
        "required": False,
        "allow_null": True,
        "allow_blank": True,
        "error_messages": {
            "required": "Field is required!",
            "blank": "Cannot be empty!"
        },
        "validators": [custom_validator_function],
        "default": "Default Value",
    }
}
``` 
- Key: model এর field name
- Value: field-specific options dictionary

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        extra_kwargs = {
            'author': {'read_only': True},   # শুধু পড়া যাবে, আপডেট করা যাবে না
            'published_date': {'required': False},  # এই ফিল্ড অপশনাল হবে
        }
```

### `extra_kwargs` Dictionary এ ব্যবহারযোগ্য parameter গুলো

**read_only**
- Purpose: Field শুধুমাত্র GET response এ দেখানো হবে।
- Example: "email": {"read_only": True}

**write_only**
- Purpose: Field শুধুমাত্র POST/PUT/PATCH এ পাঠানো যাবে, GET response এ দেখাবে না।
- Example: "password": {"write_only": True}

**required**
- Purpose: Field আবশ্যক কি না POST/PUT এ।
- Example: "username": {"required": False}

**default**
- Purpose: যদি POST এ field না থাকে তাহলে default value ব্যবহার হবে।
- Example: "last_name": {"default": "Not Provided"}

**validators**
- Purpose: Custom validation function ব্যবহার করতে। 
- Example: "email": {"validators": [validate_email]} # from django.core.validators import validate_email
- Example: "email": {"validators": [custom_email_validator]} 

```
from rest_framework import serializers
def validate_username(value):
    if "admin" in value.lower():
        raise serializers.ValidationError("Username cannot contain 'admin'.")
    return value

# ---
extra_kwargs = {
    "username": {"validators": [validate_username]}
}
```
 
**help_text**
- Purpose: Documentation বা API Swagger এর জন্য।
- Example: "password": {"help_text": "Enter a strong password"}

**error_messages**
- Purpose: Custom error message দিতে।
- Example: "first_name": {"error_messages": {"required": "First name লাগবেই!"}}

Key (error_key)
- এই key গুলো হলো Django REST Framework বা Django এর field validation এর default error codes। কিছু সাধারণ key:

<h6>

| Key          | Meaning                              |
| ------------ | ------------------------------------ |
| `required`   | Field required, যদি না দেওয়া হয়    |
| `blank`      | Field খালি হলে                       |
| `null`       | Field null হলে (nullable fields)     |
| `invalid`    | Invalid value বা type দিলে           |
| `max_length` | Field length max limit অতিক্রম করলে  |
| `min_length` | Field length min limit পূরণ না করলে  |
| `max_value`  | Numeric field max value অতিক্রম করলে |
| `min_value`  | Numeric field min value পূরণ না করলে |
| `unique`     | Unique constraint fail করলে          |

    
</h6>

```py
first_name = serializers.CharField(
    required=True,
    allow_blank=False,
    error_messages={
        "required": "First name লাগবেই!",
        "blank": "First name খালি রাখা যাবে না।",
        "max_length": "First name অনেক বড়!"
    }

```

**allow_blank**
- Purpose: CharField বা TextField এ খালি string allow করা।
- Example: "username": {"allow_blank": True}

**allow_null**
- Purpose: Field এ Null value allow করা।
- Example: "first_name": {"allow_null": True}

**max_length**, **min_length**
- Purpose: String field এর max/min length validation।
- Example: "username": {"max_length": 50, "min_length": 3}

**trim_whitespace**
- Purpose: Field এর string value trim করবে POST/PUT এ।
- Example: "username": {"trim_whitespace": True} 



## 6. **depth** Attribute 
[UP](#Meta-class-attribute-ও-field-types)

- depth ব্যবহার করা হয় nested relationships কে automatically expand করে দেখানোর জন্য। অর্থাৎ foreign key বা related object এর full details nested structure হিসেবে দেখানো যায়।

```py
class Meta:
    model = YourModel
    fields = '__all__'
    depth = 1  # 1 level nested relation দেখাবে
```

Purpose
- Related objects সহজে view করার জন্য।
- ForeignKey, OneToOneField, ManyToManyField কে nested JSON হিসেবে দেখতে চাইলে।

Behavior
- depth=0 → Related object শুধু primary key দেখাবে।
- depth=1 → Related object এর সব field দেখাবে।
- depth=2 → Related object এর nested object পর্যন্ত দেখাবে।

```py
# models.py
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# serializers.py
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
```

যদি depth=1 হলে, author এর সব fields দেখাবে:
```json
{
    "id": 1,
    "title": "Django for Beginners",
    "author": {
        "id": 1,
        "name": "John Doe"
    }
}
```



---

<br>
<br>
<br>
<br>
<br>

## ModelSerializer এর Override Methods
[Home](#table-of-contents)
 
<h6>
 
| Method                | Use Case                                 |
| --------------------- | ---------------------------------------- |
| `create()`            | Save new object with custom logic        |
| `update()`            | Update existing object with custom logic |
| `validate_<field>()`  | Single field validation                  |
| `validate()`          | Multi-field validation                   |
| `to_representation()` | Customize output JSON                    |
| `to_internal_value()` | Customize input parsing                  |
| `run_validation()`    | Manually run validation chain            |

</h6>


### 1. create(self, validated_data)
[Up](#ModelSerializer-এর-Override-Methods)
 
- নতুন object database এ save করার জন্য।
- ModelSerializer হলে default automatically create করবে, কিন্তু custom behavior দরকার হলে override করা যায়।

```py
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # hashed password
        user.save()
        return user
``` 
Password hash করার জন্য, অথবা extra fields handle করার জন্য।

### 2.  update(self, instance, validated_data)
[Up](#ModelSerializer-এর-Override-Methods)
 
- Existing object update করার জন্য।
```py
def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    password = validated_data.get('password', None)
    if password:
        instance.set_password(password)
    instance.save()
    return instance
```
Custom update logic যেমন password hashing বা computed fields।

### 3. validate_<field_name>(self, value)
[Up](#ModelSerializer-এর-Override-Methods)
- Field-level validation করার জন্য।
```py
def validate_email(self, value):
    if "@example.com" not in value:
        raise serializers.ValidationError("Email must be from example.com")
    return value
``` 
Single field এর specific validation করতে।

### 4. validate(self, data)
[Up](#ModelSerializer-এর-Override-Methods)
- Serializer-level validation।
- একাধিক field একসাথে validate করা যায়।
```py
def validate(self, data):
    if data['password'] != data['password2']:
        raise serializers.ValidationError("Passwords must match!")
    return data
``` 
Multi-field consistency check (e.g., password confirmation)।

### 5. to_representation(self, instance)
[Up](#ModelSerializer-এর-Override-Methods)
- Object কে Python dict → JSON convert করার জন্য।
- Output customize করতে পারে।
```py
def to_representation(self, instance):
    rep = super().to_representation(instance)
    rep['full_name'] = f"{instance.first_name} {instance.last_name}"
    return rep
``` 
Output JSON customize করার জন্য।

### 6. to_internal_value(self, data)
[Up](#ModelSerializer-এর-Override-Methods)
- Incoming JSON → Python dict convert করার জন্য।
- Mostly advanced use, custom parsing দরকার হলে।
```py
def to_internal_value(self, data):
    internal = super().to_internal_value(data)
    internal['username'] = internal['username'].lower()
    return internal
```
 
Input normalize করার জন্য (যেমন username lowercase)।

### 7. run_validation(self, data)
[Up](#ModelSerializer-এর-Override-Methods)
- Serializer এর validation chain manually run করার জন্য।
- Mostly internal, rare use case।
















---
<br>
<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

 


# Django REST Framework Serializers - বিস্তারিত ব্যাখ্যা

Serializers Django REST Framework (DRF)-এর একটি গুরুত্বপূর্ণ অংশ যা Django মডেল ইনস্ট্যান্স বা কুয়েরিসেটকে JSON, XML বা অন্যান্য ফরম্যাটে রূপান্তর করতে সাহায্য করে। এছাড়াও এটি ডাটা ভ্যালিডেশন নিশ্চিত করে।

---

## 1. **Basic Serializer Example** (পাইথন ডাটাকে JSON-এ রূপান্তর করা)

```python
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()

user_data = {'username': 'john_doe', 'email': 'john@example.com', 'is_active': True}
serializer = UserSerializer(data=user_data)

if serializer.is_valid():
    validated_data = serializer.validated_data
    print(validated_data)  # {'username': 'john_doe', 'email': 'john@example.com', 'is_active': True}
else:
    print(serializer.errors)
```

---

## 2. **Model Serializer** (Django মডেল থেকে Serializer তৈরি করা)

```python
from rest_framework import serializers
from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
```

**`ModelSerializer`** ব্যবহার করলে মডেলের ফিল্ড অনুযায়ী অটোমেটিক সিরিয়ালাইজেশন হয়।

---
<br>
<br>
<br>
<br>

## 3. **ডাটা ভ্যালিডেশন (Validation) in Serializers**

### **Field-Level Validation**
```python
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)

    def validate_username(self, value):
        if " " in value:
            raise serializers.ValidationError("Username-এ স্পেস থাকতে পারবে না।")
        return value
```

### **Object-Level Validation**
```python
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate(self, data):
        if data['username'] == data['email']:
            raise serializers.ValidationError("Username এবং email এক হতে পারবে না।")
        return data
```

---

## 4. **Serializer দিয়ে মডেল Data Create/Update করা**
```python
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

user_data = {'username': 'john_doe', 'email': 'john@example.com'}
serializer = UserModelSerializer(data=user_data)

if serializer.is_valid():
    user = serializer.save()  # নতুন User তৈরি করবে
    print(f"User created: {user}")
else:
    print(serializer.errors)
```

---

## 5. **Serializer for Nested Data** (নেস্টেড অবজেক্ট সিরিয়ালাইজ করা)
```python
class AddressSerializer(serializers.Serializer):
    street = serializers.CharField()
    city = serializers.CharField()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    address = AddressSerializer()
```

✅ **নেস্টেড Serializer ব্যবহার করে সম্পর্কিত মডেল বা অবজেক্টের ডাটা একসাথে সিরিয়ালাইজ করা যায়।**

---

## 6. **Serializer দিয়ে Queryset হ্যান্ডেল করা**
```python
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

users = User.objects.all()
serializer = UserModelSerializer(users, many=True)
print(serializer.data)  # List আকারে Serialized Output
```

✅ **`many=True` দিলে একাধিক অবজেক্ট সিরিয়ালাইজ করা যায়।**

---

## 7. **Serializer Fields** (বিভিন্ন ফিল্ড টাইপ)
```python
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
```

✅ **DRF-এর `CharField`, `IntegerField`, `EmailField`, `BooleanField` ইত্যাদি ফিল্ড ব্যবহার করে বিভিন্ন ডাটা টাইপ নির্ধারণ করা যায়।**

---

## 8. **ModelSerializer-এ Custom Method Field**
```python
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
```

✅ **`SerializerMethodField()` দিয়ে কাস্টম ডাটা জেনারেট করা যায়।**

---

## 9. **Serializer Context ব্যবহার করা**
```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

extra_data = {'custom_param': 'some_value'}
serializer = UserSerializer(user_instance, context=extra_data)
```

✅ **`context` ব্যবহার করে কাস্টম ডাটা পাঠানো যায়।**

---

 

## **ModelSerializer এর Common Methods**

### **Create Method (নতুন Object তৈরি করা)**
```python
def create(self, validated_data):
    return MyModel.objects.create(**validated_data)
```

### **Update Method (Object আপডেট করা)**
```python
def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.save()
    return instance
```

### **Custom Representation Method (Output কাস্টমাইজ করা)**
```python
def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['extra_field'] = 'Custom Data'
    return representation
```

✅ **এই পদ্ধতিগুলো ModelSerializer-এ ডাটা প্রসেস করার জন্য খুবই গুরুত্বপূর্ণ।**

---

### 🎯 **সংক্ষেপে মূল বিষয়:**
- ✔ **Field-Level Validation:** `validate_<field_name>` মেথড ব্যবহার করুন। <br> 
- ✔ **Object-Level Validation:** `validate(self, data)` ব্যবহার করে অবজেক্ট ভ্যালিডেশন করুন।
- ✔ **Write Operations:** `save()` মেথড ব্যবহার করে নতুন অবজেক্ট তৈরি করুন বা আপডেট করুন।
- ✔ **Nested Data:** নেস্টেড Serializer ব্যবহার করুন।
- ✔ **Custom Fields:** `SerializerMethodField()` দিয়ে কাস্টম ফিল্ড তৈরি করুন।


---

<br>
<br>

### Custom Field created with funciton/method

`serializers.py`
```python
class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    total_book_read = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_total_book_read(self, obj):
        return obj.profile_transactions.filter(status='returned').count()

    def get_rating(self, obj):
        total = self.get_total_book_read(obj)
        return min(5, int((total / 100) * 5))  # ensure max rating is 5
    
    def get_last_login(self,obj):
        return obj.user.last_login if obj.user else None
    def get_is_active(self,obj):
        return obj.user.is_active if obj.user else None
```

`models.py`
```python
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    image = models.URLField(max_length=255,null=True,blank=True,default='https://www.w3schools.com/howto/img_avatar.png')
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10,choices=USER_ROLE,default='student')
    phone = models.CharField(max_length=14,unique=True)
    email = models.CharField(max_length=50,unique=True)
    
    roll = models.CharField(max_length=8,unique=True,null=True,blank=True)
    registration = models.CharField(max_length=40,unique=True,null=True,blank=True)
    department = models.CharField(max_length=12,null=True,blank=True)
    session = models.CharField(max_length=4,null=True,blank=True)
    address = models.CharField(max_length=100)
    blood = models.CharField(choices=STATUS_BLOOD,max_length=10,null=True,blank=True)
    gender = models.CharField(choices=STATUS_GENDER,max_length=10,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)

    nationality_type = models.CharField(max_length=10,choices=NATIONALITY)
    nationality_number = models.CharField(max_length=17,unique=True)
 


    def __str__(self):
        return f"{self.roll} - {self.session}"
class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,related_name='profile_transactions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="book_transactions")
    request_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    due_date = models.IntegerField(choices=STATUS_DUE, default=7,null=True,blank=True) 

    borrow_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending') 
```

### 🔰 serializers.ModelSerializer এর সব methods (Built-in)

`ModelSerializer`→ `inherits from Serializer` → `inherits from BaseSerializer` → `inherits from object`

#### ✅ 1. __init__(self, instance=None, data=empty, **kwargs)

instance: model instance, e.g. object from database (for read/update)
data: input data (for create/update)
context: dictionary, usually request context ({'request': request})
many: Boolean, multiple objects serialize হবে কিনা

🔹 Use-case:
```python 
serializer = UserSerializer(data=request.data, context={'request': request})
# Data Represented: Input data বা instance থেকে ডেটা।
```


#### ✅ 2. create(self, validated_data)

validated_data: validated form of data

```
def create(self, validated_data):
    # validated_data হচ্ছে dict → {'name': 'Phone', 'price': 10000, 'quantity': 5}
    return User.objects.create(**validated_data)

def create(self, validated_data):
        user = self.context['request'].user  # কনটেক্সট থেকে ইউজার ধরলাম
        product = Product.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            quantity=validated_data['quantity'],
            created_by=user
        )
        return product
```
🔹 Data Represented: New object তৈরি করার জন্য validated dict।

#### ✅ 3. update(self, instance, validated_data)

instance: model instance to update
validated_data: new data

```
def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.save()
    return instance
```
🔹 Data Represented: Object আপডেট করার ডেটা।

#### ✅ 4. to_representation(self, instance)

instance: model instance

```
def to_representation(self, instance):
    rep = super().to_representation(instance)
    rep['full_name'] = instance.first_name + " " + instance.last_name
    return rep
```
🔹 Data Represented: কিভাবে ডেটা serialize হবে। Output কাস্টমাইজ করতে

#### ✅ 5. to_internal_value(self, data)

data: raw input data

```
def to_internal_value(self, data):
    data = super().to_internal_value(data)
    data['username'] = data['username'].lower()
    return data
```
🔹 Data Represented: কিভাবে raw data model field-এ map হবে। Input ডেটা কাস্টমভাবে process করা

#### ✅ ৬. validate(self, attrs)
attrs: all validated fields as dict

```
def validate(self, attrs):
    if attrs['start'] > attrs['end']:
        raise serializers.ValidationError("End must come after start")
    return attrs
```

🔹 Data Represented: ফিল্ডের উপর নির্ভরশীল validation

#### ✅ ৭. validate_<field>(self, value)
value: field-specific value
```
def validate_email(self, value):
    if "spam" in value:
        raise serializers.ValidationError("Invalid email")
    return value
```
🔹 Data Represented: নির্দিষ্ট ফিল্ডের validation data



### 🔰 serializers.Serializer এর সব methods (Built-in)

| Method              | ব্যবহার                  |
| ------------------- | ------------------------ |
| `validate_<field>`  | ফিল্ড লেভেল চেক          |
| `validate`          | সব ফিল্ড একসাথে চেক      |
| `create`            | নতুন object তৈরি         |
| `update`            | পুরাতন object আপডেট      |
| `to_representation` | output customize         |
| `to_internal_value` | input customize (কমন নয়) |