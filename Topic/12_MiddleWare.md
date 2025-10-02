

## Middleware কীভাবে কাজ করে
Middleware একটি Python class যা __init__ ও __call__ method ব্যবহার করে।
Request → Middleware → View → Response → Middleware (reverse)

*Read This Blogs*
[docs.djangoproject.com](https://docs.djangoproject.com/en/5.2/topics/http/middleware/)
[geeksforgeeks.org](https://www.geeksforgeeks.org/python/middleware-in-django-image-video-error/)


---
 <br>
 <br>
 <br>

## Middleware file structure
```sh
demo/
    __init__.py
    settings.py
    urls.py
    wsgi.py
    middleware/
        __init__.py
        custom_middleware.py
```
---
 <br>
 <br>
 <br>


**Code**
```py
# demo/middleware/custom_middleware.py
class SimpleMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Started Custom MiddleWare")
    
    def __call__(self, request , *args, **kwds):
         # Request Phase (view এর আগে)
        print(f"Incoming request path: {request.path}")

        response = self.get_response(request)  # View call

        # Response Phase (view এর পরে)
        print(f"Outgoing response status: {response.status_code}")

        return response
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == "dashboard" :
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("🚫 Only staff can access admin panel")
        return None  # None হলে normal view continue
```

---
 <br>
 <br>
 <br>



## setting.py path setup
```py
MIDDLEWARE = [
    # Django default middleware ...
    'django.middleware.security.SecurityMiddleware',       # Security headers
    'django.contrib.sessions.middleware.SessionMiddleware', # Sessions
    'django.middleware.common.CommonMiddleware',           # Handles URL rewriting, etc
    'django.middleware.csrf.CsrfViewMiddleware',           # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Auth system
    'django.contrib.messages.middleware.MessageMiddleware', # Messages framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking protection

    #  custom middleware
    "demo.middleware.custom_middleware.SimpleMiddleware",
]
```


**SecurityMiddleware**
- extra security headers যোগ করে।
- Cross-Site Scripting (XSS) থেকে সুরক্ষা দেয়।


**SessionMiddleware**
- Session ID cookie management

**CommonMiddleware**
- URL এ / অ্যাড বা রিমুভ করে যদি APPEND_SLASH=True হয়।
- নির্দিষ্ট user-agent ব্লক করতে পারে।
- Response এ Content-Length অটো সেট করে।

**AuthenticationMiddleware**
- request.user.is_authenticated → ইউজার লগইন করা আছে কিনা জানায়।
- এটা ছাড়া request.user কাজ করবে না, লগইন সিস্টেম ভেঙে যাবে।

**MessageMiddleware**
- Django এর message framework কাজ করায়।
- টেম্পোরারি ম্যাসেজ দেখাতে ব্যবহার হয় (success, error, warning, info)।

**XFrameOptionsMiddleware**
- Clickjacking attack থেকে রক্ষা করে।
- তোমার সাইট অন্য কোনো <iframe> এর মধ্যে লোড হতে পারবে না। এর ফলে হ্যাকাররা লুকানো ফ্রেম দিয়ে ইউজারকে ভুল বোতাম ক্লিক করাতে পারবে না।


---
 <br>
 <br>
 <br>

## Middleware Cycle:

**🟢 Django Template Flow**
`Request → Middleware → URL Resolver → View → Template Engine → HTML Response → Middleware → Client (Browser)`

**🔵 DRF Flow**
`Request → Middleware → URL Resolver → APIView/ViewSet → Serializer → JSON Response → Middleware → Client (API/Frontend)`

---
 <br>
 <br>
 <br>

## Custom Middleware Methods:

**1. Required / Core Methods**

1. __init__(self, get_response)
- Server start হলে একবার run হয়।
- get_response দিয়ে next middleware বা view call করা হয়।


2. __call__(self, request)
- প্রতিটি request এ run হয়।
- Request → View → Response chain handle করে।



**2. Optional Hooks / Methods**

3. process_view(self, request, view_func, view_args, view_kwargs)
- View call হওয়ার আগে run হয়।
- Inspect/modify request or redirect before view।


4. process_exception(self, request, exception)
- View execution এ exception হলে run হয়।
- Custom response return করতে পারে।

5. process_template_response(self, request, response)
- View থেকে TemplateResponse আসলে run হয়।
- Template render হওয়ার আগে modify করতে পারে।

<br>

`Request → __call__ → process_view → View → process_exception (if error) → process_template_response → __call__ (response phase)`


---
 <br>
 <br>
 <br>


## Commonly Used Objects/Methods Inside Middleware
 
**From request (HttpRequest object):**
`request.path` → full URL path
`request.method` → HTTP method (GET, POST...)
`request.user` → current logged-in user (if AuthenticationMiddleware enabled)
`request.session` → session data
`request.GET` / `request.POST` → query params / form data
`request.headers` → request headers

**From view_func:**
`view_func.__name__` → view function name
`view_func.__module__` → কোন module এ আছে
`view_args` / `view_kwargs` → URL parameters

**From response:**
`response.status_code` → status (200, 403, 500 …)
`response.content` → response body
`response.headers` → response headers

**From exception:**
`exception.__class__.__name__` → error class name
`str(exception) → error message`



---
 <br>
 <br>
 <br>



