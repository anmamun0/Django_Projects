✅ Why? Recommended: drf-spectacular

<h6>
    
- Actively maintained
- Uses OpenAPI 3 (modern and standardized)
- Built for DRF
- Works with tools like Swagger UI, ReDoc

</h6>


#### 🔧 Installation & Setup
```bash 
pip install drf-spectacular
```

#### Update settings.py
```python
INSTALLED_APPS += ['drf_spectacular']

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```
#### Add URLs
```python 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```
#### ✅ Alternative: drf-yasg (if you prefer Swagger 2.0)

```bash 
pip install drf-yasg
```
#### Add to urls.py:

```python 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```


✅ After setup:
- Swagger UI 👉 http://localhost:8000/api/schema/swagger-ui/
- ReDoc UI 👉 http://localhost:8000/api/schema/redoc/
- Raw schema 👉 http://localhost:8000/api/schema/


<br> 
<br> 
<br> 
<br> 
<br> 

## Example: 


### 1. your_project_name/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),  # Your API endpoints
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

### 🔍 2. Why Login POST is missing?

<h6> 
DRF APIView doesn't automatically generate schemas because it doesn’t use @api_view or ViewSet. v

That’s why this won’t show up properly: <br> 
</h6>


```python 
class UserLoginView(APIView):
    def post(self, request):
        ...
```


### 3. ✅ Fix with @extend_schema

<h6> 
⚠️ If Your POST Endpoint Doesn’t Show in Schema  <br> 
❌ Problem: Login POST request isn’t showing parameters or JSON in Swagger or ReDoc? <br> 
    
That’s because APIView doesn’t auto-generate schema. <br> 
✅ Fix it using @extend_schema. <br> 
</h6>

```python
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes

class UserLoginView(APIView):
    
    @extend_schema(
        request=UserLoginSerializer,
        responses=OpenApiTypes.OBJECT,  # You can also use a response serializer here
        tags=["User"],
        operation_id="user_login_create",
        description="Log in a user and return auth token + user ID"
    )

    def post(self,request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            user = serializer._validated_data['user']
            if user:
                token , _ = Token.objects.get_or_create(user=user)
                login(request,user) 

                return Response({"token":token.key,"user_id":user.id, })
            else:
                return Response({"error":"Invalid Credential"})
        return Response(serializer.errors)
```

