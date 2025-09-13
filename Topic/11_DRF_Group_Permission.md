# DRF_Group_Permission 


> **Summary Details**
<h6>

- [Global Permission](#global-permission)
- [View বা ViewSet অনুযায়ী আলাদা Permission সেট করা](#view-বা-viewset-অনুযায়ী-আলাদা-permission-সেট-করা)
- [Multiple Permissions (Optional)](1-#multiple-permissions-optional)
- [Django Group Model Permission](#django-group-model-permission)
</h6>


**Group কী?**
- Django তে Group হলো user এর একটি collection, যাদের একই permission দেওয়া হয়। যেমন: Manager, Editor, Viewer।
- Manager → সব কিছু করতে পারবে।
- Editor → কেবল update/edit এবং view করতে পারবে।
- Viewer → কেবল দেখার permission থাকবে।

**DRF এর সাথে ব্যবহার:**
- Django REST Framework এ আমরা permission_classes ব্যবহার করি view বা viewset এ। আমরা চাইলে এই permissions group এর উপর ভিত্তি করে দিতে পারি।

`DRF` + `Group Permission` = `API access` কে user এর group অনুযায়ী control করা।

# Global Permission 

settings.py এ যেমন আছে:

```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Default
    ]
}
```


### 1️⃣ DEFAULT_AUTHENTICATION_CLASSES কি?

এটা বলে Django REST Framework (DRF) কোন authentication method ব্যবহার করবে।
```py
'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
],
```

**TokenAuthentication**
- User login করলে একটি unique token generate হয়।
- পরবর্তী API call এ user সেই token পাঠাবে।
- Mobile apps বা external clients এর জন্য খুব useful।

**SessionAuthentication**
- Django এর default session system ব্যবহার করে।
- সাধারণত web browser থেকে API access করলে session cookie এর মাধ্যমে validate করে।
- 💡 অর্থাৎ তুমি দুই ধরনের authentication একসাথে ব্যবহার করতে পারো।


### 2️⃣ DEFAULT_PERMISSION_CLASSES কি?

DRF এর permission system নির্ধারণ করে কোন user কোন API access করতে পারবে।
```py
'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissions',
]
```

**DjangoModelPermissions**
- DRF automatically Django এর model permission ব্যবহার করে।
- Permission অনুযায়ী API access control করবে।
 
অর্থাৎ সব view/endpoint by default IsAuthenticated হবে। 
<h6>

| Permission Class                       | Bangla Explanation                                                                 |
| -------------------------------------- | ---------------------------------------------------------------------------------- |
| `AllowAny`                             | সব user API access করতে পারবে, login লাগবে না।                                     |
| `IsAuthenticated`                      | শুধু logged-in user access করতে পারবে।                                             |
| `IsAdminUser`                          | শুধু `is_staff=True` user access করতে পারবে।                                       |
| `IsAuthenticatedOrReadOnly`            | Logged-in user সব করতে পারবে, non-logged-in user শুধু GET করতে পারবে।              |
| `DjangoModelPermissions`               | Django model permissions অনুযায়ী API access control।                              |
| `DjangoModelPermissionsOrAnonReadOnly` | Logged-in user permission অনুযায়ী API control, non-logged-in user শুধু read-only। |

</h6>
 

DRF automatically map করে HTTP methods → **`DjangoModelPermissions`**:

<h6>
    
| HTTP Method | Required Permission |
| ----------- | ------------------- |
| GET         | `view_<model>`      |
| POST        | `add_<model>`       |
| PUT/PATCH   | `change_<model>`    |
| DELETE      | `delete_<model>`    |

</h6>

উদাহরণ: 

- `Viewer group` → শুধু `view_product` আছে →  GET request  করতে পারবে,  POST/PUT/DELETE  করতে পারবে না।
- `Editor group` → `view_product`, `change_product` আছে → GET  এবং  PUT/PATCH  করতে পারবে,  POST/DELETE করতে পারবে না।
- `Manager group` → সব permission আছে → সব করতে পারবে।



---

<br>
<br>
<br>
<br>

# View বা ViewSet অনুযায়ী আলাদা Permission সেট করা
[Home](#DRF-Group-Permission)

```py
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import Product, Blog
from .serializers import ProductSerializer, BlogSerializer


# Example 1: Product → Only authenticated users
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # শুধু logged-in user access করতে পারবে
 

# Example 2: Blog → Anyone can access
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]  # কোনো login লাগবে না
```

✅ এখানে permission_classes attribute দিয়ে প্রতিটি view বা viewset আলাদা permission enforce করা হয়।

### 1️⃣ Multiple Permissions (Optional)

- একাধিক permission class একসাথে দিতে পারো।
- DRF সব permission চেক করে, এবং সব permission satisfy করতে হবে।

```py
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
```

এখানে user login করতে হবে এবং model permission থাকতে হবে।

Summary Bangla
- Global permission → settings.py এ, সব view এ default হবে।
- View-specific permission → permission_classes = [...] দিয়ে override করা যাবে।
- AllowAny → সবাই access করতে পারবে।
- IsAuthenticated → শুধু logged-in user access করতে পারবে।
- Multiple permissions → সব permission satisfy করতে হবে।




--- 


<br>
<br>
<br>
<br>
<br>
<br>


# Use a Custom permission.py Class
```
from rest_framework.permissions import BasePermission

class CustomIsAuthenticated(BasePermission):
    message = "Please log in first to access this endpoint."

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
```
Then in your view:

```python 
class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Register
    permission_classes = [CustomIsAuthenticated]
```


<br>
<br>
<br>
<br>

# Own Object Access Permission
permission.py
```py
from rest_framework.permissions import BasePermission

class IsOwnerPermission(BasePermission):
    message = "You can only access your own profile."

    # General view-level permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # Object-level permission
    def has_object_permission(self, request, view, obj):
        # obj is a User instance
        return obj == request.user

```
views.py
```py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .permissions import IsOwnerPermission

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    # Override get_object to make sure object-level permission works
    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
```




# Django Group Model Permission 
[Home](#DRF-Group-Permission)

setting.py
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ]
}

```
  
signals.py
```py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.apps import apps

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name != "accounts":  # শুধু accounts migrate হলে চালু হবে
        return
    
       # products app-এ Product Model
    Product = apps.get_model("people", "Product")

    # Groups create
    manager_group, _ = Group.objects.get_or_create(name="Manager")
    editor_group, _ = Group.objects.get_or_create(name="Editor")
    viewer_group, _ = Group.objects.get_or_create(name="Viewer")

    # যেসব model এর permission দিতে চান
    target_models = ["product", "category", "cart", "cartitem", "order"]
 
    # Manager → সব পারমিশন
    manager_perms = Permission.objects.filter(content_type__model__in=target_models)
    manager_group.permissions.set(manager_perms)

    # Editor → শুধু change এবং view পারমিশন
    editor_permission = [ "change_product", "view_product",  "change_category", "view_category","change_cart", "view_cart", "change_cartitem", "view_cartitem", "change_order", "view_order",]
    editor_perms = Permission.objects.filter( content_type__model__in=target_models, codename__in=editor_permission,)
    editor_group.permissions.set(editor_perms)

    # Viewer → শুধু view পারমিশন
    viewer_permission = [  "view_product", "view_category", "view_cart", "view_cartitem", "view_order",]
    viewer_perms = Permission.objects.filter( content_type__model__in=target_models, codename__in=viewer_permission,)
    viewer_group.permissions.set(viewer_perms) 
```




explanation:
 
###  1️⃣ Signal & Receiver
- `post_migrate`→ মাইগ্রেশন শেষ হলে trigger হবে।
- `@receiver(post_migrate)` → এই ফাংশন run হবে মাইগ্রেশন শেষে।

###  2️⃣ Sender check

```py
if sender.name != "people":
    return
```

শুধু "people" অ্যাপের জন্য এই কোড রান হবে।

### 3️⃣ Model Dynamic Import

```py
Product = apps.get_model("people", "Product")
```

মডেল dynamic ভাবে নেয়া হয়েছে, direct import না করে।

### 4️⃣ Group তৈরি
get_or_create() → যদি group না থাকে create করবে, না হলে fetch করবে।

###  5️⃣ Permission filter
- Django প্রতিটি মডেলের জন্য create করে: `add_model`, `change_model`, `delete_model`, `view_model`
- আমরা শুধু Product মডেলের permission filter করেছি।

### 6️⃣ Manager permission

সব permission assign করা হয়েছে।

### 7️⃣ Editor permission
```py
editor_group.permissions.set(perms.filter(codename__in=["change_product", "view_product"]))
```

- `codename__in` → codename list এর মধ্যে যা আছে filter করবে।
- Editor শুধু edit এবং view করতে পারবে।

### 8️⃣ Viewer permission
```py
viewer_group.permissions.set(perms.filter(codename__in=["view_product"]))
```

Viewer শুধু দেখত পারে, edit বা add পারবে না।

###  Extra Use-case

- Article Model (blog অ্যাপ)
- Manager → সব permission
- Editor → edit + view
- Viewer → view only

```py
perms = Permission.objects.filter(content_type__app_label="blog", content_type__model="article")
editor_group.permissions.add(
    Permission.objects.get(codename='publish_article')
)
```

Custom permission বানানো সম্ভব, যেমন publish_article।