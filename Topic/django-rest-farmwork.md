file_name: rest_farmwork-view.py

in view.py
from rest_framwork import ViewSets,APIView,Generic,Routers,Permissions,Authentication,Pagination


📌 Django REST Framework (DRF) Summary Table
<h6> 
  
| Component | 	Purpose	| Usage Example | 
|-----------|----------|-----------------|
| Serializers	| মডেল ডাটাকে JSON-এ রূপান্তর করা ও পুনরুদ্ধার করা	| serializers.ModelSerializer দিয়ে মডেল ডাটা সিরিয়ালাইজ করা| 
| ViewSets| 	CRUD অপারেশন পরিচালনা করা	| ModelViewSet দিয়ে CRUD তৈরি করা| 
| APIView	| HTTP রিকোয়েস্ট কাস্টমাইজ করা	| APIView ব্যবহার করে get(), post() মেথড ডিফাইন করা| 
| Generic|  Views	সাধারণ CRUD অপারেশন সহজ করা| 	ListCreateAPIView, RetrieveUpdateDestroyAPIView ব্যবহার করা| 
| Routers| 	স্বয়ংক্রিয়ভাবে URL তৈরি করা	| DefaultRouter() দিয়ে ViewSet রেজিস্টার করা| 
| Permissions| 	API অ্যাক্সেস নিয়ন্ত্রণ করা| 	IsAuthenticated, IsAdminUser ব্যবহার করে API নিরাপদ করা| 
| Authentication| 	ইউজার যাচাই করা| 	TokenAuthentication, SessionAuthentication ব্যবহার করা| 
| Pagination| 	ডাটা সীমিত করে পেজিনেশন করা	| PageNumberPagination, LimitOffsetPagination ব্যবহার করা| 

</h6>


## 1️⃣  ViewSets
🔹 ব্যাখ্যা:
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


## 2️⃣ APIView

🔹 ব্যাখ্যা:
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


## 3️⃣ Generic Views

🔹 ব্যাখ্যা:
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

## 4️⃣ Routers
🔹 ব্যাখ্যা:
- Routers স্বয়ংক্রিয়ভাবে ViewSet-এর জন্য URL তৈরি করে, ফলে আমাদের আলাদা আলাদা urls.py সেটআপ করতে হয় না।
 

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
✔ ব্যবহার: Routers ব্যবহার করলে API-এর জন্য আলাদা আলাদা URL ম্যানুয়ালি লিখতে হয় না।
```

## 5️⃣ Permissions
🔹 ব্যাখ্যা:
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

## 6️⃣ Authentication

🔹 ব্যাখ্যা:
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

###### ✔ ব্যবহার: TokenAuthentication ব্যবহার করলে প্রতিটি ইউজারকে টোকেনের মাধ্যমে অথেনটিকেশন করতে হয়।

## 6️⃣ Pagination

🔹 ব্যাখ্যা:
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



APIView ক্লাস ব্যাখ্যা (Django REST Framework)
APIView হলো Django REST Framework এর একটি ক্লাস যা Class-Based Views (CBV) ব্যবহার করে API তৈরি করতে সাহায্য করে। এটি Django-র View ক্লাসের উপর ভিত্তি করে তৈরি করা হয়েছে, কিন্তু এটি RESTful API তৈরির জন্য কিছু অতিরিক্ত ফিচার প্রদান করে, যেমন authentication, permission, throttling, parsers, renderers ইত্যাদি।

APIView এর বৈশিষ্ট্যসমূহ
Low-Level Control: APIView ব্যবহারের মাধ্যমে HTTP GET, POST, PUT, DELETE মেথডগুলোর কাস্টম লজিক লেখা যায়।
Explicit HTTP Methods: প্রতিটি HTTP request আলাদা করে হ্যান্ডেল করা যায় (যেমন get(), post(), put(), delete() ইত্যাদি)।
Full Control: APIView আমাদের request, response, authentication, and permissions এর উপর সম্পূর্ণ নিয়ন্ত্রণ দেয়।
No Automatic URL Routing: APIView ব্যবহারের সময় router ব্যবহার করতে হয় না, urls.py-তে ম্যানুয়ালি URL নির্ধারণ করতে হয়।
APIView এর উদাহরণ (Example)
1. Read-Only API (GET Request)
এটি একটি APIView যেখানে শুধু GET Method সাপোর্ট করে।

python
Copy
Edit
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Django REST Framework!"}, status=status.HTTP_200_OK)
👉 এন্ডপয়েন্ট: GET /api/hello/
👉 রেসপন্স:

json
Copy
Edit
{
    "message": "Hello, Django REST Framework!"
}
2. CRUD API (GET, POST, PUT, DELETE)
এটি একটি APIView যা CRUD (Create, Read, Update, Delete) ফিচার প্রদান করে।

python
Copy
Edit
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
👉 এন্ডপয়েন্ট:

GET /api/products/{id}/ → নির্দিষ্ট প্রোডাক্ট দেখাবে।
POST /api/products/ → নতুন প্রোডাক্ট যোগ করবে।
PUT /api/products/{id}/ → প্রোডাক্ট আপডেট করবে।
DELETE /api/products/{id}/ → প্রোডাক্ট ডিলিট করবে।
3. urls.py তে এন্ডপয়েন্ট যুক্ত করা
APIView ব্যবহার করলে, URL ম্যানুয়ালি সংযুক্ত করতে হয়:

python
Copy
Edit
from django.urls import path
from .views import HelloAPIView, ProductDetailAPIView

urlpatterns = [
    path('api/hello/', HelloAPIView.as_view(), name='hello-api'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-api'),
]
APIView vs ViewSet
বৈশিষ্ট্য	APIView	ViewSet
ব্যবহার	কমপ্লেক্স কাস্টম লজিকের জন্য উপযুক্ত	স্ট্যান্ডার্ড CRUD API দ্রুত তৈরি করতে সহায়ক
URL Routing	ম্যানুয়ালি urls.py ফাইল এডিট করতে হয়	Routers স্বয়ংক্রিয়ভাবে URL তৈরি করে
কন্ট্রোল	সম্পূর্ণ নিয়ন্ত্রণ পাওয়া যায়	কিছু সীমাবদ্ধতা থাকে
Authentication & Permission	সম্পূর্ণ নিয়ন্ত্রণ	বিল্ট-ইন সাপোর্ট
কেন APIView ব্যবহার করবেন?
যদি কাস্টম লজিক দরকার হয়।
যদি আলাদা করে প্রতিটি HTTP মেথড পরিচালনা করতে হয়।
যদি URL routing ম্যানুয়ালি নিয়ন্ত্রণ করতে চান।
যদি বিল্ট-ইন ViewSet যথেষ্ট না হয়।
এটি Django REST Framework এ APIView ব্যবহারের একটি বিস্তৃত ব্যাখ্যা। 🚀
আপনি কি আরও কোনো নির্দিষ্ট বিষয় সম্পর্কে জানতে চান? 😊


