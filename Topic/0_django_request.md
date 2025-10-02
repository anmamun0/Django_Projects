# Request Object কি?
Django এর প্রতিটা view function এ request object আসে যেটা HttpRequest class এর instance। এতে client এর পাঠানো সব information থাকে।

```py
def my_view(request):
    # এই request object এ সব কিছু আছে
    pass
```

---
<br> 

```py
# HTTP Method
request.method              # 'GET', 'POST', 'PUT', 'DELETE', 'PATCH', etc.

# Data
request.GET                 # Query parameters (QueryDict)
request.POST                # Form data (QueryDict)
request.FILES               # Uploaded files (MultiValueDict)
request.body                # Raw request body (bytes)

# User & Auth
request.user                # User object or AnonymousUser
request.session             # Session data (dict-like)
request.COOKIES             # Cookies (dict)

# URL & Path
request.path                # Current URL path (without domain) | '/products/123/'
request.get_full_path()     # Path + query string | '/products/123/?page=2'
request.build_absolute_uri() # Complete URL with domain |  'https://example.com/products/123/'
request.get_host()          # Domain name | 'example.com'
request.get_port()          # Port number | '80', '443', or '8000'
request.scheme              #  'http' or 'https'
request.is_secure()         # Check if HTTPS | True if HTTPS

# Headers & Meta
request.META                # All headers & server info (dict)
request.content_type        # Request এর content type |'application/json', 'text/html', etc.
request.encoding            # Character encoding | 'utf-8'

# Other
request.resolver_match      # URL resolver match object
request.content_params      # Content type parameters
```

---
<br>
<br>
<br>


# reqest.GET

```py
# URL এর query parameters
# URL: /search/?q=django&page=2

request.GET.get('q')        # 'django'
request.GET.get('page')     # '2'
request.GET.get('name', 'default')  # না থাকলে 'default' return করবে

# সব GET parameters একসাথে
request.GET.dict()  # {'q': 'django', 'page': '2'}

# Multiple values (যদি একই key একাধিকবার থাকে)
# URL: /items/?tag=python&tag=django
request.GET.getlist('tag')  # ['python', 'django']
```

---
<br>
<br>
<br>

# request.POST

```py
# POST request এর data
# Form submit করলে এখানে data আসে

request.POST.get('username')
request.POST.get('email')
request.POST.get('password')

# সব POST data একসাথে
request.POST.dict()  # {'username': 'john', 'email': 'john@example.com'}

# Multiple values
request.POST.getlist('hobbies')  # ['coding', 'reading', 'gaming']

# Check if key exists
'username' in request.POST  # True/False
```

---
<br>
<br>
<br>

# request.FILE

```py
# File upload করলে এখানে files থাকবে

uploaded_file = request.FILES.get('profile_picture')

if uploaded_file:
    print(uploaded_file.name)        # 'photo.jpg'
    print(uploaded_file.size)        # 524288 (bytes)
    print(uploaded_file.content_type) # 'image/jpeg'
    
    # File save করুন
    with open(f'media/{uploaded_file.name}', 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

# Multiple files
files = request.FILES.getlist('images')
for file in files:
    print(file.name)

```
POST request এ file upload করলে (enctype="multipart/form-data")

---
<br>
<br>
<br>

# request.META

```py
# HTTP headers এবং server environment variables

# Common headers
request.META.get('HTTP_USER_AGENT')     # Browser info
request.META.get('HTTP_REFERER')        # Previous page URL
request.META.get('HTTP_ACCEPT_LANGUAGE') # 'en-US,en;q=0.9,bn;q=0.8'
request.META.get('HTTP_HOST')           # 'example.com'
request.META.get('HTTP_ACCEPT')         # 'text/html,application/json'

# Custom headers (যেকোনো custom header HTTP_ দিয়ে শুরু হবে)
request.META.get('HTTP_X_REQUESTED_WITH')  # 'XMLHttpRequest' (AJAX request)
request.META.get('HTTP_AUTHORIZATION')     # 'Bearer token123'

# Server info
request.META.get('REMOTE_ADDR')         # Client IP address '192.168.1.1'
request.META.get('SERVER_NAME')         # 'example.com'
request.META.get('SERVER_PORT')         # '80' or '443'
request.META.get('REQUEST_METHOD')      # 'GET', 'POST' etc
request.META.get('PATH_INFO')           # '/products/123/'
request.META.get('QUERY_STRING')        # 'page=2&sort=name'
request.META.get('CONTENT_TYPE')        # 'application/json'
request.META.get('CONTENT_LENGTH')      # Request body size


# Frontend থেকে পাঠানো custom header
# Frontend: headers: { 'X-Custom-Token': 'abc123' }
token = request.META.get('HTTP_X_CUSTOM_TOKEN')  # 'abc123'

# সব META data দেখুন (debugging এর জন্য)
for key, value in request.META.items():
    print(f"{key}: {value}")
```

---
<br>
<br>
<br>

# request.user

```py
# Currently logged in user

# Check if user is authenticated
if request.user.is_authenticated:
    print(f"User: {request.user.username}") 
else:
    print("Anonymous user")

# User permissions
if request.user.is_superuser:
    # Admin user
    pass

if request.user.is_staff:
    # Staff user (can access admin)
    pass

# Check specific permission
if request.user.has_perm('app.add_product'):
    # User can add products
    pass

# User groups
user_groups = request.user.groups.all()
```


---
<br>
<br>
<br>


# request.session
  
```py
# Session data (server-side storage)

# Set session data
request.session['cart_items'] = [1, 2, 3]
request.session['user_preferences'] = {'theme': 'dark', 'language': 'bn'}

# Get session data
cart = request.session.get('cart_items', [])  # [] হবে default value

# Check if key exists
if 'cart_items' in request.session:
    items = request.session['cart_items']

# Delete session key
del request.session['cart_items']

# Clear all session data
request.session.flush()

# Session key (unique identifier)
session_key = request.session.session_key

# Session expiry
request.session.set_expiry(300)  # 5 minutes এ expire হবে
request.session.set_expiry(0)    # Browser close করলে expire হবে
```

---
<br>
<br>
<br>

# request.COOKIES
```py
# Client-side cookies

# Get cookie
user_lang = request.COOKIES.get('language', 'en')
theme = request.COOKIES.get('theme')

# Check if cookie exists
if 'user_id' in request.COOKIES:
    user_id = request.COOKIES['user_id']

# সব cookies দেখুন
for key, value in request.COOKIES.items():
    print(f"{key}: {value}")


Response এ cookie set করতে:
response.set_cookie('theme', 'dark', max_age=3600)  # 1 hour
```