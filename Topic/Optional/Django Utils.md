
# Django Utils 


<h6>

| **Module**                       | **Important Methods / Classes**                                                                                                                 | **কাজ**                                    |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **django.utils.crypto** [Go](#django-utils-crypto)          | `get_random_string()`, `pbkdf2()`, `constant_time_compare()`, `salted_hmac()`                                                                   | Secure hash, random string, password token |
| **django.utils.dateformat**      | `format()`, `time_format()`                                                                                                                     | Date/time কে custom string format          |
| **django.utils.dateparse**       | `parse_date()`, `parse_datetime()`, `parse_time()`                                                                                              | String → Date/Datetime/Time object         |
| **django.utils.dates**           | `MONTHS`, `MONTHS_3`, `WEEKDAYS`, `WEEKDAYS_ABBR`, `WEEKDAYS_REV`                                                                               | মাস/দিন এর নাম ও mapping                   |
| **django.utils.decorators**      | `method_decorator()`, `decorator_from_middleware()`, `decorator_from_middleware_with_args()`                                                    | Decorator tools, CBV এ decorator লাগানো    |
| **django.utils.deprecation**     | `RemovedInNextVersionWarning`, `MiddlewareMixin`                                                                                                | Old features deprecate করতে                |
| **django.utils.encoding**  [Go](#django-utils-encoding)      | `force_bytes()`, `force_str()`, `smart_bytes()`, `smart_str()`, `escape_uri_path()`                                                             | Text encoding safe করা                     |
| **django.utils.formats**         | `get_format()`, `date_format()`, `time_format()`, `number_format()`, `localize()`                                                               | Locale অনুযায়ী সংখ্যা/সময় format           |
| **django.utils.functional**      | `cached_property`, `lazy()`, `keep_lazy()`, `keep_lazy_text()`                                                                                  | Lazy evaluation, property cache            |
| **django.utils.html** [Go](#django-utils-html)  | `escape()`, `escapejs()`, `format_html()`, `format_html_join()`, `linebreaks()`, `strip_tags()`                                                 | HTML/XSS safe output                       |
| **django.utils.http** [Go](django-utils-http)           | `urlencode()`, `urlquote()`, `urlunquote()`, `http_date()`, `parse_http_date()`, `urlsafe_base64_encode()`, `urlsafe_base64_decode()`           | URL encode/decode, HTTP header parse       |
| **django.utils.module\_loading** | `import_string()`, `autodiscover_modules()`                                                                                                     | String path থেকে module/class load         |
| **django.utils.numberformat**    | `format()`, `format_lazy()`                                                                                                                     | সংখ্যা locale অনুযায়ী format               |
| **django.utils.safestring**  [Go](django-utils-safestring)    | `SafeString`, `SafeText`, `mark_safe()`, `SafeData`                                                                                             | String কে “safe” হিসেবে mark করা           |
| **django.utils.text**  [GO](#django-utils-text)          | `slugify()`, `get_valid_filename()`, `Truncator`, `wrap()`, `normalize_newlines()`                                                              | Slug বানানো, text truncate, clean filename |
| **django.utils.timezone**        | `now()`, `localtime()`, `is_aware()`, `is_naive()`, `make_aware()`, `make_naive()`, `activate()`, `deactivate()`                                | Timezone-aware datetime                    |
| **django.utils.translation**     | `gettext()`, `gettext_lazy()`, `ngettext()`, `ngettext_lazy()`, `pgettext()`, `pgettext_lazy()`, `get_language()`, `activate()`, `deactivate()` | i18n/L10n translation system               |
| **django.utils.version**         | `get_version()`, `get_docs_version()`                                                                                                           | Django version info                        |
| **django.utils.regex\_helper**   | `normalize()`, `replace_named_groups()`, `flatten_result()`                                                                                     | Regex pattern helper                       |



</h6>




---
<br>
<br>
<br>
<br>

### Detailed Table: django.utils modules & key methods / classes + ব্যবহার

<h6>

| **Module**                       | **Function / Class / Attribute**                                                      | **Why / Use (কেন ব্যবহার হয়)**                                                                                   |                       |
| -------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------- |
| **django.utils.cache**           | `patch_cache_control(response, **kwargs)`                                             | HTTP response এ `Cache-Control` header add / modify করে caching behavior control করার জন্য ([Django Project][1]) |                       |
|                                  | `get_max_age(response)`                                                               | `Cache-Control` থেকে `max-age` বের করার জন্য ([Django Project][1])                                               |                       |
|                                  | `patch_response_headers(response, cache_timeout=None)`                                | Response এ `Expires`, `Cache-Control` ইত্যাদি header add করার জন্য ([Django Project][1])                         |                       |
|                                  | `add_never_cache_headers(response)`                                                   | এমন header add করে যে response কোনো ধরনের cache এ রাখবে না ([Django Project][1])                                 |                       |
|                                  | `patch_vary_headers(response, newheaders)`                                            | Response এ `Vary` header update করতে ([Django Project][1])                                                       |                       |
|                                  | `get_cache_key(request, key_prefix=None, method='GET', cache=None)`                   | Request ভিত্তিতে cache key তৈরি/পায়                                                                              | ([Django Project][1]) |
|                                  | `learn_cache_key(request, response, cache_timeout=None, key_prefix=None, cache=None)` | প্রথমবার response তৈরি হলে, যা `Vary` হেডার নির্দেশ করে, সে অনুযায়ী future cache keys শিখতে                      | ([Django Project][1]) |
| **django.utils.dateparse**       | `parse_date(value)`                                                                   | String → `datetime.date` object convert করা                                                                      | ([Django Project][1]) |
|                                  | `parse_time(value)`                                                                   | String → `datetime.time` object convert করা                                                                      | ([Django Project][1]) |
|                                  | `parse_datetime(value)`                                                               | String → `datetime.datetime` convert করা (UTC offset সমর্থন সহ)                                                  | ([Django Project][1]) |
|                                  | `parse_duration(value)`                                                               | String → `datetime.timedelta` convert করা                                                                        | ([Django Project][1]) |
| **django.utils.decorators**      | `method_decorator(decorator, name='')`                                                | Class-based view method এ decorator লাগাতে                                                                       | ([Django Project][1]) |
|                                  | `decorator_from_middleware(middleware_class)`                                         | Middleware class থেকে view decorator বানাতে                                                                      | ([Django Project][1]) |
|                                  | `decorator_from_middleware_with_args(middleware_class)`                               | Middleware class + arguments দিয়ে decorator বানাতে                                                               | ([Django Project][1]) |
|                                  | `sync_only_middleware(middleware)`                                                    | Middleware কে synchronous-only হিসেবে mark করা                                                                   | ([Django Project][1]) |
|                                  | `async_only_middleware(middleware)`                                                   | Middleware কে asynchronous-only হিসেবে mark করা                                                                  | ([Django Project][1]) |
|                                  | `sync_and_async_middleware(middleware)`                                               | Middleware কে sync ও async দুটো মোডে কাজ করতে সক্ষম করা                                                          | ([Django Project][1]) |
| **django.utils.encoding**        | `smart_str(s, encoding='utf-8', strings_only=False, errors='strict')`                 | Python object → string convert করা, lazy objects resolve করা                                                     | ([Django Project][1]) |
|                                  | `force_str(s, encoding='utf-8', strings_only=False, errors='strict')`                 | lazy objects ছাড়া সব কিছুকে string এ convert করা                                                                 | ([Django Project][1]) |
|                                  | `smart_bytes(s, encoding='utf-8', strings_only=False, errors='strict')`               | Python object → bytes convert করা                                                                                | ([Django Project][1]) |
|                                  | `force_bytes(s, encoding='utf-8', strings_only=False, errors='strict')`               | lazy objects ছাড়া সব bytes এ convert করা                                                                         | ([Django Project][1]) |
|                                  | `iri_to_uri(iri)`                                                                     | IRIs (Internationalized Resource Identifiers) → URI (ASCII-safe) convert করা                                     | ([Django Project][1]) |
|                                  | `escape_uri_path(path)`                                                               | URL path এর unsafe chars escape করা                                                                              | ([Django Project][1]) |
| **django.utils.feedgenerator**   | `get_tag_uri(url, date)`                                                              | RSS feed এ Tag URI বানানো                                                                                        | ([Django Project][1]) |
|                                  | `Stylesheet` class                                                                    | RSS stylesheet represent করার জন্য                                                                               | ([Django Project][1]) |
|                                  | `SyndicationFeed` class                                                               | Base class for making RSS / Atom feed                                                                            | ([Django Project][1]) |
| **django.utils.functional**      | `cached_property(func)`                                                               | একটি method কে property বানানো + একবার calculate করে cache করা                                                   | ([Django Project][1]) |
|                                  | `classproperty(method)`                                                               | class-level property (classmethod style)                                                                         | ([Django Project][1]) |
|                                  | `keep_lazy(func, *resultclasses)`                                                     | Function কে lazy args কে support করতে enable করা                                                                 | ([Django Project][1]) |
|                                  | `keep_lazy_text(func)`                                                                | `keep_lazy(str)(func)` এর shortcut                                                                               | ([Django Project][1]) |
| **django.utils.html**            | `escape(text)`                                                                        | HTML special chars escape করা (XSS protection)                                                                   | ([Django Project][1]) |
|                                  | `conditional_escape(text)`                                                            | escape, কিন্তু preescaped strings এ double escape না করা                                                         | ([Django Project][1]) |
|                                  | `format_html(format_string, *args, **kwargs)`                                         | HTML string build করা, args/kwargs auto-escaped                                                                  | ([Django Project][1]) |
|                                  | `format_html_join(sep, format_string, args_generator)`                                | অনেক HTML parts join করতে safe way                                                                               | ([Django Project][1]) |
|                                  | `json_script(value, element_id=None, encoder=None)`                                   | JSON data safely embed করা `<script>` tag এ                                                                      | ([Django Project][1]) |
|                                  | `strip_tags(value)`                                                                   | String থেকে HTML tags remove করা                                                                                 | ([Django Project][1]) |
| **django.utils.http**            | `urlencode(query, doseq=False)`                                                       | Dictionary → URL query string বানানো, MultiValueDict সহ                                                          | ([Django Project][1]) |
|                                  | `http_date(epoch_seconds=None)`                                                       | HTTP standard datetime string তৈরি করা (RFC standard)                                                            | ([Django Project][1]) |
|                                  | `content_disposition_header(as_attachment, filename)`                                 | `Content-Disposition` HTTP header value তৈরি করা                                                                 | ([Django Project][1]) |
|                                  | `base36_to_int(s)`                                                                    | Base36 string → integer convert করা                                                                              | ([Django Project][1]) |
|                                  | `int_to_base36(i)`                                                                    | Integer → Base36 string convert করা                                                                              | ([Django Project][1]) |
|                                  | `urlsafe_base64_encode(s)`                                                            | Bytes → URL-safe base64 encode করা                                                                               | ([Django Project][1]) |
|                                  | `urlsafe_base64_decode(s)`                                                            | URL-safe base64 decode করা                                                                                       | ([Django Project][1]) |
| **django.utils.module\_loading** | `import_string(dotted_path)`                                                          | Dotted path string থেকে module/class import করা                                                                  | ([Django Project][1]) |
|                                  | `autodiscover_modules(module_name)`                                                   | প্রতিটি installed app এ নির্দিষ্ট module খুঁজে import করা                                                        | ([Django Project][1]) |
| **django.utils.safestring**      | `SafeString`, `SafeText`                                                              | “safe” HTML string class (escape না করা)                                                                         | ([Django Project][1]) |
|                                  | `mark_safe(s)`                                                                        | String কে safe হিসেবে mark করা                                                                                   | ([Django Project][1]) |
| **django.utils.text**            | `format_lazy(format_string, *args, **kwargs)`                                         | Lazy strings + format একসাথে support করা                                                                         | ([Django Project][1]) |
|                                  | `slugify(value, allow_unicode=False)`                                                 | String → URL slug (lowercase, remove invalid chars)                                                              | ([Django Project][1]) |
| **django.utils.timezone**        | `get_fixed_timezone(offset)`                                                          | Fixed-offset timezone object তৈরি করা                                                                            | ([Django Project][1]) |
|                                  | `get_default_timezone()`                                                              | Default timezone instance (settings.TIME\_ZONE)                                                                  | ([Django Project][1]) |
|                                  | `get_default_timezone_name()`                                                         | Default timezone name                                                                                            | ([Django Project][1]) |
|                                  | `get_current_timezone()`                                                              | Current timezone object (thread local)                                                                           | ([Django Project][1]) |
|                                  | `get_current_timezone_name()`                                                         | Current timezone name                                                                                            | ([Django Project][1]) |
|                                  | `activate(timezone)`                                                                  | Current thread এ timezone set করা                                                                                | ([Django Project][1]) |
|                                  | `deactivate()`                                                                        | Timezone deactivate করা                                                                                          | ([Django Project][1]) |
|                                  | `override(timezone)`                                                                  | Context manager / decorator to temporarily override timezone                                                     | ([Django Project][1]) |
|                                  | `localtime(value=None, timezone=None)`                                                | UTC-aware datetime → local time                                                                                  | ([Django Project][1]) |
|                                  | `is_aware(value)`                                                                     | Check if datetime is timezone-aware                                                                              | ([Django Project][1]) |
|                                  | `is_naive(value)`                                                                     | Check if datetime is naive (no tzinfo)                                                                           | ([Django Project][1]) |
|                                  | `make_aware(value, timezone=None)`                                                    | Naive datetime → Aware datetime in given timezone                                                                | ([Django Project][1]) |
|                                  | `make_naive(value, timezone=None)`                                                    | Aware datetime → Naive datetime in given timezone                                                                | ([Django Project][1]) |
| **django.utils.translation**     | `gettext(message)`                                                                    | Translate a message immediately                                                                                  | ([Django Project][1]) |
|                                  | `gettext_lazy(message)`                                                               | Lazy translation (deferred until string conversion)                                                              | ([Django Project][1]) |
|                                  | `pgettext(context, message)`                                                          | Context-aware translation                                                                                        | ([Django Project][1]) |
|                                  | `pgettext_lazy(context, message)`                                                     | Lazy context-aware translation                                                                                   | ([Django Project][1]) |
|                                  | `gettext_noop(message)`                                                               | Mark string for translation but don’t translate now                                                              | ([Django Project][1]) |
|                                  | `ngettext(singular, plural, number)`                                                  | Singular/plural translation based on number                                                                      | ([Django Project][1]) |
|                                  | `ngettext_lazy(singular, plural, number)`                                             | Lazy version of `ngettext`                                                                                       | ([Django Project][1]) |
|                                  | `npgettext(context, singular, plural, number)`                                        | Contextual plural translation                                                                                    | ([Django Project][1]) |
|                                  | `npgettext_lazy(context, singular, plural, number)`                                   | Lazy version of above                                                                                            | ([Django Project][1]) |
|                                  | `activate(language)`                                                                  | Activate a given translation language                                                                            | ([Django Project][1]) |
|                                  | `deactivate()`                                                                        | Deactivate translations (reset)                                                                                  | ([Django Project][1]) |
| **django.utils.version**         | `get_version()`                                                                       | Django version string                                                                                            | ([Django Project][1]) |
|                                  | `get_docs_version()`                                                                  | Version for docs (major.minor)                                                                                   | ([Django Project][1]) |
| **django.utils.regex\_helper**   | `normalize(pattern)`                                                                  | Normalize regex pattern                                                                                          | ([Django Project][1]) |
|                                  | `replace_named_groups(pattern, replacement)`                                          | Replace named groups in regex                                                                                    | ([Django Project][1]) |
|                                  | `flatten_result(matches)`                                                             | Flatten results from re module matches                                                                           | ([Django Project][1]) |

[1]: https://docs.djangoproject.com/en/5.2/ref/utils/?utm_source=chatgpt.com "Django Utils"


</h6>


---
<br>
<br>
<br>


# Django Utils HTML

[Home](#django-utils)

`django.utils.html`
<br>

 `escape()`, `escapejs()`, `format_html()`, `format_html_join()`, `linebreaks()`, `linebreaksbr()`, `strip_tags()`, `strip_spaces_between_tags()`, `urlize()`, `urlize_lazy()`, `avoid_wrapping()`, `html_safe()`

```py
from django.utils.html import (
    escape, escapejs, format_html, format_html_join,
    linebreaks, linebreaksbr, strip_tags, strip_spaces_between_tags,
    urlize, urlize_lazy, avoid_wrapping, html_safe
)

# 1. escape
unsafe_html = "<h1>Hello</h1>"
safe_html = escape(unsafe_html)  
print("Escape:", safe_html)  # output: &lt;h1&gt;Hello&lt;/h1&gt;

# 2. escapejs
unsafe_js = "alert('Hello <script>bad</script>')"
safe_js = escapejs(unsafe_js)
print("Escape JS:", safe_js)

# 3. format_html
html_text = format_html("<b>{}</b>", "Safe Text")
print("Format HTML:", html_text)  # output: <b>Safe Text</b>

# 4. format_html_join
items = ["Apple", "Banana", "Cherry"]
html_list = format_html_join(", ", "<li>{}</li>", ((item,) for item in items))
print("Format HTML Join:", html_list)  # output: <li>Apple</li>, <li>Banana</li>, <li>Cherry</li>

# 5. linebreaks
text_with_newlines = "Hello\nWorld"
print("Linebreaks:", linebreaks(text_with_newlines))  
# output: <p>Hello<br>World</p>

# 6. linebreaksbr
print("Linebreaks BR:", linebreaksbr(text_with_newlines))  
# output: Hello<br>World

# 7. strip_tags
html_string = "<p>Hello <b>World</b></p>"
print("Strip Tags:", strip_tags(html_string))  
# output: Hello World

# 8. strip_spaces_between_tags
html_with_spaces = "<div>   <span>Text</span>   </div>"
print("Strip Spaces:", strip_spaces_between_tags(html_with_spaces))  
# output: <div><span>Text</span></div>

# 9. urlize
text_with_url = "Visit https://www.djangoproject.com/ for docs"
print("Urlize:", urlize(text_with_url))  
# output: Visit <a href="https://www.djangoproject.com/">https://www.djangoproject.com/</a> for docs

# 10. urlize_lazy
lazy_func = urlize_lazy("Check https://github.com/")
print("Urlize Lazy:", lazy_func)  

# 11. avoid_wrapping
nowrap_text = avoid_wrapping("No wrap text")
print("Avoid Wrapping:", nowrap_text)  
# output: <span class="nowrap">No wrap text</span>

# 12. html_safe decorator
@html_safe
def custom_html():
    return "<b>Custom Safe HTML</b>"

print("Custom HTML Safe:", custom_html())
```


---
<br>
<br>
<br>
<br>

# Django Utils Text
[Home](#django-utils)

`django.utils.text`

<br>

 `slugify()`, `get_text_list()`, `Truncator()`, wrap()`, `unescape_entities()`,
    `normalize_newlines()`, `phone2numeric()`, `camel_case_to_spaces()`,
    `capfirst()`, `get_valid_filename()`, `smart_split()`

```py
from django.utils.text import (
    slugify, get_text_list, Truncator, wrap, unescape_entities,
    normalize_newlines, phone2numeric, camel_case_to_spaces,
    capfirst, get_valid_filename, smart_split
)

# 1. slugify
print("Slugify:", slugify("Hello World! Django Utils"))  
# output: hello-world-django-utils

# 2. get_text_list
print("Text List:", get_text_list(["Apple", "Banana", "Cherry"]))  
# output: Apple, Banana or Cherry

# 3. Truncator
t = Truncator("Django makes it easier to build better web apps quickly and with less code")
print("Truncate chars:", t.chars(20))  
# output: Django makes it e...
print("Truncate words:", t.words(5))  
# output: Django makes it easier...
print("Truncate words HTML:", Truncator("<p>Hello <b>World</b></p>").words(2, html=True))  
# output: <p>Hello <b>World...</b></p>

# 4. wrap
print("Wrap:", wrap("Django is awesome framework", 10))  
# output: ['Django is', 'awesome', 'framework']

# 5. unescape_entities
print("Unescape Entities:", unescape_entities("Tom &amp; Jerry &lt;3"))  
# output: Tom & Jerry <3

# 6. normalize_newlines
print("Normalize Newlines:", normalize_newlines("Line1\r\nLine2\rLine3\n"))  
# output: Line1\nLine2\nLine3\n

# 7. phone2numeric
print("Phone to Numeric:", phone2numeric("1800-FLOWERS"))  
# output: 18003569377

# 8. camel_case_to_spaces
print("Camel to Spaces:", camel_case_to_spaces("CamelCaseToWords"))  
# output: camel case to words

# 9. capfirst
print("Capfirst:", capfirst("django"))  
# output: Django

# 10. get_valid_filename
print("Valid Filename:", get_valid_filename("My File @2025.pdf"))  
# output: My_File_2025.pdf

# 11. smart_split
print("Smart Split:", list(smart_split("Some text 'with quotes' and more")))  
# output: ['Some', 'text', "'with quotes'", 'and', 'more']

```


# Django Utils SafeString

[Home](#django-utils)

`django.utils.safestring`

<br>

`mark_safe()`, `mark_for_escaping()`, `SafeString()`

```py
from django.utils.safestring import mark_safe, mark_for_escaping, SafeString
from django.utils.html import escape, escapejs

# 1. Normal unsafe string
html_string = "<b>Hello Django</b>"

# 2. mark_safe → টেমপ্লেটে raw HTML render করবে
safe_html = mark_safe(html_string)
print("Mark Safe:", safe_html, isinstance(safe_html, SafeString))
# Output: <b>Hello Django</b> True

# 3. mark_for_escaping → টেমপ্লেটে escape করবেই
escaped_html = mark_for_escaping(html_string)
print("Mark For Escaping:", escaped_html)
# Output: &lt;b&gt;Hello Django&lt;/b&gt;

# 4. escape → সব HTML char কে safe বানায়
print("Escape:", escape("<script>alert('XSS')</script>"))
# Output: &lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;

# 5. escapejs → JS context এ safe
print("Escape JS:", escapejs("Hello 'Django' <script>"))
# Output: Hello \u0027Django\u0027 \u003Cscript\u003E

# 6. Check if safe
print("Is Safe (raw):", isinstance(html_string, SafeString))  
# Output: False
print("Is Safe (safe_html):", isinstance(safe_html, SafeString))  
# Output: True

```


---
<br>
<br>
<br>
<br>

# Django Utils HTTP
[Home](#django-utils)

`django.utils.http`

<br>

 `urlquote()`, `urlquote_plus()`, `urlunquote()`, `urlunquote_plus()`, `urlencode()`,
    `urlsafe_base64_encode()`, `urlsafe_base64_decode()`, `int_to_base36()`, `base36_to_int()`


```py
from django.utils.http import (
    urlquote, urlquote_plus, urlunquote, urlunquote_plus, urlencode,
    urlsafe_base64_encode, urlsafe_base64_decode, int_to_base36, base36_to_int
)

# 1. urlquote
text = "Hello World!"
print("urlquote:", urlquote(text))
# Output: Hello%20World%21

# 2. urlquote_plus
print("urlquote_plus:", urlquote_plus(text))
# Output: Hello+World%21

# 3. urlunquote
encoded = "Hello%20World%21"
print("urlunquote:", urlunquote(encoded))
# Output: Hello World!

# 4. urlunquote_plus
encoded_plus = "Hello+World%21"
print("urlunquote_plus:", urlunquote_plus(encoded_plus))
# Output: Hello World!

# 5. urlencode
params = {'q': 'django utils', 'page': 2}
print("urlencode:", urlencode(params))
# Output: q=django+utils&page=2

# 6. urlsafe_base64_encode / decode
b = b"hello world"
encoded = urlsafe_base64_encode(b)
print("Base64 Encode:", encoded)
# Output: aGVsbG8gd29ybGQ=
decoded = urlsafe_base64_decode(encoded)
print("Base64 Decode:", decoded)
# Output: b'hello world'

# 7. int_to_base36 / base36_to_int
num = 123456
b36 = int_to_base36(num)
print("Int to Base36:", b36)
# Output: 2n9c
print("Base36 to Int:", base36_to_int(b36))
# Output: 123456

```



---
<br>
<br>
<br>

# Django Utils EnCoding

[Home](#django-utils)

`django.utils.encoding`

<br>

`force_bytes()`, `force_str()`, `smart_bytes()`, `smart_str()`, `iri_to_uri()`, `uri_to_iri()`
 
```py
from django.utils.encoding import (
    force_bytes, force_str, smart_bytes, smart_str, iri_to_uri, uri_to_iri
)

# 1. force_bytes
text = "Hello Django 🌐"
b = force_bytes(text)
print("force_bytes:", b)
# Output: b'Hello Django \xf0\x9f\x8c\x90'

# 2. force_str
print("force_str:", force_str(b))
# Output: Hello Django 🌐

# 3. smart_bytes
lazy_text = "Lazy String"
print("smart_bytes:", smart_bytes(lazy_text))
# Output: b'Lazy String'

# 4. smart_str
print("smart_str:", smart_str(b))
# Output: Hello Django 🌐

# 5. iri_to_uri
iri = "https://example.com/হেলো"
uri = iri_to_uri(iri)
print("IRI to URI:", uri)
# Output: https://example.com/%E0%A6%B9%E0%A7%87%E0%A6%B2%E0%A7%8B

# 6. uri_to_iri
print("URI to IRI:", uri_to_iri(uri))
# Output: https://example.com/হেলো
```


---
<br>
<br>
<br>
<br>

# Django Utils Crypto

[Home](#django-utils)

`django.utils.crypto`
<br>

`get_random_string()`, `constant_time_compare()`, `salted_hmac()`

```py
from django.utils.crypto import get_random_string, constant_time_compare, salted_hmac
from django.utils.encoding import force_bytes

# 1. get_random_string
random_token = get_random_string(16)
print("Random Token:", random_token)
# Output: k9F3Gh2LzPqRt8Xy  (example, varies each run)

# 2. constant_time_compare
a = "secure_value"
b = "secure_value"
c = "wrong_value"
print("Compare A & B:", constant_time_compare(a, b))  # True
print("Compare A & C:", constant_time_compare(a, c))  # False

# 3. salted_hmac
key_salt = "my_salt"
value = "user@example.com"
hmac = salted_hmac(key_salt, value).hexdigest()
print("HMAC:", hmac)
# Output: 1a2b3c... (example)

# 4. Using for password token
password = "mysecretpassword"
salt = get_random_string(8)
hashed = salted_hmac(salt, password).hexdigest()
print("Hashed Password Token:", hashed)
```