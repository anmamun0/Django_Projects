Django Signals হলো একটি শক্তিশালী ফিচার যা বিভিন্ন ইভেন্টের উপর ভিত্তি করে বিভিন্ন অ্যাকশন ট্রিগার করতে সাহায্য করে। এটি মূলত Django অ্যাপ্লিকেশনের মধ্যে ডিকপ্লিং (decoupling) এবং ইভেন্ট-ড্রিভেন (event-driven) প্রোগ্রামিং করার জন্য ব্যবহৃত হয়।

## Django Signals কী?
##### Django Signals মূলত অফলাইন বা ব্যাকগ্রাউন্ড প্রসেস পরিচালনার জন্য ব্যবহৃত হয়। যখন কোনও নির্দিষ্ট ঘটনা ঘটে, তখন সিগন্যাল ট্রিগার হয় এবং আপনি সেটির সাথে সংযুক্ত একটি ফাংশনকে চালু করতে পারেন।

## Signal কিভাবে কাজ করে?
##### Django Signals হল একটি Publisher-Subscriber pattern। একটি signal (Publisher) অন্য কোড (Subscriber) কে জানাতে পারে যে একটি নির্দিষ্ট ঘটনা ঘটেছে।

### প্রধান Components:
- Signal: এটি সেই ইভেন্ট বা ঘটনা যা ঘটলে সিগন্যাল ট্রিগার হবে। উদাহরণস্বরূপ, একটি নতুন ইউজার তৈরি হওয়া বা একটি মডেল সেভ হওয়া।

- Receiver: এটি সেই ফাংশন বা মেথড যা signal প্রাপ্ত হলে কার্যকর হবে। এটি নির্দিষ্ট ঘটনা ঘটার পর আপনাকে যা করতে হবে তা পরিচালনা করবে।

- Sender: এটি সেই সত্তা যা signal পাঠায়, যেমন মডেল, ভিউ বা অন্য কিছু।

### Signal Register ও Connect:
- Signal Definition: Django signals মডিউল থেকে একটি সিগন্যাল তৈরি করা হয়।

- Receiver Function: এটি signal ট্রিগার হলে চালানোর জন্য একটি ফাংশন তৈরি করা হয়।

- Connect Signal to Receiver: signal এবং receiver কে সংযুক্ত করতে connect() মেথড ব্যবহার করা হয়।

### Signal ব্যবহার করার উদাহরণ:
##### ধরা যাক, আপনি একটি User মডেল তৈরি করেছেন এবং চান যখন একটি নতুন User তৈরি হবে, তখন একটি ইমেইল পাঠানো হবে। এটি Django Signal দিয়ে করা যেতে পারে।

```python 
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # যদি নতুন ইউজার তৈরি হয়
        send_mail(
            'Welcome to Our Platform!',
            'Thank you for signing up.',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
```
এখানে:

- post_save signal ব্যবহার করা হয়েছে, যা User মডেল সেভ হওয়ার পর ট্রিগার হবে।
- send_welcome_email একটি receiver function যা সিগন্যাল প্রাপ্ত হলে ইমেইল পাঠাবে।

##### Signal Registration:
- Signal কে apps.py ফাইলের AppConfig ক্লাসের মাধ্যমে রেজিস্টার করতে হয়:

```python 
# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # signals.py ফাইলটি ইমপোর্ট করা হচ্ছে
```

Django Signals-এর অন্যান্য উদাহরণ:

- pre_save: কোন মডেল সেভ হওয়ার আগে সিগন্যাল ট্রিগার হয়।
- post_save: কোন মডেল সেভ হওয়ার পর সিগন্যাল ট্রিগার হয়।
- pre_delete: কোন মডেল ডিলিট হওয়ার আগে সিগন্যাল ট্রিগার হয়।
- post_delete: কোন মডেল ডিলিট হওয়ার পর সিগন্যাল ট্রিগার হয়।

## Signal কীভাবে ব্যবহার উপকারী?
- ডিকপ্লিং: আপনার কোডের মধ্যে সিগন্যাল ব্যবহারের মাধ্যমে আপনি কোডকে আলাদা রাখতে পারেন এবং একে অপরের উপর নির্ভরশীল না করে আলাদা কাজ করতে পারেন।

- এন্টি-প্যাটার্ন এড়ানো: আপনি যখন বিভিন্ন মডিউল থেকে একে অপরকে কল করেন, তখন কোডের পুনরাবৃত্তি এবং জটিলতা বাড়ে। সিগন্যাল ব্যবহারের মাধ্যমে এটি এড়ানো সম্ভব।

- এনহ্যান্সড ইউজার এক্সপেরিয়েন্স: উদাহরণস্বরূপ, সিগন্যাল ব্যবহার করে আপনি ইউজার লগইন বা রেজিস্ট্রেশনের পরে ইমেইল পাঠাতে পারেন, যা ইউজারের অভিজ্ঞতা বাড়াতে সাহায্য করে।

সমাপ্তি:
Django Signals আপনাকে কোডের মধ্যে একটি ডিকপ্লড আর্কিটেকচার তৈরি করতে সাহায্য করে, যা বড় অ্যাপ্লিকেশনে খুবই কার্যকরী। Signals ব্যবহারের মাধ্যমে, আপনি বিশেষ কিছু ইভেন্টের উপর ভিত্তি করে অ্যাকশন নিতে পারেন, যা Django অ্যাপ্লিকেশনটিকে আরও দক্ষ এবং পরিষ্কার করে তোলে।





  
###### Django-তে signals ব্যবহারের মাধ্যমে, আপনি বিভিন্ন ইভেন্টের উপর ভিত্তি করে কোড কার্যকর করতে পারেন, যেমন মডেল সেভ হওয়া, মডেল ডিলিট হওয়া, ভিউ কল হওয়া, ইত্যাদি। এটি Django অ্যাপ্লিকেশনগুলোর মধ্যে ডিকপ্লিং (decoupling) করতে সাহায্য করে, অর্থাৎ বিভিন্ন অংশের মধ্যে নির্ভরশীলতা কমায়।

##### Django Signals-এর প্রকারভেদ:
###### Django-তে বিভিন্ন ধরনের সিগন্যাল রয়েছে, যেগুলো বিভিন্ন ইভেন্টের উপর ভিত্তি করে ট্রিগার হয়। নিচে কিছু গুরুত্বপূর্ণ Django signals এবং তাদের ব্যাখ্যা দেয়া হল:

## 1. pre_save Signal

- Use Case: মডেল সেভ হওয়ার আগে কিছু পরিবর্তন বা যাচাইকরণ করা।
- pre_save সিগন্যালটি তখন ট্রিগার হয় যখন মডেল সেভ হওয়ার আগে। আপনি যদি ডেটা পরিবর্তন করতে চান বা কোনো বৈধতা যাচাই করতে চান, তাহলে এটি ব্যবহার করবেন।

- উদাহরণ:
 - ইমেইল ফর্ম্যাট যাচাই: সেভ করার আগে ইমেইল ফর্ম্যাট চেক করা।

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User

@receiver(pre_save, sender=User)
def validate_email_format(sender, instance, **kwargs):
    if not "@" in instance.email:
        raise ValueError("Invalid email format")
```

```python 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import MyModel

@receiver(pre_save, sender=MyModel)
def modify_data_before_save(sender, instance, **kwargs):
    if instance.some_field:
        instance.some_field = instance.some_field.upper()  # সেভ করার আগে ফিল্ডটি পরিবর্তন
```


## 2. post_save Signal
- Use Case: মডেল সেভ হওয়ার পর কিছু অ্যাকশন ট্রিগার করা।
- এটি খুবই সাধারণ একটি use case। আপনি যখন কোনও মডেল সেভ করবেন, তখন আপনি কিছু অতিরিক্ত কাজ করতে পারেন, যেমন ইমেইল পাঠানো, লগিং করা, বা কোন সম্পর্কিত কাজ সম্পাদন করা।

- উদাহরণ:
 - ইমেইল পাঠানো: নতুন ইউজার সাইন আপ করলে স্বাগতম ইমেইল পাঠানো।
 - লগিং: নতুন অবজেক্ট তৈরি হলে লগিং করা।
   
```python 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # যদি নতুন ইউজার তৈরি হয়
        send_mail(
            'Welcome to Our Platform!',
            'Thank you for signing up.',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
``` 


## 3. pre_delete Signal
- Use Case: এই সিগন্যালটি তখন ট্রিগার হয়, যখন কোন মডেল ডিলিট হওয়ার আগে।
- ব্যবহার: আপনি যদি মডেল ডিলিট হওয়ার আগে কিছু এক্সট্রা কাজ করতে চান, যেমন লগিং বা অন্য কোনো অপারেশন, তাহলে pre_delete ব্যবহার করবেন।


```python 
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import MyModel

@receiver(pre_delete, sender=MyModel)
def log_delete(sender, instance, **kwargs):
    print(f"{instance} will be deleted.")  # ডিলিট হওয়ার আগে লগ
```


    
## 4. post_delete Signal

- Use Case: মডেল ডিলিট হওয়ার পর কিছু অ্যাকশন ট্রিগার করা।
- যখন মডেল অবজেক্ট ডিলিট হয়, আপনি কিছু কাজ করতে পারেন, যেমন ডিলিট হওয়া অবজেক্টের সম্পর্কিত ফাইল বা ডাটা সরিয়ে ফেলা।
- ফাইল ডিলিট: ডিলিট হওয়া অবজেক্টের সাথে সংযুক্ত ফাইল মুছে ফেলা।

```python 
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import MyModel

@receiver(post_delete, sender=MyModel)
def delete_related_files(sender, instance, **kwargs):
    # যদি মডেলটির সঙ্গে কোনও ফাইল যুক্ত থাকে, সেটি ডিলিট করুন
    instance.file.delete()
```
```python
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_delete, sender=UserProfile)
def delete_related_files(sender, instance, **kwargs):
    instance.profile_picture.delete()  # প্রোফাইল ছবি ডিলিট করা হচ্ছে

```

## 5. m2m_changed Signal
- এই সিগন্যালটি তখন ট্রিগার হয়, যখন একটি মডেল এর Many-to-Many (M2M) রিলেশন আপডেট হয়, যেমন একটি ফিল্ডে নতুন আইটেম যোগ করা বা সরানো।
- ব্যবহার: যখন আপনি একটি M2M রিলেশন আপডেট করেন, তখন m2m_changed সিগন্যালটি ব্যবহার করা হয়।
 
```python 
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import MyModel

@receiver(m2m_changed, sender=MyModel.some_many_to_many_field.through)
def log_m2m_change(sender, instance, action, **kwargs):
    print(f"Action: {action} on {instance}")
```

## 6. pre_migrate and post_migrate Signals
এই সিগন্যালগুলো তখন ট্রিগার হয়, যখন Django মাইগ্রেশন চালায়।

ব্যবহার: আপনি যদি মাইগ্রেশন চলার আগে বা পরে কিছু কাজ করতে চান, যেমন ডেটাবেসের কিছু পরিবর্তন, তাহলে pre_migrate বা post_migrate ব্যবহার করা হয়।

```python
from django.db.backends.signals import pre_migrate, post_migrate
from django.dispatch import receiver

@receiver(pre_migrate)
def before_migrate(sender, **kwargs):
    print("Before migration starts.")

@receiver(post_migrate)
def after_migrate(sender, **kwargs):
    print("Migration is completed.")
```


## 7. request_started and request_finished Signals
- Use Case: HTTP রিকোয়েস্ট শুরু এবং শেষ হওয়া ট্র্যাক করা।
- এটি মূলত request এর শুরুর এবং শেষের সময় ট্র্যাক করার জন্য ব্যবহৃত হয়।
- লগিং রিকোয়েস্ট শুরু ও শেষ হওয়া: আপনি যখন রিকোয়েস্ট শুরু বা শেষ হতে দেখবেন, তখন লগিং করতে পারেন।

```python
from django.core.signals import request_started, request_finished
from django.dispatch import receiver

@receiver(request_started)
def log_request_start(sender, **kwargs):
    print("Request started!")

@receiver(request_finished)
def log_request_end(sender, **kwargs):
    print("Request finished!")
```

## 8. database_rollback Signal
- Use Case: ডাটাবেস রোলব্যাক ঘটলে ট্র্যাক করা।
- ****এটি তখন ট্রিগার হয় যখন কোন ট্রানজেকশনের রোলব্যাক করা হয়। যদি ডাটাবেসের কোন অপারেশন ব্যর্থ হয়ে রোলব্যাক হয়, তখন এটি ব্যবহৃত হতে পারে।
- রোলব্যাক ট্র্যাকিং: ডাটাবেস রোলব্যাক হলে কিছু কাজ করা।

```python
from django.db.backends.signals import transaction_rollback
from django.dispatch import receiver

@receiver(transaction_rollback)
def log_rollback(sender, **kwargs):
    print("Transaction was rolled back!")
```

সারাংশ:
- Django সিগন্যাল বিভিন্ন গুরুত্বপূর্ণ কাজ করার জন্য ব্যবহার করা হয়, যেমন:
- ডাটাবেস অপারেশন বা মডেল সেভ/ডিলিট করার পরে কিছু কাজ করা।
- ইমেইল পাঠানো, লগিং, ফাইল ম্যানেজমেন্ট, ও অন্যান্য সার্ভিসের সঙ্গে ইন্টিগ্রেশন।
- সিগন্যাল ব্যবহারের মাধ্যমে আপনার কোডের লজিক ও ইভেন্টগুলো আলাদা রাখা যায়, যেটি অ্যাপ্লিকেশনকে আরও ক্লিন এবং ম্যানটেইনেবল করে তোলে।







# Signal Trigger করার প্রক্রিয়া (Step by Step):
- Signal Definition: প্রথমে Django-তে সিগন্যালটি তৈরি করতে হবে। উদাহরণস্বরূপ, post_save, pre_save, ইত্যাদি।

- Receiver Function: একটি ফাংশন তৈরি করতে হবে যা সিগন্যালটি পাওয়ার পরে কার্যকর হবে। ফাংশনটি signal এবং sender এর সাথে সংযুক্ত হবে।

- Connect Signal to Receiver: সিগন্যালটি একটি receiver ফাংশনের সাথে যুক্ত করতে হবে @receiver ডেকোরেটরের মাধ্যমে। অথবা ম্যানুয়ালি signal.connect() ব্যবহার করা যেতে পারে।

Complete Example:

```python 
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_model_saved(sender, instance, created, **kwargs):
    if created:
        print(f"A new {sender} instance was created: {instance}")
```
##### Signal Register করা:
- Signals ব্যবহারের জন্য, apps.py-এর ready() মেথডে সিগন্যাল ফাইলটি ইমপোর্ট করতে হবে।

```python 
# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # signals.py ফাইলটি ইমপোর্ট করা হচ্ছে
```

## Signal Disconnect:
##### আপনি যখন চাইবেন যে সিগন্যাল আর ট্রিগার না হোক, তখন disconnect() মেথড ব্যবহার করে সিগন্যালটি ডিসকানেক্ট করা যাবে।

```python 
from django.db.models.signals import post_save
from .models import MyModel
post_save.disconnect(my_model_saved, sender=MyModel)
```

## সারাংশ:

<h6> 
    
Django Signals আপনাকে ইভেন্ট ড্রিভেন প্রোগ্রামিংয়ের সুবিধা দেয়। সিগন্যাল দিয়ে আপনি নির্দিষ্ট ঘটনাগুলোর উপর ভিত্তি করে অ্যাকশন নিতে পারেন, যেমন মডেল সেভ, ডিলিট, M2M চেঞ্জ ইত্যাদি। Django Signals ব্যবহারের মাধ্যমে আপনার কোডের মধ্যে ডিকপ্লিং আসে, যা কোডের সচ্ছলতা এবং পুনরায় ব্যবহারযোগ্যতা বাড়ায়।

এটি কোডের মধ্যে আলাদা ফাংশনালিটিকে আলাদা করে দেয়, এবং একে অপরের উপর নির্ভরশীলতা কমায়।

</h6>


















##  Django Signals: সব প্যারামিটার ব্যাখ্যা (বাংলায়)
##### Django Signals হল এক ধরনের Observer Pattern, যা বিভিন্ন মডেল বা ইভেন্টের উপর নির্ভর করে callback function ট্রিগার করার সুবিধা দেয়।

##### Django signals এর প্রধানভাবে ব্যবহৃত কিছু প্যারামিটার (parameters) এবং তাদের ব্যাখ্যা নিচে দেওয়া হলো।

###  1. sender
- ব্যাখ্যা: কোন মডেল বা ক্লাস থেকে signal পাঠানো হচ্ছে তা নির্দেশ করে।
- ব্যবহার: আপনি নির্দিষ্ট মডেল থেকে ট্রিগার করতে sender=MyModel সেট করতে পারেন।
- যদি sender না দেওয়া হয়, তাহলে signal সকল মডেল এর জন্য কাজ করবে।
 
```python 
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Student

@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"New student added: {instance.name}")
```
###### 📌 ব্যাখ্যা: এখানে sender=Student অর্থাৎ শুধুমাত্র Student মডেলে কোন অবজেক্ট create/update হলে signal কাজ করবে।

###  2. instance
- ব্যাখ্যা: যে মডেলের অবজেক্ট তৈরি, আপডেট বা ডিলিট হচ্ছে সেই নির্দিষ্ট অবজেক্ট।
- ব্যবহার: আমরা instance ব্যবহার করে সেই অবজেক্টের ডেটা অ্যাক্সেস করতে পারি।
 
```python 
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"Student Name: {instance.name}, Email: {instance.email}")
```

###### 📌 ব্যাখ্যা: এখানে instance.name এবং instance.email দ্বারা নতুন তৈরি হওয়া অথবা আপডেট হওয়া Student অবজেক্ট এর তথ্য বের করা হয়েছে।

### 3. created
- ব্যাখ্যা: নতুন অবজেক্ট তৈরি হলে True, যদি আপডেট হয় তবে False রিটার্ন করে।
- ব্যবহার: এটি ব্যবহার করে আমরা চেক করতে পারি অবজেক্ট নতুন তৈরি হয়েছে নাকি আপডেট হয়েছে।

```python
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        print("A new student has been registered!")
    else:
        print("Student information updated.")
```

###### 📌 ব্যাখ্যা: যদি নতুন Student অবজেক্ট তৈরি হয়, তাহলে "A new student has been registered!" প্রিন্ট হবে।

###### যদি Student আপডেট হয়, তাহলে "Student information updated." প্রিন্ট হবে।

###  4. raw
- ব্যাখ্যা: যদি ডাটাবেজ bulk_create বা fixture load করা হয়, তবে raw=True হয়।
- ব্যবহার: সাধারণত এটি data migrations অথবা bulk data insertions এর ক্ষেত্রে গুরুত্বপূর্ণ।
 
```python 
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, created, raw, **kwargs):
    if raw:
        print("This data was added via bulk insert.")
```

###### 📌 যদি bulk_create() এর মাধ্যমে ডাটা যোগ করা হয়, তাহলে "This data was added via bulk insert." প্রিন্ট হবে।

###  5. using
- ব্যাখ্যা: কোন ডাটাবেজে এই অপারেশন হয়েছে তা নির্দেশ করে (যদি multiple databases থাকে)।

- ব্যবহার: যদি Django একাধিক ডাটাবেজ ব্যবহার করে, তখন using প্যারামিটার দিয়ে নির্দিষ্ট ডাটাবেজ চেক করা যায়।
 
```python 
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, using, **kwargs):
    print(f"Data saved in database: {using}")
```
###### 📌 যদি using='default', তাহলে ডিফল্ট ডাটাবেজে ডাটা সেভ হয়েছে।

###### যদি অন্য কোনো ডাটাবেজ হয়, তাহলে সেই ডাটাবেজের নাম প্রিন্ট হবে।

###  6. update_fields
- ব্যাখ্যা: কোন কোন ফিল্ড আপডেট হয়েছে তা একটি লিস্ট আকারে দেয়।
- ব্যবহার: স্পেসিফিক ফিল্ড আপডেট হলে চেক করা যায়।
 
```python 
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, update_fields, **kwargs):
    if update_fields:
        print(f"Updated fields: {update_fields}")
```

###### 📌 যদি update_fields=['email'], তাহলে প্রিন্ট হবে "Updated fields: ['email']"।

### 7. kwargs
- ব্যাখ্যা: এটি সবসময় অতিরিক্ত ডাটা ক্যাপচার করতে ব্যবহৃত হয়।
- ব্যবহার: যদি ভবিষ্যতে Django নতুন কোনো প্যারামিটার যোগ করে, তাহলে kwargs ব্যবহার করলে signal ব্রেক হবে না।
 
```python 
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received successfully!")
```

###### 📌 এটি all extra arguments গ্রহণ করবে এবং errors এড়াবে।

## 🎯 Signals Trigger করার ধাপসমূহ
Signal Import করুন:

```python 
from django.db.models.signals import post_save
from django.dispatch import receiver
```

Signal Function তৈরি করুন:

```python 
@receiver(post_save, sender=Student)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        print(f"New Student Created: {instance.name}")
```

Django Apps Config ফাইলে ready() মেথডে Signal Register করুন:

```python 
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Ensure signals are loaded
```

## সব Django Signals এর তালিকা

<h6> 
    
| Signal	| Trigger Time|
|----------|-------------|
| pre_save	| Model সেভ হবার আগে| 
| post_save	| Model সেভ হবার পরে| 
| pre_delete	| Model ডিলিট হবার আগে| 
| post_delete	| Model ডিলিট হবার পরে| 
| m2m_changed| 	ManyToManyField আপডেট হলে| 
| pre_migrate| 	মাইগ্রেশন চালানোর আগে| 
| post_migrate	| মাইগ্রেশন চালানোর পরে| 

</h6>

## ✅ শেষ কথা
Django Signals অনেক শক্তিশালী এবং automated operations পরিচালনার জন্য ব্যবহৃত হয়। আপনি চাইলে post_save, pre_delete ইত্যাদি ব্যবহার করে ডাটাবেজ আপডেট, ইমেইল পাঠানো, লগিং, নোটিফিকেশন পাঠানো ইত্যাদি করতে পারেন।
 