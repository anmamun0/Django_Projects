# Django-REST-Framework TokenAuthentication & JWTAuthentication

#### Content of Table

<h6> 

- [1. DRF এর TokenAuthentication](#1-DRF-এর-TokenAuthentication)
- [2. DRF এর JWTAuthentication](#2-DRF-এর-JWTAuthentication)
- [Setting Setup Different TokenAuthentication  & JWTAuthentication](#Setting-Setup-Different-TokenAuthentication-&-JWTAuthentication)
- [React custom hook - TokenAuth বা JWTAuth ব্যবহার](#React-custom-hook---TokenAuth-বা-JWTAuth-ব্যবহার)

- [TokenAuthentication দিয়ে Login + Logout](#TokenAuthentication-দিয়ে-Login-+-Logout)
- [JWTAuthentication দিয়ে Login + Logout](#JWTAuthenticationদিয়ে-Login-+-Logout)

</h6>

# 1. DRF এর TokenAuthentication
[Home](#-content-of-table)
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
[Home](#-content-of-table)

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
[Home](#-content-of-table)
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
[Home](#-content-of-table)
**TokenAuth:** Header এ পাঠাতে হয় →
- `Authorization`: Token <your_token>

**JWTAuth:** Header এ পাঠাতে হয় →
- `Authorization`: Bearer <access_token>


---

<br>
<br>
<br>
<br>

## React custom hook - TokenAuth বা JWTAuth ব্যবহার
[Home](#-content-of-table)

#### React Custom Hook: useAuth
👉 useAuth.js
```
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
```
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
[Home](#-content-of-table)

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

 Flow Summary
- Login (/login/) → Access + Refresh Token generate
- Use Access Token → Protected API access করতে হবে
- Refresh (/refresh/) → Refresh Token দিয়ে নতুন Access Token পাওয়া যাবে
- Logout (/logout/) → Refresh Token blacklist → আর valid হবে না





--- 
<br>
<br>
<br>
<br>
<br>
<br>
<br>


 
 


 