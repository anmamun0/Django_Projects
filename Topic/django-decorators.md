###### In Django REST Framework (DRF), decorators are used to simplify views by adding functionality like authentication, permissions, throttling, and more. Below is a list of the main decorators in DRF with explanations in Bengali:

## 1. @api_view
ব্যাখ্যা:
এই ডেকোরেটরটি Django views-এর জন্য ব্যবহার করা হয়, যেখানে আপনি একটি সাধারণ function-based view তৈরি করতে পারেন। @api_view ডেকোরেটর HTTP মেথডের (যেমন GET, POST) জন্য views তৈরির সময় সাহায্য করে।

ব্যবহার:

```python 
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_items(request):
    data = {"message": "Hello, world!"}
    return Response(data)
```

ব্যাখ্যা:
এই ডেকোরেটরটি get_items view কে GET HTTP রিকোয়েস্টের জন্য অনুমতি দেয়।

## 2. @action
ব্যাখ্যা:
এই ডেকোরেটরটি Django REST Framework এর viewsets-এ ব্যবহার করা হয়। এটি ব্যবহার করে আপনি custom actions তৈরি করতে পারেন, যেগুলি সাধারণ CRUD অপারেশন থেকে আলাদা।

ব্যবহার:

```python 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

class ItemViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def get_item_details(self, request, pk=None):
        # Custom logic here
        return Response({"message": "Item details"})
```

ব্যাখ্যা:
এখানে @action ডেকোরেটরটি get_item_details action তৈরি করছে, যা একটি GET রিকোয়েস্টের জন্য নির্দিষ্ট আইটেমের বিস্তারিত তথ্য ফেরত দেবে।

## 3. @permission_classes
ব্যাখ্যা:
এই ডেকোরেটরটি view-এর জন্য পারমিশন কন্ট্রোল নির্ধারণ করতে ব্যবহৃত হয়। এটি নিশ্চিত করে যে কে বা কী রিকোয়েস্ট করার অনুমতি পাবে এবং কে পাবে না।

ব্যবহার:

```python 
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

@permission_classes([IsAuthenticated])
class ItemView(APIView):
    def get(self, request):
        return Response({"message": "This is a secure endpoint"})
```

ব্যাখ্যা:
এখানে @permission_classes ডেকোরেটরটি নিশ্চিত করছে যে শুধুমাত্র Authenticated user এই view-access করতে পারবে।

4. @authentication_classes
ব্যাখ্যা:
এই ডেকোরেটরটি view-এর জন্য Authentication classes নির্ধারণ করে। এটি ব্যবহার করে আপনি কিভাবে এবং কোন পদ্ধতিতে ইউজারের পরিচয় যাচাই করবেন তা নিয়ন্ত্রণ করতে পারেন।

ব্যবহার:

```python 
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes

@authentication_classes([TokenAuthentication])
class ItemView(APIView):
    def get(self, request):
        return Response({"message": "Authenticated!"})
```

ব্যাখ্যা:
এখানে TokenAuthentication ব্যবহার করা হয়েছে, যার মাধ্যমে টোকেনের মাধ্যমে authentication হবে।

## 5. @throttle_classes
ব্যাখ্যা:
এই ডেকোরেটরটি ডেকোরেটেড view-এর জন্য throttle classes (rate-limiting) নির্ধারণ করে। এটি ব্যবহার করে আপনি রিকোয়েস্টের সংখ্যা সীমিত করতে পারেন।

ব্যবহার:

```python 
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import throttle_classes

@throttle_classes([UserRateThrottle])
class ItemView(APIView):
    def get(self, request):
        return Response({"message": "This endpoint is rate-limited"})
```

ব্যাখ্যা:
এখানে UserRateThrottle ব্যবহার করা হয়েছে, যা প্রতি ব্যবহারকারীর জন্য নির্দিষ্ট রিকোয়েস্ট সীমা নির্ধারণ করবে।

## 6. @renderer_classes
ব্যাখ্যা:
এই ডেকোরেটরটি একটি view-এর জন্য renderer নির্ধারণ করে, অর্থাৎ ডেটা কিভাবে রেন্ডার হবে তা নিয়ন্ত্রণ করে (যেমন JSON বা XML)।

ব্যবহার:

```python
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes

@renderer_classes([JSONRenderer])
class ItemView(APIView):
    def get(self, request):
        return Response({"message": "Rendered as JSON"})
```

ব্যাখ্যা:
এখানে JSONRenderer ব্যবহার করা হয়েছে, যা রেসপন্সকে JSON ফরম্যাটে রেন্ডার করবে।

## 7. @parse_error
ব্যাখ্যা:
এই ডেকোরেটরটি একটি custom exception handler হিসাবে কাজ করে, যা কাস্টম error মেসেজ প্রদর্শন করতে সাহায্য করে।

ব্যবহার:

```python 
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@parser_classes([JSONParser])
def parse_view(request):
    return Response({"message": "Parsed successfully"})
```

ব্যাখ্যা:
এখানে JSONParser ব্যবহার করা হয়েছে, যা কেবল JSON ডাটা রিকোয়েস্ট থেকে পাস করবে।

## 8. @swagger_auto_schema
ব্যাখ্যা:
এই ডেকোরেটরটি Django REST Framework এর জন্য Swagger UI ব্যবহার করে API ডকুমেন্টেশন তৈরি করার জন্য ব্যবহৃত হয়।

ব্যবহার:

```python 
from rest_framework.decorators import swagger_auto_schema

@swagger_auto_schema(operation_description="This is a description of the endpoint")
def my_view(request):
    return Response({"message": "Swagger documented!"})
```

ব্যাখ্যা:
এখানে swagger_auto_schema ডেকোরেটরটি API endpoint-এর ডকুমেন্টেশন বর্ণনা যোগ করতে ব্যবহার করা হয়েছে।

## 9. @csrf_exempt
ব্যাখ্যা:
এই ডেকোরেটরটি CSRF (Cross-Site Request Forgery) সুরক্ষা নিষ্ক্রিয় করতে ব্যবহৃত হয়। এটা Django REST Framework views-এ ব্যবহৃত হতে পারে, যেখানে আপনি CSRF সুরক্ষা ব্যবহার না করতে চান।

ব্যবহার:

```python 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['POST'])
def my_view(request):
    return Response({"message": "CSRF is exempted!"})
```

ব্যাখ্যা:
এখানে @csrf_exempt CSRF সুরক্ষা নিষ্ক্রিয় করে দিয়েছে, যাতে POST রিকোয়েস্ট CSRF ভ্যালিডেশন না করে।

উপসংহার:
এই ডেকোরেটরগুলো Django REST Framework-এর জন্য গুরুত্বপূর্ণ। তারা views-এর মধ্যে বিভিন্ন ধরনের কার্যক্রম (যেমন পারমিশন, অথেন্টিকেশন, থ্রোটলিং, ডাটা রেন্ডারিং) সহজে এবং কার্যকরীভাবে যুক্ত করতে সাহায্য করে।

এগুলি ব্যবহার করলে Django অ্যাপ্লিকেশনগুলো আরও নিরাপদ এবং স্কেলেবল হতে পারে।