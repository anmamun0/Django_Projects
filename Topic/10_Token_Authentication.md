# Django-REST-Framework TokenAuthentication & JWTAuthentication

#### Content of Table

<h6> 

- [1. DRF এর TokenAuthentication](#1-DRF-এর-TokenAuthentication)
- [2. DRF এর JWTAuthentication](#2-drf-এর-jwtauthentication)
- [Setting Setup Different TokenAuthentication  & JWTAuthentication](#Setting-Setup-Different-TokenAuthentication-&-JWTAuthentication)
- [React.js custom hook - TokenAuth বা JWTAuth ব্যবহার](#reactjs-custom-hook---tokenauth-বা-jwtauth-ব্যবহার)
>
- [TokenAuthentication দিয়ে Login + Logout](#tokenauthentication-দিয়ে-login--logout)
- [JWTAuthentication দিয়ে Login + Logout](#jwtauthentication-দিয়ে-login--logout)
  
</h6>

# 1. DRF এর TokenAuthentication
[Home](#content-of-table)
```
pip install djangorestframework
pip install djangorestframework-authtoken # TokenAuth Installation Command 
rest_framework.authentication.TokenAuthentication # TokenAuth Class
```

কাজের ধরণ:
- একবার ইউজার লগইন করলে Server থেকে একটা Static Token তৈরি হয় (যেমন: "123abcxyz...")।
- সেই TokenDB তে authtoken_token টেবিলে স্টোর থাকে।
- প্রত্যেক রিকোয়েস্টে সেই Token পাঠাতে হয়।

সুবিধা: Easy Setup (built-in আসে DRF এ)। ছোট প্রোজেক্টের জন্য ঠিক আছে।

অসুবিধা:
- Token কখনও এক্সপায়ার হয় না (ম্যানুয়ালি রিভোক করতে হয়)।
- যদি Token লিক হয়ে যায় → পুরো একাউন্ট কমপ্রোমাইজড।
- বড় স্কেল প্রোজেক্টে Security সমস্যা।

Add Apps in   *setting.py*
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```
`python manage.py migrate` //এতে করে authtoken_token নামে টেবিল তৈরি হবে যেখানে টোকেন স্টোর হবে।

Add Authentication Class in *setting.py*
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```
**Response: api call **
```json
{
  "token": "94f5374bcf..."
}
```

**Access API with  Token**
```json
GET /profile/
Authorization: Token 94f5374bcf...
```

Example (JavaScript fetch)
```js
// Token Auth Login
fetch("http://127.0.0.1:8000/login/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username: "mamun",
    password: "1234"
  })
})
.then(res => res.json())
.then(data => {
  console.log("Token:", data.token);
  // Save token to localStorage
  localStorage.setItem("authToken", data.token);
});
```
তারপর Protected API কল করার সময়:
```js
const token = localStorage.getItem("authToken");

fetch("http://127.0.0.1:8000/profile/", {
  method: "GET",
  headers: {
    "Authorization": `Token ${token}`
  }
})
.then(res => res.json())
.then(data => console.log(data));

```



---
<br>
<br>
<br>
<br>

# 2. DRF এর JWTAuthentication
[Home](#content-of-table)

```sh
pip install djangorestframework-simplejwt # Installation command
rest_framework_simplejwt.authentication.JWTAuthentication # JWTAuth Class
```

কাজের ধরণ:
User Login করলে সার্ভার JWT টোকেন তৈরি করে → ২টা অংশে:
- Access Token (স্বল্প সময়ের জন্য, যেমন 5 মিনিট / 1 ঘণ্টা)
- Refresh Token (লম্বা সময়ের জন্য, যেমন 1 সপ্তাহ / 1 মাস)
- Access টোকেন এক্সপায়ার হয়ে গেলে Refresh টোকেন দিয়ে নতুন Access টোকেন নেওয়া যায়।

সুবিধা:
- টোকেন DB তে স্টোর করতে হয় না (stateless → scalable)।
- এক্সপায়ার টাইম সেট করা যায় → সিকিউরিটি বাড়ে।
- Refresh টোকেন দিয়ে সহজে Access টোকেন রিনিউ করা যায়।
- আধুনিক স্ট্যান্ডার্ড → মোবাইল অ্যাপ, SPA (React, Vue, Angular) এর জন্য পারফেক্ট।

অসুবিধা:
- Setup এ একটু বেশি কাজ লাগে।
- Access Token লিক হয়ে গেলে যতক্ষণ না expire হয় ততক্ষণ ব্যবহার করা যাবে।

So Which is best?
- ছোট / প্র্যাকটিস প্রোজেক্ট → TokenAuthentication চলবে।
- প্রফেশনাল / বড় স্কেল প্রোজেক্ট → JWTAuthentication বেস্ট ✅
- (কারণ এটা stateless, scalable, secure এবং আধুনিক ওয়েব/মোবাইল অ্যাপের সাথে compatible)।

Add Authentication Class in *setting.py*
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [ 
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
}
```
**Response: api call**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
  "access": "eyJ0eXAiOiJKV1QiLCJhb..."
}

```

Step 7: Refresh Expired Access Token

```json
POST /token/refresh/
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
}

// Response:

{
  "access": "new_access_token..."
}
```
 
 
Login API (SimpleJWT) 
```js
// JWT Login
fetch("http://127.0.0.1:8000/token/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    username: "mamun",
    password: "1234"
  })
})
.then(res => res.json())
.then(data => {
  console.log("Access:", data.access);
  console.log("Refresh:", data.refresh);

  // Save tokens
  localStorage.setItem("accessToken", data.access);
  localStorage.setItem("refreshToken", data.refresh);
});
```
তারপর Protected API কল করার সময়:
```js
const access = localStorage.getItem("accessToken");

fetch("http://127.0.0.1:8000/dashboard/", {
  method: "GET",
  headers: {
    "Authorization": `Bearer ${access}`
  }
})
.then(res => res.json())
.then(data => console.log(data));
```


---
<br>
<br>
<br>
<br>

### Setting Setup Different TokenAuthentication  & JWTAuthentication
[Home](#content-of-table)
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', # that use for TokenAuth
        'rest_framework_simplejwt.authentication.JWTAuthentication' # That use for JWTAuth
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```
### Key Difference
[Home](#content-of-table)
**TokenAuth:** Header এ পাঠাতে হয় →
- `Authorization`: Token <your_token>

**JWTAuth:** Header এ পাঠাতে হয় →
- `Authorization`: Bearer <access_token>


---

<br>
<br>
<br>
<br>

## React.js custom hook - TokenAuth বা JWTAuth ব্যবহার
[Home](#content-of-table)

#### React Custom Hook: useAuth
👉 useAuth.js
```jsx
import { useState } from "react";

export function useAuth(authType = "jwt") {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("authToken") || null);

  // Login function
  const login = async (username, password) => {
    const url = authType === "jwt"
      ? "http://127.0.0.1:8000/token/"
      : "http://127.0.0.1:8000/login/";

    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (authType === "jwt" && data.access) {
      localStorage.setItem("accessToken", data.access);
      localStorage.setItem("refreshToken", data.refresh);
      setToken(data.access);
    } else if (authType === "token" && data.token) {
      localStorage.setItem("authToken", data.token);
      setToken(data.token);
    }

    setUser(username);
    return data;
  };

  // Logout function
  const logout = () => {
    localStorage.clear();
    setUser(null);
    setToken(null);
  };

  // Fetch with auth header
  const authFetch = async (url, options = {}) => {
    const headers = options.headers || {};
    if (token) {
      headers["Authorization"] =
        authType === "jwt" ? `Bearer ${token}` : `Token ${token}`;
    }

    return fetch(url, { ...options, headers });
  };

  return { user, token, login, logout, authFetch };
}
```
#### ব্যবহার করার নিয়ম

App.js
```jsx
import React, { useState } from "react";
import { useAuth } from "./useAuth";

function App() {
  const { login, logout, authFetch, user, token } = useAuth("jwt"); // অথবা "token"
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const res = await login(username, password);
    console.log("Login Response:", res);
  };

  const handleProfile = async () => {
    const res = await authFetch("http://127.0.0.1:8000/profile/");
    const data = await res.json();
    console.log("Profile:", data);
  };

  return (
    <div className="p-5">
      <h2>Auth Demo</h2>
      {user ? (
        <>
          <p>Welcome {user}</p>
          <button onClick={handleProfile}>Get Profile</button>
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <>
          <input
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleLogin}>Login</button>
        </>
      )}
    </div>
  );
}

export default App;
```

Usefull
- চাইলে "jwt" বা "token" সিলেক্ট করে দুই সিস্টেমেই ইউজ করতে পারবে।
- login() করলে টোকেন localStorage এ সেভ হবে।
- authFetch() দিয়ে API কল করলে অটো হেডার সেট হবে।
- logout() করলে লোকালস্টোরেজ ক্লিয়ার হবে।

---

<br>
<br>
<br>
<br>


# TokenAuthentication দিয়ে Login + Logout
[Home](#content-of-table)

> Step 2: Django REST Framework এ ready-made login API আছে।
👉 urls.py
```py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutView, ProfileView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),  # login (generate token)
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
```

> Step 3: Logout API (Token Delete)
👉 views.py
```py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # ইউজারের টোকেন ডিলিট করা হবে
        request.user.auth_token.delete()
        return Response({"message": "Logout successful, token deleted"})
```

> Step 4: Protected API Example
👉 views.py
```py
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
        })
```

> Step 5: Test the Flow
(1) Login Request

```
POST /login/
Content-Type: application/json

// Body
{
  "username": "mamun",
  "password": "1234"
}
```

Response:
```
{
  "token": "94f5374bcf1a..."
}
```

> (2) Access Protected API

```json
GET /profile/
Authorization: Token 94f5374bcf1a...
```


> (3) Logout Request
```json
POST /logout/
Authorization: Token 94f5374bcf1a...
```

Response
```json
{
  "message": "Logout successful, token deleted"
}
```
👉 এখন সেই টোকেন আর কাজ করবে না।
<br>

### Token attributes/methods

`rest_framework.authtoken.models.Token` এর সব attributes/methods:

<h6>
  
| Attribute / Method                       | বর্ণনা (Usecase)                                     | উদাহরণ                                                    |
| ---------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------- |
| `Token.objects.create(user=user)`        | নতুন টোকেন তৈরি করে User এর সাথে bind করবে           | `token = Token.objects.create(user=user)`                 |
| `Token.objects.get(user=user)`           | নির্দিষ্ট User এর existing টোকেন return করবে         | `token = Token.objects.get(user=user)`                    |
| `Token.objects.get_or_create(user=user)` | আগে টোকেন থাকলে return করবে, না থাকলে নতুন তৈরি করবে | `token, created = Token.objects.get_or_create(user=user)` |
| `Token.key`                              | আসল টোকেন string (client কে পাঠানো হয়)               | `print(token.key)`                                        |
| `Token.user`                             | টোকেন কোন User এর সাথে যুক্ত সেটা return করবে        | `print(token.user.username)`                              |
| `Token.created`                          | টোকেন কবে তৈরি হয়েছে সেটা জানাবে                     | `print(token.created)`                                    |
| `Token.delete()`                         | টোকেন মুছে ফেলবে (logout এর সময় কাজে লাগে)           | `token.delete()`                                          |

</h6>
- .get() এ তুমি model এর যেকোনো ফিল্ড দিয়ে query করতে পারো।
- একাধিক parameter দিলে AND condition হবে।

  
- 1. user দিয়ে get   →  `token = Token.objects.get(user=user)`
- 2. key দিয়ে get   →    `token = Token.objects.get(key="abcd1234...")`
- 3. multiple condition   →   `token = Token.objects.get(user=user, key="abcd1234...")`
- 4. Case-insensitive match `(__iexact)`   →   `token = Token.objects.get(user__username__iexact="mamun")`
- 5. Contains `(__icontains)`    →   `token = Token.objects.get(user__email__icontains="@gmail.com")`
- 6. In list `(__in)`   →   `token = Token.objects.get(user__id__in=[1, 2, 3])`
- 7. Greater than / Less than `(__gt, __lt)`   →   `token = Token.objects.get(created__gt="2025-01-01")`


#### Custom Auth Token View 
```py
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class EmailAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=400)

        user = authenticate(username=user_obj.username, password=password)
        if not user:
            return Response({"error": "Invalid email or password"}, status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "email": user.email
        })
```

#### Practical usecase: in my project

```py
# permissions.py

from rest_framework.authtoken.models import Token
from accounts.models import Profile

class CustomAdminTokenCheckMixin:
    def is_admin(self, request):

        # its best for safe security
        # it will check , Header section has any "Authorization" variable ?
        auth_header = request.headers.get('Authorization')

        # it will check , Body section has any "token_id" variable ?
        token_id = (
            request.data.get('token_id') or
            request.query_params.get('token_id') or
            request.headers.get('token_id')
        )
        if auth_header and auth_header.startswith('Token '):
            token_id = auth_header.split(' ')[1]
  
        if not token_id:
            return False
        try:
            token = Token.objects.get(key=token_id)
            user = token.user
            profile = Profile.objects.get(user=user)
            return profile.role == 'admin'
        except (Token.DoesNotExist, Profile.DoesNotExist):
            return False
```

--- 
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# JWTAuthentication দিয়ে Login + Logout
[Home](#-content-of-table)

> Step 2: Add JWT URLs
👉 urls.py
```py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import LogoutView, ProfileView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # refresh token
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),         # verify token
    path('logout/', LogoutView.as_view(), name='logout'),                    # logout
    path('profile/', ProfileView.as_view(), name='profile'),                 # protected
]
```

> Step 3: JWT Login & Refresh

- Login API (/login/)
 - ইউজারনেম + পাসওয়ার্ড দিলে Access Token + Refresh Token দেবে।

- Refresh API (/refresh/)
 - Refresh Token দিয়ে নতুন Access Token তৈরি করা যাবে।

> Step 4: Logout (Blacklist Token)

- SimpleJWT-তে Logout করার মানে হচ্ছে → Refresh Token কে blacklist করা
- (কারণ JWT stateless, সার্ভারে কিছু store হয় না)।

### 👉 প্রথমে settings.py এ blacklist অ্যাপ যোগ করতে হবে
```py
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt.token_blacklist',
]
```

### 👉 migrate চালাও
```sh
python manage.py migrate
```

👉 views.py
```py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful, token blacklisted"})
        except Exception as e:
            return Response({"error": "Invalid token"}, status=400)
```

> Step 5: Protected API Example
👉 views.py
```py
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
        })
```

> Step 6: Test the Flow

(1) Login Request
```
POST /login/
Content-Type: application/json

Body
{
  "username": "mamun",
  "password": "1234"
}
```

Response
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh...",
  "access": "eyJ0eXAiOiJKV1QiLCJhb..."
}
```

### (2) Access Protected API
```json
GET /profile/
Authorization: Bearer <access_token>
```

Response
```json
{
  "username": "mamun",
  "email": "mamun@gmail.com"
}
```

### (3) Refresh Token
```json
POST /refresh/
Content-Type: application/json

// Body
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

Response
```json
{
  "access": "new_access_token_here"
}
```

### (4) Logout Request
```json
POST /logout/
Content-Type: application/json
Authorization: Bearer <access_token>

// Body
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
}
```


Response
```json
{
  "message": "Logout successful, token blacklisted"
}
```


### Custom Login make : its not good usecase

```py
# serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password.")

        # generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "email": user.email,
            "id": user.id,
        }

```

 Flow Summary
- Login (/login/) → Access + Refresh Token generate
- Use Access Token → Protected API access করতে হবে
- Refresh (/refresh/) → Refresh Token দিয়ে নতুন Access Token পাওয়া যাবে
- Logout (/logout/) → Refresh Token blacklist → আর valid হবে না

<br>
<br>

### JWT Life Cycle
`login → get JWT → use JWT → refresh → logout example`

<br>
<br>

### rest_framework_simplejwt.tokens Methods & Attributes

`rest_framework_simplejwt.tokens import RefreshToken, AccessToken , SlidingToken`

#### Methods & Attributes
1. RefreshToken
- Long-lived token
- এর মাধ্যমে নতুন access token generate করা যায়।
- DB তে save হয় না (JWT stateless)।

2. AccessToken
- Short-lived token (যেটা API call করার সময় client পাঠায়)।
- সাধারণত ৫ মিনিট থেকে ১ ঘণ্টা পর্যন্ত valid থাকে।
  
3. SlidingToken
- Access + Refresh দুইটার mix alternative
- একটাই টোকেন ইউজ হয়, কিন্তু auto refresh হয় expiration এর আগে

<h6> 
  
| Method / Attribute            | কাজ                                                     |
| ----------------------------- | ------------------------------------------------------- |
| `RefreshToken.for_user(user)` | নির্দিষ্ট user এর জন্য নতুন refresh token তৈরি করবে     |
| `.access_token`               | refresh token থেকে নতুন access token তৈরি করবে          |
| `.get('exp')`                 | expiry time বের করবে                                    |
| `.get('jti')`                 | unique token id (UUID) বের করবে                         |
| `.blacklist()`                | blacklist করলে token invalid হয়ে যাবে (logout এ useful) |

</h6>

```py
refresh = RefreshToken.for_user(user)
print(str(refresh))              # refresh token string
print(str(refresh.access_token)) # access token string
 
print(refresh['exp'])   # expiry timestamp
print(refresh['user_id'])  # কোন user এর জন্য তৈরি হয়েছে

```
```py
access_token = AccessToken.for_user(user)
print(str(access_token))  # access token string

print("Before setting exp:", access_token.payload['exp'])  # default expiration | Token এর expiration time দেখতে পারি।

# Change expiration time (e.g., 1 hour from now)
access_token.set_exp(lifetime=timedelta(hours=1))

```
--- 
<br>
<br>
<br>
<br>
<br>
<br>
<br>


 
 


 