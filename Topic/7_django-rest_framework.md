## REST_Framework

| লাইব্রেরি (Module)              | কেন বেশি ব্যবহার হয়?                                        | সংক্ষিপ্ত উদাহরণ                 |
| ------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| **rest\_framework.serializers** | ডেটা ভ্যালিডেশন ও সিরিয়ালাইজ করার জন্য অপরিহার্য            | ModelSerializer, Serializer      |
| **rest\_framework.views**       | API endpoint তৈরি করার বেস ক্লাস থাকে এখানে                 | APIView                          |
| **rest\_framework.viewsets**    | CRUD অপারেশন সহজে করতে ModelViewSet ব্যবহার হয়              | ModelViewSet                     |
| **rest\_framework.response**    | রেসপন্স তৈরি করতে Response ক্লাস লাগে                       | Response({"msg": "success"})     |
| **rest\_framework.status**      | HTTP status কোডের রিডেবল কনস্ট্যান্ট                        | status.HTTP\_200\_OK             |
| **rest\_framework.permissions** | API তে ইউজার এক্সেস নিয়ন্ত্রণ করতে দরকার                    | IsAuthenticated, AllowAny        |
| **rest\_framework.decorators**  | ফাংশন বা ভিউতে সহজে permission, throttle ইত্যাদি যুক্ত করতে | @api\_view, @permission\_classes |

### rest_framework.serializers এর প্রধান ক্লাস ও ফিল্ডসমূহ (নাম, ব্যবহার)
: DRF এর বেস ক্লাস, যেটা দিয়ে তোমার নিজস্ব ফিল্ড ডিফাইন করে ডেটা সিরিয়ালাইজ ও ভ্যালিডেশন করতে পারো।
যদি তোমার ডেটা মডেলের সাথে সরাসরি না থাকে বা কাস্টম ফিল্ড ও ভ্যালিডেশন দরকার হয় তখন।
<h6>
    
| লাইব্রেরি (Library/Class)            | কাজ (Purpose)                            | সংক্ষিপ্ত বর্ণনা                            |
| ------------------------------------ | ---------------------------------------- | ------------------------------------------- |
| `serializers.Serializer`             | কাস্টম সিরিয়ালাইজার তৈরির জন্য           | মডেল ছাড়া ডেটা ভ্যালিডেশন ও সিরিয়ালাইজ করতে |
| `serializers.ModelSerializer`        | মডেল ভিত্তিক সিরিয়ালাইজার                | মডেল থেকে অটোমেটিক ফিল্ড তৈরি হয়            |
| `serializers.CharField`              | টেক্সট ইনপুট/আউটপুটের জন্য               | স্ট্রিং টাইপের ডেটা হ্যান্ডেল করে           |
| `serializers.IntegerField`           | পূর্ণসংখ্যার জন্য                        | ইনটিজার ভ্যালু ভ্যালিডেট করে                |
| `serializers.BooleanField`           | বুলিয়ান ডেটার জন্য                       | True/False হ্যান্ডেল করে                    |
| `serializers.EmailField`             | ইমেইল ইনপুটের জন্য                       | ইমেইল ফরম্যাট যাচাই করে                     |
| `serializers.DateTimeField`          | সময় ও তারিখের জন্য                       | ডেটটাইম ডেটা হ্যান্ডেল করে                  |
| `serializers.ListField`              | লিস্ট (তালিকা) ডেটার জন্য                | লিস্ট টাইপ ডেটা ইনপুট নেয়                   |
| `serializers.SerializerMethodField`  | কাস্টম রিড-অনলি ফিল্ড                    | সিরিয়ালাইজারের মেথড থেকে মান নেয়            |
| `serializers.PrimaryKeyRelatedField` | রিলেটেড অবজেক্টকে প্রাইমারি কি হিসেবে    | ফরেনকি হিসেবে আইডি দেয়                      |
| `serializers.StringRelatedField`     | রিলেটেড অবজেক্টের স্ট্রিং রেপ্রেজেন্টেশন | `__str__()` রিটার্ন করে                     |
| `serializers.SlugRelatedField`       | রিলেটেড অবজেক্টকে স্লাগ ফিল্ড হিসেবে     | ফরেনকি হিসেবে স্লাগ ইউজ করে                 |
| `serializers.ReadOnlyField`          | শুধু আউটপুটে দেখানোর জন্য                | ইনপুটে নেয় না                               |
| `serializers.WriteOnlyField`         | শুধু ইনপুটে নেওয়ার জন্য                  | আউটপুটে দেখায় না                            |
| `serializers.ValidationError`        | ভ্যালিডেশন এরর রেইজ করার জন্য            | ইনভ্যালিড ডেটায় এক্সসেপশন ছোঁড়ে             |

</h6>


### rest_framework.views এর প্রধান ক্লাস ও ফিল্ডসমূহ (নাম, ব্যবহার)
: DRF এর বেস ক্লাস যা HTTP মেথড (GET, POST, PUT, DELETE ইত্যাদি) হ্যান্ডল করে।
ক্লাস-ভিত্তিক API ভিউ তৈরি করার জন্য।

| নাম                    | কাজ                                 | সংক্ষিপ্ত উদাহরণ                     |
| ---------------------- | ----------------------------------- | ------------------------------------ |
| `APIView`              | ক্লাস-ভিত্তিক API view তৈরি         | `class MyView(APIView): ...`         |
| `Request`              | উন্নত HTTP রিকোয়েস্ট ক্লাস          | `request.data` থেকে ডেটা পাওয়া       |
| `Response`             | API রেসপন্স তৈরির ক্লাস             | `return Response({"msg": "ok"})`     |
| `ExceptionHandler`     | কাস্টম এক্সসেপশন হ্যান্ডলার সেট করা | settings.py তে কাস্টম হ্যান্ডলার সেট |
| `BrowsableAPIRenderer` | ব্রাউজারে ইন্টারেক্টিভ API দেখায়    | ডিফল্ট রেন্ডারার হিসেবে ব্যবহার      |
| `JSONParser`           | JSON ডেটা পার্স করে                 | `parser_classes = [JSONParser]`      |
| `FormParser`           | ফর্ম ডেটা পার্স করে                 |                                      |
| `MultiPartParser`      | মাল্টিপার্ট (ফাইল আপলোড) ডেটা পার্স |                                      |

### rest_framework.viewsets

: একটি বেস ক্লাস যা API এর ভিন্ন HTTP মেথড (GET, POST, PUT, DELETE) হ্যান্ডল করার জন্য মেথড ডিফাইন করতে দেয়।
 ভিউ লজিকগুলো সহজ ও রিইউজযোগ্য করে তুলতে।

<h6> 
    
| ক্লাস নাম              | কাজ                                        | ব্যবহার কেন?                    | সংক্ষিপ্ত উদাহরণ                                                   |
| ---------------------- | ------------------------------------------ | ------------------------------- | ------------------------------------------------------------------ |
| `ViewSet`              | কাস্টম API মেথড ডিফাইন করার জন্য           | সহজ কাস্টম ভিউ তৈরির জন্য       | `class MyViewSet(viewsets.ViewSet): ...`                           |
| `ModelViewSet`         | পুরো CRUD অপারেশন অটোমেটিকালি হ্যান্ডল করে | দ্রুত মডেলভিত্তিক API তৈরি করতে | `class ProductViewSet(viewsets.ModelViewSet): ...`                 |
| `ReadOnlyModelViewSet` | শুধু GET মেথড (list, retrieve) দেয়         | শুধুমাত্র পড়ার API দরকার হলে    | `class ProductReadOnlyViewSet(viewsets.ReadOnlyModelViewSet): ...` |
| `GenericViewSet`       | মিক্সিনের সাথে কাস্টম CRUD তৈরি করার জন্য  | কাস্টম অপারেশন দরকার হলে        | মিক্সিন ও ভিউসেট কম্বাইন করে        |
</h6>

### rest_framework.response

: এটা ডেটাকে স্বয়ংক্রিয়ভাবে রেন্ডার (যেমন JSON, XML) করে দেয় এবং HTTP স্ট্যাটাস কোড সেট করা যায়।
API থেকে ক্লায়েন্টকে JSON বা অন্য ফরম্যাটে ডেটা পাঠাতে ব্যবহার হয়।

```python
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class HelloView(APIView):
    def get(self, request):
        data = {"message": "Hello, world!"}
        return Response(data, status=status.HTTP_200_OK)
```


### rest_framework.status
API রেসপন্সে স্ট্যাটাস কোড ব্যবহারে readability ও maintainability বাড়ায়।

| কোড | নাম (Constant)                   | অর্থ                            |
| --- | -------------------------------- | ------------------------------- |
| 200 | `HTTP_200_OK`                    | সফল রেসপন্স                     |
| 201 | `HTTP_201_CREATED`               | নতুন রিসোর্স সফলভাবে তৈরি হয়েছে |
| 204 | `HTTP_204_NO_CONTENT`            | সফল অপারেশন, কোনো কনটেন্ট নেই   |
| 400 | `HTTP_400_BAD_REQUEST`           | ভুল রিকোয়েস্ট, ক্লায়েন্ট এরর    |
| 401 | `HTTP_401_UNAUTHORIZED`          | অথেনটিকেশন প্রয়োজন              |
| 403 | `HTTP_403_FORBIDDEN`             | নিষিদ্ধ, অনুমতি নেই             |
| 404 | `HTTP_404_NOT_FOUND`             | রিসোর্স পাওয়া যায়নি             |
| 500 | `HTTP_500_INTERNAL_SERVER_ERROR` | সার্ভার এরর                     |


### rest_framework.permissions
rest_framework.permissions হলো Django REST Framework (DRF)-এর একটি module, যা API access control বা user permissions ব্যবস্থাপনার জন্য ব্যবহৃত হয়।

| Permission Class            | ব্যাখ্যা (বাংলা)                                    | কবে ব্যবহার হয় |
| --------------------------- | --------------------------------------------------- | -------------- |
| `AllowAny`                  | সবার জন্য উন্মুক্ত (authenticated না হলেও চলবে)     | Public API     |
| `IsAuthenticated`           | শুধু logged-in ইউজার অ্যাক্সেস পাবে                 | Private API    |
| `IsAdminUser`               | শুধু admin ইউজার অ্যাক্সেস পাবে                     | Admin-only API |
| `IsAuthenticatedOrReadOnly` | logged-in হলে সব পারবে, না হলে শুধু read করতে পারবে | Semi-private   |
| `DjangoModelPermissions`    | Django এর model level permission অনুযায়ী কাজ করে    | RBAC systems   |
| `DjangoObjectPermissions`   | object-level permission প্রয়োগ করে                  | Advanced cases |

### rest_framework.decorators
rest_framework.decorators হলো Django REST Framework (DRF)-এর একটি module যা API views-এ function-based view (FBV) এবং class-based view (CBV) এর উপরে additional control ও functionality যোগ করতে ব্যবহৃত হয়।

| Decorator Name              | কাজ/ব্যবহার                                    | কোথায় ব্যবহার হয়     |
| --------------------------- | ---------------------------------------------- | -------------------- |
| `@api_view()`               | function কে DRF API view-এ রূপান্তর            | Function-based views |
| `@permission_classes()`     | কাস্টম permission নির্ধারণ                     | FBV                  |
| `@authentication_classes()` | Authentication ক্লাস নির্ধারণ                  | FBV                  |
| `@renderer_classes()`       | কোন format-এ response যাবে (JSON, XML)         | FBV                  |
| `@parser_classes()`         | কোন format-এ data ইনপুট parse হবে (JSON, form) | FBV                  |
| `@throttle_classes()`       | Rate limit control                             | FBV                  |
| `@action()`                 | ViewSet-এ extra actions যুক্ত করতে             | CBV (ViewSet)        |
