#  REST framework -views.py


 
### DRF Library Table
`from rest_framwork import ViewSets,APIView,Generic,Routers,Permissions,Authentication,Pagination`
<h6> 
  
| Component | 	Purpose	| Usage Example | 
|-----------|----------|-----------------|
| Serializers	| মডেল ডাটাকে JSON-এ রূপান্তর করা ও পুনরুদ্ধার করা	| serializers.ModelSerializer দিয়ে মডেল ডাটা সিরিয়ালাইজ করা| 
| ViewSets| 	CRUD অপারেশন পরিচালনা করা [see more.](#1-viewsets)	| ModelViewSet দিয়ে CRUD তৈরি করা | 
| APIView	| HTTP রিকোয়েস্ট কাস্টমাইজ করা	[see more.](#2-apiview)	| APIView ব্যবহার করে get(), post() মেথড ডিফাইন করা| 
| Generic|  Views	সাধারণ CRUD অপারেশন সহজ করা [see more.](#3-generic)	| 	ListCreateAPIView, RetrieveUpdateDestroyAPIView ব্যবহার করা| 
| Routers| 	স্বয়ংক্রিয়ভাবে URL তৈরি করা [see more.](#4-routers)	| DefaultRouter() দিয়ে ViewSet রেজিস্টার করা| 
| Permissions| 	API অ্যাক্সেস নিয়ন্ত্রণ করা [see more.](#5-permissions)	| 	IsAuthenticated, IsAdminUser ব্যবহার করে API নিরাপদ করা| 
| Authentication| 	ইউজার যাচাই করা [see more.](#6-authentication)	| 	TokenAuthentication, SessionAuthentication ব্যবহার করা| 
| Pagination| 	ডাটা সীমিত করে পেজিনেশন করা	[see more.](#7-pagination)	| PageNumberPagination, LimitOffsetPagination ব্যবহার করা| 



</h6>

---
<br>
<br>
<br>
<br>
 
## 1. ViewSets
[Home](#drf-library-table)

- ViewSet হল একটি ক্লাস, যা সাধারণ CRUD অপারেশনগুলোর জন্য প্রস্তুত করা হয়েছে। এটি ModelViewSet ব্যবহার করে সম্পূর্ণ CRUD (Create, Retrieve, Update, Delete) অপারেশন সহজেই পরিচালনা করে।
- স্বয়ংক্রিয়ভাবে CRUD (List, Retrieve, Create, Update, Delete) হ্যান্ডেল করে
- Routers-এর মাধ্যমে অটোমেটিক URL তৈরি হয়
- ModelViewSet ব্যবহার করলে অধিকাংশ কাজ সহজে সম্পন্ন হয়
- [more-explanation](#viewsets-more-explanation)

```python 
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```
##### ✔ ব্যবহার: ViewSet ব্যবহার করলে আলাদা আলাদা list, retrieve, create, update, ও delete মেথড লিখতে হয় না।

### Attributes in ModelViewSet

<h6>

| Attribute                | Type                           | Use                                                                                                               |
| ------------------------ | ------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `queryset`               | QuerySet                       | এই viewset কোন model এর data handle করবে তা define করে। উদাহরণ: `queryset = Category.objects.all()`               |
| `serializer_class`       | Serializer class               | কোন serializer দিয়ে data serialize/deserialize হবে তা define করে। উদাহরণ: `serializer_class = CategorySerializer` |
| `permission_classes`     | List of Permission classes     | Default permission define করে। উদাহরণ: `[IsAuthenticated]`                                                        |
| `authentication_classes` | List of Authentication classes | কোন authentication method ব্যবহার হবে তা define করে। উদাহরণ: `[TokenAuthentication]`                              |
| `pagination_class`       | Pagination class               | QuerySet pagination control করে।                                                                                  |
| `filter_backends`        | List of filter backend classes | Search, ordering, filter control করে। উদাহরণ: `[SearchFilter, OrderingFilter]`                                    |
| `search_fields`          | List of fields                 | Search filter এর জন্য ব্যবহার হয়।                                                                                 |
| `ordering_fields`        | List of fields                 | Order filter এর জন্য ব্যবহার হয়।                                                                                  |
| `lookup_field`           | String                         | Detail view এ object খুঁজতে কোন field use হবে। default `"pk"`                                                     |

</h6>

```py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import UserRateThrottle
from .models import Category
from .serializers import CategorySerializer
 
class CategoryView(ModelViewSet):
    # -------------------- Model and Serializer --------------------
    queryset = Category.objects.all()  # কোন model data serve করবে
    serializer_class = CategorySerializer  # কোন serializer use হবে

    # -------------------- Authentication and Permissions --------------------
    authentication_classes = [TokenAuthentication, SessionAuthentication]  # API কে authenticate করবে
    permission_classes = [AllowAny]  # ডিফল্টে GET anyone access পাবে

    # -------------------- Filter, Search, Ordering --------------------
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # filter, search, ordering support
    filterset_fields = ['name', 'status']  # filterable fields
    search_fields = ['name', 'description']  # searchable fields
    ordering_fields = ['name', 'created_at']  # orderable fields
    ordering = ['name']  # default ordering

    # -------------------- HTTP Methods --------------------
    http_method_names = ['get', 'post']  # PUT, PATCH, DELETE blocked

    # -------------------- Throttling --------------------
    throttle_classes = [UserRateThrottle]  # rate limit control
    throttle_scope = 'category'  # custom throttle scope

    # -------------------- Lookup Customization --------------------
    lookup_field = 'slug'  # URL থেকে object select করতে custom field
    lookup_url_kwarg = 'category_slug'  # URL keyword arg name
```


### Methods in ModelViewSet
ModelViewSet basically all CRUD operations support করে। DRF internally ViewSet + Mixins use করে।

<h6>

| Method / Overrideable Method                     | Description                                                            | HTTP Method / Type |
| ------------------------------------------------ | --------------------------------------------------------- | ------------------ |
| `initial(self, request, *args, **kwargs)`        | Request এর আগে run হয়; method block, header validation ইত্যাদি করা যায় | Override Method    |
| `get_permissions(self)`                          | Method-wise permission override করতে use হয়                            | Override Method/Custom    |
| `get_queryset(self)`                             | Dynamic queryset provide করতে use হয়                                   | Override Method    |
| `list(self, request, *args, **kwargs)`           | All objects list করে                                                   | GET                |
| `retrieve(self, request, *args, **kwargs)`       | Single object detail দেয়                                               | GET                |
| `create(self, request, *args, **kwargs)`         | নতুন object create করে                                                 | POST               |
| `update(self, request, *args, **kwargs)`         | Existing object update করে                                             | PUT                |
| `partial_update(self, request, *args, **kwargs)` | Existing object partial update করে                                     | PATCH              |
| `destroy(self, request, *args, **kwargs)`        | Existing object delete করে                                             | DELETE             |
| `perform_create(self, serializer)`               | Object save করার আগে extra logic execute করতে use হয়                   | Override Method    |
| `perform_update(self, serializer)`               | Object update করার আগে extra logic execute করতে use হয়                 | Override Method    |
| `perform_destroy(self, instance)`                | Object delete করার আগে extra logic execute করতে use হয়                 | Override Method    |
| `get_serializer(self, *args, **kwargs)`          | Serializer instance return করে, dynamic data pass করা যায়              | Override Method    |
| `get_serializer_class(self)`                     | Serializer class dynamicভাবে override করতে use হয়                      | Override Method    |
| `get_serializer_context(self)`                   | Serializer context (যেমন request, view) provide করতে use হয়            | Override Method    |
| `get_object(self)`                               | Single object fetch করার জন্য use হয়                                   | Override Method    |
| `paginate_queryset(self, queryset)`              | Queryset paginate করতে use হয়                                          | Override Method    |
| `get_paginated_response(self, data)`             | Paginated response return করতে use হয়                                  | Override Method    |
| `filter_queryset(self, queryset)`                | Queryset filter ও search করার জন্য use হয়                              | Override Method    |
  
</h6>


### 1. list()
[up](#methods-in-modelviewset)

ব্যবহার: সব objects এর list ফেরত দেয়।
```
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        # GET request handle
        print("List method called")
        return super().list(request, *args, **kwargs)
``` 
- এই method GET request এর জন্য call হয়।
- সব objects এর list return করতে super().list() use করা হয়।

### 2. retrieve()
[up](#methods-in-modelviewset)

ব্যবহার: একটি single object এর detail দেয়।
```py
def retrieve(self, request, *args, **kwargs):
    print("Retrieve method called")
    return super().retrieve(request, *args, **kwargs)
```
- URL এ /category/1/ দিলে id=1 এর object return করবে।

### 3. create()
[up](#methods-in-modelviewset)

ব্যবহার: নতুন object create করে।
```py
def create(self, request, *args, **kwargs):
    print("Create method called")
    return super().create(request, *args, **kwargs)
``` 
- POST request handle করে।
- Serializer validate করে save করে।

### 4. update()
[up](#methods-in-modelviewset)

ব্যবহার: existing object সম্পূর্ণ update করে।
```py
def update(self, request, *args, **kwargs):
    print("Update method called")
    return super().update(request, *args, **kwargs)
``` 
- PUT request handle করে।
- সম্পূর্ণ object replace করে নতুন data দিয়ে।

### 5. partial_update()
[up](#methods-in-modelviewset)

ব্যবহার: existing object partial update করে।
```py
def partial_update(self, request, *args, **kwargs):
    print("Partial update called")
    return super().partial_update(request, *args, **kwargs)
``` 
PATCH request handle করে। 
শুধু যেসব field পাঠানো হয়েছে, শুধু সেগুলো update করে।

### 6. destroy()
[up](#methods-in-modelviewset)

ব্যবহার: object delete করে।
```py
def destroy(self, request, *args, **kwargs):
    print("Destroy method called")
    return super().destroy(request, *args, **kwargs)
```
- DELETE request handle করে।

### 7. initial()
[up](#methods-in-modelviewset)

**What is `initial()` in DRF?**

<h5> 

  `initial()` is a special method in Django REST Framework's APIView class (which `ModelViewSet` inherits from). <br>
  It runs before the actual request handler methods like: `get()`, `post()`, `put()`, `destroy()`, etc.
</h5>



ব্যবহার: request এর আগে run হয়।
```py
def initial(self, request, *args, **kwargs):
    print(f"Request method: {request.method}")
    if request.method not in ["GET", "POST"]:
        from rest_framework.exceptions import MethodNotAllowed
        raise MethodNotAllowed(request.method)
    return super().initial(request, *args, **kwargs)
``` 
- সব request এর আগে execute হয়।
- আমরা এখানে GET এবং POST ছাড়া অন্য request block করেছি।

### 8. get_permissions()
[up](#methods-in-modelviewset)

ব্যবহার: method-wise permission override করতে।
```py
def get_permissions(self):
    if self.request.method == "GET":
        permission_classes = []  # public access
    else:
        permission_classes = [IsAuthenticated]  # POST, PUT, DELETE authenticated
    return [permission() for permission in permission_classes]
``` 
GET public, POST authenticated করতে use হয়।

### 9. get_queryset()
[up](#methods-in-modelviewset)

ব্যবহার: dynamic queryset provide করতে।
```py
def get_queryset(self):
    user = self.request.user
    if user.is_authenticated:
        return Category.objects.filter(user=user)
    return Category.objects.none()
``` 
user specific queryset return করতে use হয়।

### 10. perform_create()
[up](#methods-in-modelviewset)

ব্যবহার: object save করার আগে extra logic execute করতে।
```py
def perform_create(self, serializer):
    serializer.save(user=self.request.user)  # current logged in user assign
``` 
Serializer save করার আগে custom logic run করতে।

### 11. perform_update()
[up](#methods-in-modelviewset)

ব্যবহার: update করার আগে extra logic execute করতে।
```py
def perform_update(self, serializer):
    serializer.save(updated_by=self.request.user)
```
### 12. perform_destroy()
[up](#methods-in-modelviewset)

ব্যবহার: delete করার আগে extra logic execute করতে।
```py
def perform_destroy(self, instance):
    print(f"Deleting {instance}")
    instance.delete()
```
### 13. get_serializer_context()
[up](#methods-in-modelviewset)

ব্যবহার: serializer কে extra context provide করতে।
```py
def get_serializer_context(self):
    context = super().get_serializer_context()
    context['request_user'] = self.request.user
    return context
``` 
Serializer এর মধ্যে request বা extra info পাঠানোর জন্য।


---
<br>
<br>


```py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category
from .serializers import CategorySerializer

# Custom pagination
class CategoryPagination(PageNumberPagination):
    page_size = 10             # এক পেজে কতটা object দেখাবে
    page_size_query_param = 'size'  # URL ?size=5 দিয়ে change করতে পারবে
    max_page_size = 50

class CategoryView(ModelViewSet):
    # 1 Basic queryset
    queryset = Category.objects.all()

    # 2 Serializer
    serializer_class = CategorySerializer

    # 3 Authentication methods
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    # 4 Default permission (can override per method)
    permission_classes = [IsAuthenticated]

    # 5 Pagination
    pagination_class = CategoryPagination

    # 6 Filters
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']    # search ?search=xyz
    ordering_fields = ['name', 'created_at']   # order ?ordering=name
    ordering = ['name']                        # default ordering

    # 7 Method-wise permissions
    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            # GET requests anyone can access
            permission_classes = [AllowAny]
        else:
            # POST/PUT/PATCH/DELETE only authenticated users
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    # 8 Dynamic queryset example (optional)
    # def get_queryset(self):
    #     user = self.request.user
    #     return Category.objects.filter(user=user)

    # 9 Custom save logic
    def perform_create(self, serializer):
        # Automatically add current user to the category if needed
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Extra logic before update
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        # Extra logic before delete
        instance.delete()
```


---

<br>
<br>
<br>
<br>
<br>
<br>

## 2. APIView
[Home](#drf-library-table)

- APIView হলো ক্লাস-বেসড ভিউ (CBV), যা HTTP রিকোয়েস্টগুলোকে সম্পূর্ণ কাস্টমাইজ করতে দেয়। এটি ফাংশন-বেসড ভিউয়ের তুলনায় আরও বেশি কন্ট্রোল দেয়।

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentAPI(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

###### ✔ ব্যবহার: APIView ব্যবহার করলে আমরা GET, POST, PUT, ও DELETE রিকোয়েস্টকে নিজের মতো কাস্টমাইজ করতে পারি।

---
<br>
<br>
<br>
<br>

## 3. Generic Views
[Home](#drf-library-table)
 
- Generic Views হলো DRF-এর তৈরি করা ভিউ, যা আমাদের সাধারণ CRUD অপারেশনগুলো খুব সহজেই পরিচালনা করতে সাহায্য করে।

```python
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

###### ✔ ব্যবহার: Generic Views ব্যবহার করলে খুব কম কোড লিখেই আমরা API তৈরি করতে পারি।

---
<br>
<br>
<br>
<br>
## 4. Routers
[Home](#drf-library-table)
- Routers স্বয়ংক্রিয়ভাবে ViewSet-এর জন্য URL তৈরি করে, ফলে আমাদের আলাদা আলাদা urls.py সেটআপ করতে হয় না।
 

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
✔ ব্যবহার: Routers ব্যবহার করলে API-এর জন্য আলাদা আলাদা URL ম্যানুয়ালি লিখতে হয় না।
```

---
<br>
<br>
<br>
<br>

## 5. Permissions
[Home](#drf-library-table)
- Permissions নির্ধারণ করে কোন ইউজার API অ্যাক্সেস করতে পারবে।

```python
from rest_framework.permissions import IsAuthenticated

class StudentAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
```

###### ✔ ব্যবহার: শুধুমাত্র অথেনটিকেটেড ইউজাররা এই API অ্যাক্সেস করতে পারবে।

## 6. Authentication

[Home](#drf-library-table)
- Authentication ব্যবহারকারীদের যাচাই করে এবং সঠিক ইউজার হলে API অ্যাক্সেস দিতে সাহায্য করে।

🔹 প্রধান অথেনটিকেশন মেথড:
- 1️⃣ BasicAuthentication → ইউজারনেম ও পাসওয়ার্ড যাচাই করে।
- 2️⃣ TokenAuthentication → টোকেন ব্যবহার করে অথেনটিকেশন করে।
- 3️⃣ SessionAuthentication → Django-এর সেশন বেসড অথেনটিকেশন সিস্টেম ব্যবহার করে।
 
```python 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
```

✔ ব্যবহার: TokenAuthentication ব্যবহার করলে প্রতিটি ইউজারকে টোকেনের মাধ্যমে অথেনটিকেশন করতে হয়।

---
<br>
<br>
<br>
<br>


## 6. Pagination
[Home](#drf-library-table)

- Pagination ব্যবহার করলে API থেকে অনেক বেশি ডাটা রিটার্ন করলে সেটিকে ছোট ছোট অংশে ভাগ করে দেখানো যায়।
 
```python 
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
```

###### ✔ ব্যবহার: প্রতি পৃষ্ঠায় ৫টি ডাটা দেখানোর জন্য page_size=5 সেট করা হয়েছে।

🔹 সংক্ষেপে মূল বিষয়গুলো
| কম্পোনেন্ট	| কাজ| 
|-------------|------------|
| Serializers	| মডেল ডাটাকে JSON-এ রূপান্তর করা ও পুনরুদ্ধার করা| 
| ViewSets| 	স্বয়ংক্রিয়ভাবে CRUD অপারেশন পরিচালনা করা| 
| APIView| 	HTTP রিকোয়েস্ট কাস্টমাইজ করা| 
| Generic|  Views	সাধারণ CRUD অপারেশন সহজ করা| 
| Routers| 	স্বয়ংক্রিয়ভাবে URL তৈরি করা| 
| Permissions| 	API অ্যাক্সেস নিয়ন্ত্রণ করা| 
| Authentication| 	ইউজার যাচাই করা| 
| Pagination	| ডাটা সীমিত করে পেজিনেশন করা| 


Django REST Framework ব্যবহার করে আমরা সহজেই RESTful API তৈরি করতে পারি। DRF-এর Serializers, ViewSets, APIView, Generic Views, Routers, Permissions, Authentication, এবং Pagination আমাদের API ডেভেলপমেন্ট সহজ করে তোলে।




<br>
<br>
<br>
<br>
<br>
<br>


---

## ViewSets more explanation

- 🔹 ViewSets এর ধরন ও উদাহরণ

<h6> 
  
| ViewSet Class |	ব্যবহারের উদ্দেশ্য| 
|-------------|-------------------|
| ViewSet| 	কাস্টম লজিক সহ API তৈরি করতে ব্যবহৃত হয়| 
| ModelViewSet v	Full CRUD API স্বয়ংক্রিয়ভাবে হ্যান্ডেল করে| 
| ReadOnlyModelViewSet	 | শুধুমাত্র GET (List, Retrieve) অপারেশন কাজ করবে| 
| GenericViewSet	Mixins | ব্যবহার করে কাস্টম CRUD API তৈরি করা যায়| 
</h6>

### 🛠️ ১. Basic ViewSet Example
- 📌 ব্যবহার: যখন সম্পূর্ণ কাস্টমাইজড API তৈরি করতে চাই।

🔹 Code Example:

```python
from rest_framework import viewsets
from rest_framework.response import Response

class SampleViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "List of items"})

    def retrieve(self, request, pk=None):
        return Response({"message": f"Details of item {pk}"})
```

📌 API Routes:

<h6> 
  
| Method |	URL | 	কাজ | 
|-----------|-------|--------|
| GET	| /api/sample/ |	সব ডাটা দেখাবে | 
| GET	| /api/sample/{id}/ |	নির্দিষ্ট ডাটা দেখাবে | 

</h6>

### 🛠️ ২. ModelViewSet (Full CRUD API)
📌 ব্যবহার: যখন আমরা CRUD (Create, Read, Update, Delete) অপারেশন স্বয়ংক্রিয়ভাবে করতে চাই।
 
```python 
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

📌 API Routes:

<h6> 

| Method| 	URL| 	কাজ| 
|--------|----|-----------|
| GET	| /api/books/	| সব বই দেখাবে| 
| GET| 	/api/books/{id}/	| নির্দিষ্ট বই দেখাবে| 
| POST| 	/api/books/	| নতুন বই যোগ করবে| 
| PUT| 	/api/books/{id}/	| বই আপডেট করবে| 
| DELETE| 	/api/books/{id}/	| বই মুছে ফেলবে| 

</h6>

### 🛠️ ৩. ReadOnlyModelViewSet (শুধুমাত্র Read অপারেশন)
📌 ব্যবহার: যখন শুধু List & Retrieve অপারেশন দরকার হয়, Create/Update/Delete দরকার নেই।
 
```python 
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
```

📌 API Routes:
<h6> 
  
| Method | 	URL| 	কাজ | 
|--------|--------|---------|
| GET	| /api/authors/	| সব লেখকের তালিকা দেখাবে| 
| GET	| /api/authors/{id}/	| নির্দিষ্ট লেখক দেখাবে| 
| ❌ POST, PUT, DELETE সাপোর্ট করবে না। | | | 

</h6>

### 🛠️ ৪. GenericViewSet + Mixins (কাস্টম CRUD)
📌 ব্যবহার: যখন কিছু নির্দিষ্ট CRUD অপারেশন দরকার হয় (সম্পূর্ণ না)।

🔹 Code Example:

```python 
from rest_framework import viewsets, mixins
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

📌 API Routes:

<h6> 

| Method  | URL                      | কাজ                     |
|---------|--------------------------|--------------------------|
| GET     | `/api/movies/`           | সব মুভি দেখাবে          |
| GET     | `/api/movies/{id}/`      | নির্দিষ্ট মুভি দেখাবে   |
| ❌ POST, PUT, DELETE সাপোর্ট করবে না।| | |

</h6>

### 🛠️ ৫. GenericViewSet + Mixins (Full CRUD)
📌 ব্যবহার: ModelViewSet-এর মতো কাজ করবে, কিন্তু কাস্টমাইজ করা যাবে।
 
```python 
from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin, 
                     mixins.RetrieveModelMixin, 
                     mixins.CreateModelMixin, 
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

📌 API Routes:

<h6> 
  
| Method  | URL                      | কাজ                     |
|---------|--------------------------|--------------------------|
| GET     | `/api/products/`         | সব প্রোডাক্ট দেখাবে     |
| GET     | `/api/products/{id}/`    | নির্দিষ্ট প্রোডাক্ট দেখাবে |
| POST    | `/api/products/`         | নতুন প্রোডাক্ট যোগ করবে |
| PUT     | `/api/products/{id}/`    | প্রোডাক্ট আপডেট করবে   |
| DELETE  | `/api/products/{id}/`    | প্রোডাক্ট মুছে ফেলবে   |
  
</h6>

### 🛠️ ৬. Router ব্যবহার করে ViewSet-এর URL স্বয়ংক্রিয়ভাবে তৈরি করা
- ViewSets স্বয়ংক্রিয়ভাবে URL তৈরি করতে routers ব্যবহার করা হয়।

🔹 Code Example (urls.py):

```python 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # '/api/books/' তৈরি হবে

urlpatterns = [
    path('api/', include(router.urls)),
]
```
📌 এখানে:

- DefaultRouter স্বয়ংক্রিয়ভাবে CRUD API-র URL তৈরি করবে
- /api/books/ → সব বই দেখাবে
- /api/books/{id}/ → নির্দিষ্ট বই দেখাবে
- /api/books/{id}/update/ → বই আপডেট করবে (PUT)
- /api/books/{id}/delete/ → বই মুছে ফেলবে (DELETE)
  

🔹 উপসংহার
- ViewSet → সহজে CRUD API তৈরি করে
- ModelViewSet → সবচেয়ে বেশি ব্যবহৃত, কম কোডে পূর্ণ CRUD কাজ করে
- ReadOnlyModelViewSet → শুধু GET অপারেশন সাপোর্ট করে
- GenericViewSet → কাস্টম CRUD অপারেশন করতে মিক্সিনের সাথে ব্যবহার হয়
- Router → স্বয়ংক্রিয়ভাবে ViewSet এর URL তৈরি করে


 

<br>
<br>
<br>
<br>
<br>

---

## APIView more explanation 

<h6> 
  
APIView হলো Django REST Framework এর একটি ক্লাস যা Class-Based Views (CBV) ব্যবহার করে API তৈরি করতে সাহায্য করে। এটি Django-র View ক্লাসের উপর ভিত্তি করে তৈরি করা হয়েছে, কিন্তু এটি RESTful API তৈরির জন্য কিছু অতিরিক্ত ফিচার প্রদান করে, যেমন authentication, permission, throttling, parsers, renderers ইত্যাদি।

</h6>

### APIView এর বৈশিষ্ট্যসমূহ
- Low-Level Control: APIView ব্যবহারের মাধ্যমে HTTP GET, POST, PUT, DELETE মেথডগুলোর কাস্টম লজিক লেখা যায়।
- Explicit HTTP Methods: প্রতিটি HTTP request আলাদা করে হ্যান্ডেল করা যায় (যেমন get(), post(), put(), delete() ইত্যাদি)।
- Full Control: APIView আমাদের request, response, authentication, and permissions এর উপর সম্পূর্ণ নিয়ন্ত্রণ দেয়।
- No Automatic URL Routing: APIView ব্যবহারের সময় router ব্যবহার করতে হয় না, urls.py-তে ম্যানুয়ালি URL নির্ধারণ করতে হয়।


### APIView এর উদাহরণ (Example)
- 1. Read-Only API (GET Request): এটি একটি APIView যেখানে শুধু GET Method সাপোর্ট করে।

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Django REST Framework!"}, status=status.HTTP_200_OK)
```
- 👉 এন্ডপয়েন্ট: GET /api/hello/
- 👉 রেসপন্স:

```json 
{
    "message": "Hello, Django REST Framework!"
}
```

### 2. CRUD API (GET, POST, PUT, DELETE)
- এটি একটি APIView যা CRUD (Create, Read, Update, Delete) ফিচার প্রদান করে।

```python 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

👉 এন্ডপয়েন্ট:

- GET /api/products/{id}/ → নির্দিষ্ট প্রোডাক্ট দেখাবে।
- POST /api/products/ → নতুন প্রোডাক্ট যোগ করবে।
- PUT /api/products/{id}/ → প্রোডাক্ট আপডেট করবে।
- DELETE /api/products/{id}/ → প্রোডাক্ট ডিলিট করবে।

### 3. urls.py তে এন্ডপয়েন্ট যুক্ত করা
APIView ব্যবহার করলে, URL ম্যানুয়ালি সংযুক্ত করতে হয়:

```python 
from django.urls import path
from .views import HelloAPIView, ProductDetailAPIView

urlpatterns = [
    path('api/hello/', HelloAPIView.as_view(), name='hello-api'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-api'),
]
```

### APIView vs ViewSet

<h6> 
  
| বৈশিষ্ট্য	| APIView| 	ViewSet| 
|-----------|-----------|------------|
| ব্যবহার| 	কমপ্লেক্স কাস্টম লজিকের জন্য উপযুক্ত| 	স্ট্যান্ডার্ড CRUD API দ্রুত তৈরি করতে সহায়ক| 
| URL Routing	| ম্যানুয়ালি urls.py ফাইল এডিট করতে হয় | 	Routers স্বয়ংক্রিয়ভাবে URL তৈরি করে| 
| কন্ট্রোল| 	সম্পূর্ণ নিয়ন্ত্রণ পাওয়া যায়| 	কিছু সীমাবদ্ধতা থাকে| 
| Authentication & Permission	|  সম্পূর্ণ নিয়ন্ত্রণ	|  বিল্ট-ইন সাপোর্ট| 

কেন APIView ব্যবহার করবেন?
- যদি কাস্টম লজিক দরকার হয়।
- যদি আলাদা করে প্রতিটি HTTP মেথড পরিচালনা করতে হয়।
- যদি URL routing ম্যানুয়ালি নিয়ন্ত্রণ করতে চান।
- যদি বিল্ট-ইন ViewSet যথেষ্ট না হয়।
- এটি Django REST Framework এ APIView ব্যবহারের একটি বিস্তৃত ব্যাখ্যা। 🚀
- আপনি কি আরও কোনো নির্দিষ্ট বিষয় সম্পর্কে জানতে চান? 😊

</h6>




## APIViewset Registration form create
###### if already has models field (username,password field, first_name firld ,etc)  that why use ModelSerializers

##### serializers.py

```python
from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def validate_username(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError({'error_username':'username is already exist.',})
        return value

```

##### view.py

```python
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

class RegistrationView(APIView):
    serializer_class = RegistrationSerializer
    def post(self,request):
        form = self.serializer_class(data=request.data)
        if form.is_valid():
            username = form._validated_data['username']
            first_name = form._validated_data['first_name']
            password = form._validated_data['password']
            email = form._validated_data['email']
            user =  User.objects.create_user(username=username,password=password,first_name=first_name,email=email)

            return Response("Sended Data",status=status.HTTP_201_CREATED)
        return Response("Error",status=status.HTTP_502_BAD_GATEWAY)
```

##### urls.py

```python
from django.urls import path,include
from .views import RegistrationView

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register')
]
```



## APIViewset Login form 
###### if not has models field (username,password field, first_name firld ,etc)  that why use Serializers


<br>
<br>
<br>
<br>
<br>









---

## Generic more explanation

 
###### Django REST Framework (DRF) আমাদের Generic Views প্রদান করে, যা APIView-এর উপর ভিত্তি করে তৈরি এবং কমন CRUD অপারেশন সহজেই হ্যান্ডেল করতে সাহায্য করে। Generic Views ব্যবহার করলে আমাদের কম কোড লিখতে হয় এবং API দ্রুত ডেভেলপ করা যায়।

### Generic Views এর সুবিধাসমূহ
- কম কোডে বেশি কাজ – APIView-এর মতো আলাদা করে get(), post(), put(), delete() লিখতে হয় না।
- Built-in CRUD support – List, Create, Retrieve, Update, Delete সহজেই করা যায়।
- Less Boilerplate Code – কোড সংক্ষিপ্ত হয়।
- Mixin Classes ব্যবহার করা যায় – Code Reusability বাড়ায়।
- Generic Views ক্লাসের তালিকা

|Generic | View |	কাজ|
|-------|----------|----------|
| ListAPIView| 	সব ডাটা দেখায় (Read)| 
| RetrieveAPIView| 	নির্দিষ্ট ডাটা দেখায় (Read)| 
| CreateAPIView	| নতুন ডাটা তৈরি করে (Create)| 
| UpdateAPIView	| ডাটা আপডেট করে (Update)| 
| DestroyAPIView	| ডাটা মুছে ফেলে (Delete)| 
| ListCreateAPIView	| সব ডাটা দেখায় এবং নতুন ডাটা তৈরি করে (Read + Create)| 
| RetrieveUpdateAPIView	| নির্দিষ্ট ডাটা দেখায় এবং আপডেট করে (Read + Update)| 
| RetrieveDestroyAPIView	| নির্দিষ্ট ডাটা দেখায় এবং ডিলিট করে (Read + Delete)| 
| RetrieveUpdateDestroyAPIView	| নির্দিষ্ট ডাটা দেখায়, আপডেট করে এবং ডিলিট করে (Read + Update + Delete)| 

### Generic Views উদাহরণ

#### 1. Model ও Serializer তৈরি করা
- প্রথমে আমাদের models.py ও serializers.py তৈরি করতে হবে।

###### models.py
```python 
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
###### serializers.py

```python 
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

#### 2. Generic Views ব্যবহার করা

#### (a) সব প্রোডাক্ট লিস্ট দেখানো (ListAPIView)
- 
```python 
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
- 👉 URL: GET /api/products/

#### (b) নির্দিষ্ট প্রোডাক্ট দেখানো (RetrieveAPIView)

```python 
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
- 👉 URL: GET /api/products/{id}/

#### (c) নতুন প্রোডাক্ট যোগ করা (CreateAPIView)

```python 
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
- 👉 URL: POST /api/products/

#### (d) প্রোডাক্ট আপডেট করা (UpdateAPIView)

```python 
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
- 👉 URL: PUT /api/products/{id}/

#### (e) প্রোডাক্ট ডিলিট করা (DestroyAPIView)

```python 
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
- 👉 URL: DELETE /api/products/{id}/

### 3. Combined Views
#### (a) Read + Create (ListCreateAPIView)

```python 
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

##### 👉 URL:
- GET /api/products/ (সব প্রোডাক্ট দেখাবে)
- POST /api/products/ (নতুন প্রোডাক্ট যোগ করবে)

#### (b) Read + Update (RetrieveUpdateAPIView)

```python 
class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
##### 👉 URL:
- GET /api/products/{id}/ (নির্দিষ্ট প্রোডাক্ট দেখাবে)
- PUT /api/products/{id}/ (প্রোডাক্ট আপডেট করবে)

#### (c) Read + Delete (RetrieveDestroyAPIView)

```python 
class ProductRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```
##### 👉 URL:
- GET /api/products/{id}/ (নির্দিষ্ট প্রোডাক্ট দেখাবে)
- DELETE /api/products/{id}/ (প্রোডাক্ট মুছে ফেলবে)

##### (d) Read + Update + Delete (RetrieveUpdateDestroyAPIView)

```python 
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

##### 👉 URL:
- GET /api/products/{id}/ (নির্দিষ্ট প্রোডাক্ট দেখাবে)
- PUT /api/products/{id}/ (প্রোডাক্ট আপডেট করবে)
- DELETE /api/products/{id}/ (প্রোডাক্ট মুছে ফেলবে)

  
##### 4. urls.py তে URL যুক্ত করা

```python 
from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, 
    ProductUpdateView, ProductDeleteView, ProductRetrieveUpdateDestroyView
)

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/create/', ProductCreateView.as_view(), name='product-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('api/products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('api/products/<int:pk>/all/', ProductRetrieveUpdateDestroyView.as_view(), name='product-all'),
]
``` 
 
##### কেন Generic Views ব্যবহার করবেন?
- যদি স্ট্যান্ডার্ড CRUD API তৈরি করতে চান।
- যদি কম কোডে API ডেভেলপ করতে চান।
- যদি Mixin-ভিত্তিক API তৈরি করতে চান।






<br>
<br>
<br>
<br>
<br>
<br>


---

## Routers more explanation
  
###### Django REST Framework (DRF) এ Routers ব্যবহার করে আমরা সহজে ViewSet গুলোর জন্য URL Routing তৈরি করতে পারি। এটি ম্যানুয়ালি urlpatterns এ path() বা re_path() যোগ করার প্রয়োজনীয়তা কমিয়ে দেয়।

Router ব্যবহারের সুবিধাসমূহ
- ✅ কম কোড লিখতে হয় – ম্যানুয়ালি urlpatterns এ path() যুক্ত করতে হয় না।
- ✅ Auto-generated URLs – CRUD API Routes অটোমেটিক তৈরি হয়ে যায়।
- ✅ ViewSets-এর জন্য উপযোগী – ModelViewSet বা ViewSet এর সাথে ভালোভাবে কাজ করে।
- ✅ Code Reusability – একবার Router সেটআপ করলে, সহজেই API Endpoints তৈরি করা যায়।

##### Types of Routers in DRF: DRF এ প্রধানত দুই ধরনের Router আছে:

<h6> 
  
| Router	| কাজ| 
|----------|-------|
| SimpleRouter	| শুধুমাত্র list, create, retrieve, update, destroy রুট তৈরি করে | 
| DefaultRouter| 	SimpleRouter-এর সব ফিচার + একটি Browsable API root URL যোগ করে | 

</h6>
  
## 1. SimpleRouter ব্যবহার করা
- SimpleRouter শুধু CRUD URLs তৈরি করে, তবে Browsable API root URL দেয় না।

Example: SimpleRouter ব্যবহার করে Routing
Step 1: Model & Serializer তৈরি করা
models.py
```python 
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title
```

serializers.py

```python

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
```

Step 2: ViewSet তৈরি করা


```python
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

- 👉 ModelViewSet ব্যবহার করার ফলে list, create, retrieve, update, এবং destroy সব API Route অটোমেটিক কাজ করবে।

Step 3: Router ব্যবহার করে URL যুক্ত করা

##### urls.py

```python 
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MovieViewSet

router = SimpleRouter()
router.register(r'movies', MovieViewSet)  # "movies" হবে API-এর base URL

urlpatterns = [
    path('api/', include(router.urls)),  # Router থেকে auto-generated URL যুক্ত করা হলো
]
```

Generated API URLs (Auto-Generated)

<h6> 

| Method| 	URL| 	কাজ | 
|------|-------|--------|
| GET | 	/api/movies/	| সব মুভি দেখাবে| 
| POST	| /api/movies/	| নতুন মুভি যোগ করবে| 
| GET	| /api/movies/{id}/	| নির্দিষ্ট মুভি দেখাবে| 
| PUT	| /api/movies/{id}/	| মুভি আপডেট করবে | 
| DELETE	| /api/movies/{id}/	| মুভি মুছে ফেলবে | 

</h6>

## 2. DefaultRouter ব্যবহার করা
###### DefaultRouter হল SimpleRouter এর উন্নত সংস্করণ, যা Browsable API root URL (/api/) তৈরি করে।

### Example: DefaultRouter ব্যবহার করে Routing

##### urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```
- 👉 DefaultRouter ব্যবহারের ফলে /api/ এ root URL পাবেন, যেখানে API-এর সব endpoint লিস্ট আকারে দেখা যাবে।

Generated API URLs (Auto-Generated)

<h6> 
  
| Method	| URL	| কাজ| 
|---------|-------|-----|
| GET	| /api/	ব্রাউজেবল | API root দেখাবে| 
| GET| 	/api/movies/	| সব মুভি দেখাবে| 
| POST| 	/api/movies/	| নতুন মুভি যোগ করবে| 
| GET| 	/api/movies/{id}/	| নির্দিষ্ট মুভি দেখাবে| 
| PUT| 	/api/movies/{id}/	| মুভি আপডেট করবে| 
| DELETE| 	/api/movies/{id}/	| মুভি মুছে ফেলবে| 

</h6>

#### 3. Customizing ViewSet with Routers
- কখনো কখনো ViewSet এর কিছু নির্দিষ্ট CRUD অপারেশন নিষ্ক্রিয় করতে হয়।

##### Example: Read-Only API (Only List & Retrieve)

```python
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):  # Read-Only ViewSet
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```
- 👉 এটি শুধুমাত্র GET (list, retrieve) API তৈরি করবে, POST, PUT, DELETE নিষ্ক্রিয় থাকবে।

#### 4. Multiple ViewSets with Routers
- একাধিক ViewSet থাকলে একই Router এ রেজিস্টার করা যায়।

#### Example: Multiple API Endpoints

```python
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

👉 এটি /api/movies/ এবং /api/actors/ এই দুটি API endpoint তৈরি করবে।

#### 5. Custom Actions in ViewSets
- ViewSet এ কাস্টম @action যোগ করা যায়।

##### Example: কাস্টম API অ্যাকশন (top_movies/)

```python 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def top_movies(self, request):
        """শীর্ষ ৫ মুভি দেখাবে"""
        top_movies = Movie.objects.order_by('-release_date')[:5]
        serializer = self.get_serializer(top_movies, many=True)
        return Response(serializer.data)
```
##### Generated URL for Custom Action

- Method	URL- GET	/api/movies/top_movies/	শীর্ষ ৫ মুভি দেখাবে



##### 🚀 সংক্ষেপে Router-এর কাজ
- SimpleRouter শুধু CRUD URLs তৈরি করে।
- DefaultRouter Browsable API root (/api/) সহ CRUD URLs তৈরি করে।
- ViewSet এর সাথে Router ব্যবহার করলে urlpatterns কমে যায় এবং কোড সহজ হয়।



<br>
<br>
<br>
<br>
<br>
<br>

# Django REST Framework (DRF) Authentication and Pagination Guide

## Authentication more explanation

### 🔹 Why is DRF Authentication Necessary?
- ✅ Ensures security – Prevents anonymous users from modifying API data.
- ✅ Supports various authentication methods – Session, Token, JWT, OAuth, etc.
- ✅ Identifies users – Allows separate tokens or credentials for each user.

### 🔹 DRF Default Authentication Classes

Configure authentication in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
```

### 🔹 DRF Built-in Authentication Classes

| Authentication Class | Description |
|----------------------|-------------|
| SessionAuthentication | Uses Django session for user authentication. |
| BasicAuthentication | Uses username & password for HTTP Basic Authentication. |
| TokenAuthentication | Assigns a token to each user for API access. |
| JWT Authentication | Uses JSON Web Token (JWT) for API authentication. |
| OAuth Authentication | Supports third-party authentication (Google, Facebook, GitHub, etc.). |

### 🚀 1. SessionAuthentication (Default Django Session-based Authentication)

Example:

```python
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class SessionAuthView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, Welcome!"})
```

### 🚀 2. BasicAuthentication

Example:

```python
from rest_framework.authentication import BasicAuthentication

class BasicAuthView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated via Basic Auth!"})
```

### 🚀 3. TokenAuthentication

Install dependencies:

```bash
pip install djangorestframework
djangorestframework-authtoken
```

Configure `settings.py`:

```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

Example:

```python
from rest_framework.authentication import TokenAuthentication

class TokenAuthView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated using Token!"})
```

### 🚀 4. JWT Authentication

Install dependencies:

```bash
pip install djangorestframework-simplejwt
```

Configure `settings.py`:

```python
from rest_framework_simplejwt.authentication import JWTAuthentication

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

Example:

```python
class JWTAuthView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated using JWT!"})
```

---
<br>
<br>
<br>
<br>
<br>
<br>

## Pagination more explanation

### 🔹 What is Pagination?
Pagination divides API responses into smaller pages, improving performance and making frontend integration easier.

### 🔹 DRF Pagination Setup

Configure `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Shows 10 items per page
}
```

### 🔹 DRF Built-in Pagination Classes

| Pagination Class | Description |
|------------------|-------------|
| PageNumberPagination | Uses page numbers (`?page=2`). |
| LimitOffsetPagination | Uses limit & offset (`?limit=10&offset=20`). |
| CursorPagination | Uses secure cursor-based pagination (`?cursor=YXNkZmYxMjM=`). |

### 🚀 1. PageNumberPagination Example

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
```

### API Requests

```bash
GET /api/products/?page=2
GET /api/products/?page=2&page_size=10
```

### API Response

```json
{
    "count": 50,
    "next": "http://localhost:8000/api/products/?page=3",
    "previous": "http://localhost:8000/api/products/?page=1",
    "results": [
        {"id": 6, "name": "Product 6"},
        {"id": 7, "name": "Product 7"},
        {"id": 8, "name": "Product 8"}
    ]
}
```

🚀 Secure your API with DRF Authentication and optimize performance with Pagination! 😊
