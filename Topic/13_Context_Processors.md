##  Context Processors

**Context Processor কী?**

*Django Template-এ আমরা সাধারণত views.py থেকে context পাঠাই। কিন্তু যদি কিছু data (যেমন: request.user, site_name, settings data) সব template-এ automatically available রাখতে চাই, তখন আমরা context processor ব্যবহার করি।*


### Context Processor কিভাবে কাজ করে?
- এগুলো হলো Python functions, যেগুলো একটি dictionary return করে।
- Django Template render করার সময় এগুলো context-এ inject করে।
- তাই প্রতিটি template-এ সেই values auto available হয়।


### Django ডিফল্ট ভাবে অনেকগুলো context processor দেয়, যেমনঃ

- `django.template.context_processors.debug` → debug info
- `django.template.context_processors.request` → request object template এ available
- `django.contrib.auth.context_processors.auth` → user, perms template এ available
- `django.contrib.messages.context_processors.messages` → Django messages



---
<br>
<br>
<br>


Project Structure

```sh
project/
   core/
      context_processors.py

```

**context_processors.py*
```py
def site_info(request):
    return {
        "site_title": "My Awesome Django Site",
        "author": "AN Mamun"
    }
```


*setting.py*
```py
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Custom
                "core.context_processors.site_info",
            ],
        },
    },
]

```


*template.html*
```html
<h1>{{ site_title }}</h1>
<p>Author: {{ author }}</p>
```


---
<br>
<br>
<br>
