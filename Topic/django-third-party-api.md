# Learning third-party API integration 
###### in Django requires understanding both Django's request-handling system and how external APIs work. Here’s a structured approach to mastering it:

## 1. Understand the Basics of APIs
##### Before diving into Django, make sure you understand:

<h6> 
    
- What is an API? (REST, SOAP, GraphQL)
- HTTP Methods: GET, POST, PUT, DELETE
- Authentication Types: API keys, OAuth, JWT
- Status Codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 500 Internal Server Error
- Common API Formats: JSON, XML
</h6>

## 2. Learn How to Make API Requests in Python
##### Since Django is Python-based, you should first get comfortable with the requests library:

```python 
import requests

response = requests.get('https://api.example.com/data')
data = response.json()
print(data)
```
👉 Install it using:

```sh 
pip install requests
```

## 3. Use Third-Party APIs in Django Views
##### In Django, API integration usually happens in views. Example:

```python 
import requests
from django.http import JsonResponse

def fetch_data(request):
    url = "https://api.example.com/data"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=response.status_code)
```

## 4. Work with External APIs in Django REST Framework (DRF)
##### If you are building a Django REST API that integrates with a third-party API, use Django REST Framework:

Install DRF:
```sh 
pip install djangorestframework
```

##### Example of calling an external API inside a DRF view:

```python 
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def external_api_view(request):
    api_url = "https://api.example.com/data"
    response = requests.get(api_url)

    if response.status_code == 200:
        return Response(response.json())
    else:
        return Response({"error": "API request failed"}, status=response.status_code)
```

## 5. Handling Authentication for Third-Party APIs
Different APIs require different authentication methods:

API Key Authentication:

```python 
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(url, headers=headers)
```

OAuth 2.0 Authentication: Use requests_oauthlib library.
Install it:

```sh 
pip install requests_oauthlib
```

Example:

```python 
from requests_oauthlib import OAuth1Session
oauth = OAuth1Session(client_key, client_secret, resource_owner_key, resource_owner_secret)
response = oauth.get("https://api.example.com/user")
```

## 6. Handle Errors and Logging
Always handle exceptions when making API calls:

```python 
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
    data = {"error": "API request failed"}
Use Django’s built-in logging:

```python 
import logging
logger = logging.getLogger(__name__)

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logger.error(f"API request failed: {e}")
```

## 7. Storing API Data in Django Models
If you need to save data from an API:

```python 
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.TextField()

def save_api_data():
    response = requests.get("https://api.example.com/weather")
    if response.status_code == 200:
        data = response.json()
        WeatherData.objects.create(
            city=data["city"],
            temperature=data["temp"],
            description=data["weather"]
        )
```

## 8. Asynchronous API Calls with Celery
If an API call takes too long, use Celery for async processing:

Install Celery:

```sh 
pip install celery
```
Configure Celery in Django (settings.py):

```python 
CELERY_BROKER_URL = 'redis://localhost:6379/0'
```

Create an async API task:

```python 
from celery import shared_task
import requests

@shared_task
def fetch_weather():
    response = requests.get("https://api.example.com/weather")
    if response.status_code == 200:
        return response.json()
```

## 9. Learn by Practicing

<h6> 
    
- Try integrating APIs like:
- OpenWeatherMap API – Weather data
- Google Maps API – Location & Geocoding
- Stripe API – Payments
- Twilio API – SMS & Calls
- GitHub API – User repositories
</h6>

###### For example, fetching GitHub user details:

```python 
response = requests.get("https://api.github.com/users/anmamun0")
print(response.json())
```

## 10. Explore Django Packages for API Integration

##### Instead of manually calling APIs, you can use Django packages:

<h6> 
    
- Django-Allauth – For OAuth authentication
- Django-Social-Auth – For social login with Google, Facebook, etc.
- Django-Twilio – For integrating Twilio services

Final Tips <br>
- ✅ Start with simple APIs (GET requests).
- ✅ Gradually move to authentication-based APIs (API keys, OAuth).
- ✅ Use DRF if you're working on REST API integration.
- ✅ Learn async handling (Celery) for better performance.
- ✅ Practice by integrating APIs into Django projects.

</h6>



 --- 
 ---





##### Great! To dive deeper into third-party API integration in Django, let's explore advanced concepts with hands-on examples.

## 1. Advanced API Integration Concepts
##### To master API integration, you should understand: ✅ Rate Limiting – Handling API request limits

<h6> 

- ✅ Caching API Responses – Improving performance
- ✅ Webhooks – Reacting to external API events
- ✅ Async API Calls – Making Django API calls faster
- ✅ Error Handling & Logging – Debugging API failures
- ✅ OAuth & JWT Authentication – Secure API usage
- ✅ GraphQL APIs – Working with non-REST APIs

</h6>

## 2. Working with API Rate Limits
##### Most third-party APIs have rate limits. If you exceed the limit, the API blocks requests.

- Solution: Implement Rate Limiting
- Check API headers for limits:

```python
response = requests.get("https://api.example.com/data")
print(response.headers.get("X-RateLimit-Remaining"))
```

#### Use backoff to Handle Rate Limits
Install backoff:

```sh 
pip install backoff
```

Retry if requests fail due to rate limits:

```python 
import requests
import backoff

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=5)
def fetch_data():
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
    return response.json()

data = fetch_data()
```

##### This prevents exceeding limits by retrying with exponential backoff.

## 3. Caching API Responses in Django
To avoid making too many API calls, cache responses.

#### Django Cache Example
- Use Redis or local memory caching.

Install Redis:

```sh 
pip install django-redis
```
Update settings.py:

```python 
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}
```
Cache API responses:

```python 
from django.core.cache import cache
import requests

def get_weather():
    cached_data = cache.get("weather_data")
    if cached_data:
        return cached_data
    
    response = requests.get("https://api.example.com/weather")
    data = response.json()
    cache.set("weather_data", data, timeout=600)  # Cache for 10 minutes
    return data
```
##### This reduces API calls and speeds up Django responses.

## 4. Using Webhooks in Django
Instead of polling an API, webhooks let APIs send data when an event occurs.

- Example: Handle Stripe Payment Webhook
- Create a Django View to Receive Webhook

```python 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def stripe_webhook(request):
    if request.method == "POST":
        event = request.body  # Process event data
        print("Received webhook:", event)
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)
```

Update urls.py

```python 
from django.urls import path
from .views import stripe_webhook

urlpatterns = [
    path('webhook/', stripe_webhook, name='stripe_webhook'),
]
```

-  Register the Webhook in Stripe
-  Go to the Stripe Dashboard → Developers → Webhooks
-  Add https://yourdomain.com/webhook/

✅ Webhooks let your Django app react to external API events.

## 5. Asynchronous API Calls with Django & Celery
If an API request takes too long, make it asynchronous.

Install Celery:

```sh 
pip install celery
```

Configure Celery in settings.py:

```python 
CELERY_BROKER_URL = 'redis://localhost:6379/0'
```

Create an Async Task to Fetch Data:

```python 
from celery import shared_task
import requests

@shared_task
def fetch_external_api():
    response = requests.get("https://api.example.com/data")
    return response.json()
```

Call Task from Django View:

```python 
from .tasks import fetch_external_api

def api_view(request):
    fetch_external_api.delay()  # Runs in the background
    return JsonResponse({"message": "Fetching API data asynchronously"})
```

#####  Now, Django doesn’t block while waiting for API responses.

## 6. Handling API Authentication Securely

-  OAuth Authentication with Requests
-  For APIs requiring OAuth (e.g., Google, GitHub, Twitter):

```sh 
pip install requests-oauthlib
```

```python 
from requests_oauthlib import OAuth2Session

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
token_url = "https://api.example.com/oauth/token"

oauth = OAuth2Session(client_id)
token = oauth.fetch_token(token_url, client_secret=client_secret)
response = oauth.get("https://api.example.com/user")
print(response.json())
```

✅ This secures API calls using OAuth authentication.

## 7. Calling GraphQL APIs in Django

- Many modern APIs use GraphQL instead of REST.

- Example: Fetching Data from GitHub GraphQL API

```python 
import requests

url = "https://api.github.com/graphql"
headers = {"Authorization": "Bearer YOUR_GITHUB_TOKEN"}

query = """
{
  user(login: "anmamun0") {
    name
    repositories(first: 5) {
      nodes {
        name
        url
      }
    }
  }
}
"""

response = requests.post(url, json={"query": query}, headers=headers)
print(response.json())
```

✅ This retrieves data in a single optimized request.

## 8. Error Handling and Logging for API Failures

Improve Debugging by Logging API Errors

```python
import logging

logger = logging.getLogger(__name__)

try:
    response = requests.get("https://api.example.com/data", timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logger.error(f"API request failed: {e}")
```

✅ This logs failed API calls for debugging.

## 9. Automating API Calls with Django Management Commands

- Example: Create a Management Command to Call an API
- Create a fetch_api.py file inside app/management/commands/

Add the following:

```python 
from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = "Fetch data from API"

    def handle(self, *args, **kwargs):
        response = requests.get("https://api.example.com/data")
        self.stdout.write(self.style.SUCCESS(response.json()))
```

Run it:

```sh 
python manage.py fetch_api
```

✅ This helps automate API data fetching via cron jobs.

## 10. Real-World API Integration Project Ideas

<h6> 
    
 Want to practice? Try these projects:
- Weather Dashboard – Fetch weather data via OpenWeatherMap API
- Stock Price Tracker – Use Alpha Vantage API for stock data
- Currency Converter – Integrate Forex exchange API
- GitHub Explorer – Fetch GitHub user details & repos
- E-commerce Payment – Integrate Stripe API for payments
- Automated Email Sending – Use SendGrid API

</h6>