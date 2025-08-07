## 📌 Table of Contents

<h6> 

- [serializers.ModelSerializer এবং serializers.Serializer এর ব্যাখ্যা](#serializersmodelserializer-এবং-serializers.serializer-এর-ব্যাখ্যা)
- [🔹 1. serializers.ModelSerializer](#-1-serializersmodelserializer)
- [🔹 2. serializers.Serializer](#-2-serializersserializer)
- [📌 ModelSerializer এর গুরুত্বপূর্ণ Attribute ও Field Types](#-modelserializer-এর-গুরুত্বপূর্ণ-attribute-ও-field-types)
- [📌 ModelSerializer-এর Special Fields](#-modelserializer-এর-special-fields)
- [1️⃣ StringRelatedField](#1️⃣-stringrelatedfield)
- [2️⃣ PrimaryKeyRelatedField](#2️⃣-primarykeyrelatedfield)
- [3️⃣ SlugRelatedField](#3️⃣-slugrelatedfield)
- [4️⃣ HyperlinkedIdentityField](#4️⃣-hyperlinkedidentityfield)
- [5️⃣ HyperlinkedRelatedField](#5️⃣-hyperlinkedrelatedfield)
- [6️⃣ CurrentUserDefault](#6️⃣-currentuserdefault)
- [📌 extra_kwargs দিয়ে কাস্টমাইজেশন](#extra_kwargs-দিয়ে-কাস্টমাইজেশন)

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


### serializers.ModelSerializer এবং serializers.Serializer এর ব্যাখ্যা

Django REST Framework (DRF)-এ serializers.ModelSerializer এবং serializers.Serializer দুইটি গুরুত্বপূর্ণ সিরিয়ালাইজার ক্লাস, তবে এদের কাজ এবং ব্যবহারিক পার্থক্য রয়েছে। নিচে বিস্তারিত ব্যাখ্যা করা হলো:

###### from rest_framework import serializers

## 🔹 1. serializers.ModelSerializer
ModelSerializer 👉 সহজ ও অটোমেটেড (CRUD-এর জন্য উপযুক্ত)।
<h6> 
    
 📌 সংক্ষিপ্ত পরিচিতি:
- এটি Django Model এর উপর ভিত্তি করে কাজ করে।
- কম কোডে স্বয়ংক্রিয়ভাবে সিরিয়ালাইজার তৈরি করা যায়।
- Meta ক্লাসের মাধ্যমে মডেলের সব ফিল্ড সংজ্ঞায়িত করা হয়।
  
📌 যখন ব্যবহার করবেন:
- যখন আপনি একটি Django Model থেকে সরাসরি সিরিয়ালাইজার তৈরি করতে চান।
- CRUD অপারেশন সহজ করতে চাইলে এটি বেস্ট অপশন।

📌 উদাহরণ:
```python
from rest_framework import serializers
from .models import Book  # ধরে নিই আমাদের একটি Book মডেল আছে

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # মডেলের নাম উল্লেখ করতে হবে
        fields = '__all__'  # সব ফিল্ড সিরিয়ালাইজ করতে চাই
```

✅ বৈশিষ্ট্য:
- মডেলের উপর ভিত্তি করে স্বয়ংক্রিয়ভাবে সিরিয়ালাইজার তৈরি হয়।
- কোড সংক্ষিপ্ত ও সহজ হয়।
- কম্প্লেক্স লজিক প্রয়োজন না হলে এটি ব্যবহার করা ভালো।
- 
</h6>

## 🔹 2. serializers.Serializer
Serializer 👉 ফ্লেক্সিবল ও কাস্টমাইজড (কমপ্লেক্স ডাটা ও কাস্টম ভ্যালিডেশনের জন্য উপযুক্ত)।
<h6> 
📌 সংক্ষিপ্ত পরিচিতি:
- এটি pure Python serializer, অর্থাৎ মডেলের সাথে সরাসরি লিঙ্কড নয়।
- ম্যানুয়ালি ফিল্ড ডিফাইন করতে হয় এবং create() ও update() মেথড লিখতে হয়।
- সম্পূর্ণ কাস্টমাইজ করা যায়, তাই এটি ফ্লেক্সিবল।

📌 যখন ব্যবহার করবেন:
- মডেলের সাথে সরাসরি সম্পর্ক ছাড়াই কাস্টম ডাটা সিরিয়ালাইজ করতে হলে।
- যদি কাস্টম ভ্যালিডেশন বা কমপ্লেক্স লজিক দরকার হয়।
- একাধিক মডেলের ডাটা একত্রে সিরিয়ালাইজ করতে হলে।

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

✅ বৈশিষ্ট্য:
- পূর্ণ কাস্টমাইজেশন সম্ভব।
- মডেলের উপর নির্ভরশীল নয়।
- কমপ্লেক্স লজিক ম্যানুয়ালি লিখতে হয়।

</h6>

 

---
<br>
<br>
<br>
<br>

### 📌 ModelSerializer এর গুরুত্বপূর্ণ Attribute ও Field Types

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

📌 ModelSerializer-এর গুরুত্বপূর্ণ Attribute ব্যাখ্যা
<h6>
    
| Attribute| 	ব্যাখ্যা| 
|------------| -------| 
| fields| 	সিরিয়ালাইজ করার জন্য ফিল্ড লিস্ট নির্ধারণ করে। __all__ দিলে সব ফিল্ড অন্তর্ভুক্ত হয়। | 
| exclude| 	নির্দিষ্ট কিছু ফিল্ড অপসারণ করতে ব্যবহার করা হয়। | 
| read_only_fields| 	এই ফিল্ডগুলো কেবলমাত্র রিড-অনলি হবে, মডিফাই করা যাবে না। | 
| extra_kwargs	| নির্দিষ্ট ফিল্ডের জন্য অতিরিক্ত কনফিগারেশন যোগ করতে ব্যবহৃত হয়। | 
| depth| 	নেস্টেড সিরিয়ালাইজারের গভীরতা নির্ধারণ করে। (ডিফল্ট: 0) | 
| validators| 	কাস্টম ভ্যালিডেশন ফাংশন সংযোজন করা যায়। | 


</h6>


## 📌 ModelSerializer-এর Special Fields
এগুলো বিশেষ কিছু ক্ষেত্রে ব্যবহার করা হয়।

## 1️⃣ StringRelatedField
✅ ব্যাখ্যা:

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

## 2️⃣ PrimaryKeyRelatedField
✅ ব্যাখ্যা:
- এটি ForeignKey বা ManyToManyField ফিল্ডের জন্য Primary Key (ID) রিটার্ন করে।

```python
class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['title', 'author']
```

## 3️⃣ SlugRelatedField

✅ ব্যাখ্যা:
- এটি ForeignKey সম্পর্কিত মডেলের নির্দিষ্ট স্লাগ ফিল্ড রিটার্ন করে।
- 
```python
class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='username')

    class Meta:
        model = Book
        fields = ['title', 'author']
```

## 4️⃣ HyperlinkedIdentityField
✅ ব্যাখ্যা:
- এটি প্রতিটি অবজেক্টের ডিটেইল URL লিংক তৈরি করে।
- HyperlinkedModelSerializer-এর সাথে ব্যবহার করা হয়।
  

```python
class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
```

## 5️⃣ HyperlinkedRelatedField

✅ ব্যাখ্যা:
- এটি Related Object-এর লিংক রিটার্ন করে।

```python
class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author']
```

## 6️⃣ CurrentUserDefault

✅ ব্যাখ্যা:
- এটি বর্তমান লগইনকৃত ইউজারকে স্বয়ংক্রিয়ভাবে ফিল্ডে সেট করতে ব্যবহার করা হয়।
```python 
class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
```
📌 ফলাফল:

- author ফিল্ড স্বয়ংক্রিয়ভাবে লগইন করা ইউজার দ্বারা পূরণ হবে।
  
## extra_kwargs দিয়ে কাস্টমাইজেশন
- ✅ কিছু ফিল্ডকে read_only, write_only, required, validators ইত্যাদি সেট করা যায়।

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

✅ সংক্ষেপে ModelSerializer এর গুরুত্বপূর্ণ বিষয়

| Feature	| Description| 
|-----------|------------|
| Automatic Fields	| মডেলের উপর ভিত্তি করে ফিল্ড তৈরি হয়| 
| Customizable Fields	| extra_kwargs দিয়ে কাস্টমাইজ করা যায়| 
| Relations Handling	| StringRelatedField, PrimaryKeyRelatedField, SlugRelatedField, HyperlinkedRelatedField ইত্যাদি| 
| Validation | 	ইনবিল্ট ভ্যালিডেশন ও কাস্টম ভ্যালিডেশন সাপোর্ট করে| 
| Nested Serializers| 	একাধিক মডেল একসাথে সিরিয়ালাইজ করা যায়| 
| Authentication Support	|  CurrentUserDefault ব্যবহার করে ইউজার সেট করা যায়| 


---
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

✅ **`ModelSerializer`** ব্যবহার করলে মডেলের ফিল্ড অনুযায়ী অটোমেটিক সিরিয়ালাইজেশন হয়।

---

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

## **ModelSerializer এর বিশেষ অপশন**
- `fields = '__all__'` → সকল ফিল্ড অন্তর্ভুক্ত করে।
- `exclude = ['password']` → নির্দিষ্ট ফিল্ড বাদ দেয়।
- `read_only_fields = ['id']` → শুধুমাত্র রিড-অনলি ফিল্ড নির্ধারণ করে।
- `extra_kwargs = {'email': {'required': True}}` → অতিরিক্ত ফিল্ড কনফিগারেশন।

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


serializers.py
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

