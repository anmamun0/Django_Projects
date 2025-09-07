# Django REST Framework Token Authentication (SimpleJWT ছাড়া pure Token)



### 🔹 Step 1: Django REST Framework ইনস্টল
```shell
pip install djangorestframework
pip install djangorestframework-simplejwt   # যদি JWT ব্যবহার করতে চাও
```


কিন্তু এখন আমরা TokenAuthentication দিয়ে শিখব, তাই extra কিছু লাগবে না।

### 🔹 Step 2: settings.py এ সেটআপ
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # Token system enable
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```
### 🔹 Step 3: migrate রান করো
```shell
python manage.py migrate
```

👉 এটা Token টেবিল তৈরি করবে (প্রতিটি ইউজারের জন্য আলাদা token)।

### 🔹 Step 4: urls.py এ যোগ করো
```py
# project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', views.obtain_auth_token),  # Token login endpoint
    path('api/', include('accounts.urls')),           # তোমার app এর API
]
```

### 🔹 Step 5: ইউজার Token তৈরি (automatic or manual)
Option 1: Login করে Token পাওয়া

/api/token-auth/ এ POST request পাঠালে ইউজারের username/password দিলে token return করবে।

Example (cURL / JS fetch):
```js
fetch("http://127.0.0.1:8000/api/token-auth/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        "username": "mamun",
        "password": "12345mamun"
    }),
})
.then(res => res.json())
.then(data => console.log("Your Token:", data.token));
```

Response হবে:
```js
{
  "token": "a8f6f9d0b1a2c3..."
}
```
### 🔹 Step 6: Authenticated API ব্যবহার

এখন যেকোনো API request এ header এ token পাঠাতে হবে:
```js
fetch("http://127.0.0.1:8000/api/products/", {
    method: "GET",
    headers: {
        "Authorization": "Token a8f6f9d0b1a2c3..."   // এখানে তোমার token
    }
})
.then(res => res.json())
.then(data => console.log(data));
```

### 🔹 Step 7: Views Example
```py
# accounts/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # শুধু login ইউজারই access করতে পারবে

🔹 Step 8: Logout (Token delete করে)
# accounts/views.py
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logout successful"})
```



```py
# Token created ---
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username="mamun")
token, created = Token.objects.get_or_create(user=user)
print(token.key)   # এই key টা client-এ ব্যবহার করবে

# Token delete ----
user = User.objects.get(username="mamun")
Token.objects.filter(user=user).delete()
```


```

✅ Flow Recap:

- User login → /api/token-auth/ → Token পাবে
- Client (React / Vite) → API call → Header এ "Authorization": "Token <token>" পাঠাবে
- DRF check করবে token valid কিনা → valid হলে request.user set হবে
- Logout চাইলে token delete করবে