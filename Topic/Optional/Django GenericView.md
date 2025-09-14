
# Django Generic Views  


1. Base Views (সব ভিউ এগুলো থেকে inherit করে)
`View` ,  `TemplateView`  , `RedirectView`

<h6>

| View Name        | কেন ব্যবহার হয় (Use Case)                                                      | উদাহরণ                                  |
| ---------------- | ------------------------------------------------------------------------------ | --------------------------------------- |
| **View**         | সব CBV এর বেস ক্লাস। নিজের কাস্টম HTTP method (get, post ইত্যাদি) define করতে। | `class MyView(View): def get(...): ...` |
| **TemplateView** | শুধু একটা টেমপ্লেট রেন্ডার করতে। কোনো জটিল লজিক দরকার নেই।                     | Static pages (About, Contact)           |
| **RedirectView** | এক URL থেকে আরেকটায় রিডাইরেক্ট করতে।                                           | পুরনো URL → নতুন URL                    |
</h6>

2. Object Views (Query Object Views)(একটা model object নিয়ে কাজ করে)
`DetailView`,`ListView`

<h6>

| View Name      | কেন ব্যবহার হয়                           | উদাহরণ                  |
| -------------- | ---------------------------------------- | ----------------------- |
| **DetailView** | নির্দিষ্ট একটার **object** দেখানোর জন্য। | Blog post details page  |
| **ListView**   | একসাথে অনেকগুলো object লিস্ট করার জন্য।  | Product list, Blog list |

</h6> 

4. Editing Views (Model Form Handling)(মডেলের সাথে Create, Update, Delete করার জন্য)
`FormView` `CreateView` `UpdateView` `DeleteView`

<h6>

| View Name      | কেন ব্যবহার হয়                                  | উদাহরণ                         |
| -------------- | ----------------------------------------------- | ------------------------------ |
| **FormView**   | Custom form হ্যান্ডল করার জন্য (model না হলেও)। | Contact form                   |
| **CreateView** | নতুন model object create করার জন্য।             | Add new product, Register user |
| **UpdateView** | বিদ্যমান object update করার জন্য।               | Profile edit                   |
| **DeleteView** | কোনো object delete করার জন্য।                   | Remove product, Delete post    |

</h6>

5. Date-Based Views(সময়/তারিখ অনুযায়ী data filter করার জন্য — blog/news এর জন্য বেশি ব্যবহৃত)

`ArchiveIndexView`, `YearArchiveView`, `MonthArchiveView`, `WeekArchiveView`, `DayArchiveView`, `TodayArchiveView`, `DateDetailView`

<h6>

| View Name            | কেন ব্যবহার হয়                                | উদাহরণ                         |
| -------------------- | --------------------------------------------- | ------------------------------ |
| **ArchiveIndexView** | নির্দিষ্ট তারিখ অনুযায়ী object-এর index view। | Blog archive page              |
| **YearArchiveView**  | বছরের ভিত্তিতে data filter করতে।              | Posts in 2025                  |
| **MonthArchiveView** | মাস অনুযায়ী data দেখাতে।                      | Posts in September 2025        |
| **WeekArchiveView**  | সপ্তাহ অনুযায়ী filter।                        | Weekly report                  |
| **DayArchiveView**   | নির্দিষ্ট দিনে data filter।                   | News published on 14 Sept 2025 |
| **TodayArchiveView** | আজকের ডেটার জন্য।                             | Today’s events                 |
| **DateDetailView**   | নির্দিষ্ট তারিখ + object এর ডিটেইল।           | News of a specific day         |

</h6>


### Attribute Summary


 | **Class**      | **Important Attributes**                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `TemplateView` | `template_name`, `get_context_data`                                                                                    |
| `ListView`     | `model`, `queryset`, `context_object_name`, `paginate_by`, `ordering`, `get_queryset()`                                |
| `DetailView`   | `model`, `queryset`, `context_object_name`, `pk_url_kwarg`, `slug_url_kwarg`, `slug_field`, `get_object()`             |
| `CreateView`   | `model`, `form_class`, `fields`, `template_name`, `success_url`, `form_valid()`, `form_invalid()`, `get_success_url()` |
| `UpdateView`   | `model`, `form_class`, `fields`, `template_name`, `success_url`, `get_object()`, `form_valid()`                        |
| `DeleteView`   | `model`, `template_name`, `success_url`, `get_object()`, `delete()`                                                    |


### Methods Summary

| **Class**      | **Methods**                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------ |
| `BaseView`     | `dispatch`, `setup`, `http_method_not_allowed`, `get_context_data`                               |
| `TemplateView` | `get_context_data`, `render_to_response`                                                         |
| `ListView`     | `get_queryset`, `get_context_data`, `get_ordering`, `paginate_queryset`, `get_paginate_by`       |
| `DetailView`   | `get_object`, `get_context_data`                                                                 |
| `CreateView`   | `get_form_class`, `get_form`, `get_form_kwargs`, `form_valid`, `form_invalid`, `get_success_url` |
| `UpdateView`   | `get_object`, `get_form_class`, `get_form`, `form_valid`, `form_invalid`, `get_success_url`      |
| `DeleteView`   | `get_object`, `get_context_data`, `delete`, `get_success_url`                                    |


---
<br>
<br>
<br>
<br>



# 1. BaseView (সব View এর common parent)


### Attributes
<h6>

| **Attribute / Method** | **Description**                               |
| ---------------------- | --------------------------------------------- |
| `self.request`         | বর্তমান request object (`HttpRequest`)        |
| `self.args`            | URLconf positional arguments                  |
| `self.kwargs`          | URLconf keyword arguments                     |
| `self.dispatch()`      | HTTP method route করে (`get()`, `post()` etc) |

</h6>


### Methods
<h6>

| **Method**                                          | **কাজ**                                                 |
| --------------------------------------------------- | ------------------------------------------------------- |
| `dispatch(request, *args, **kwargs)`                | HTTP method (GET/POST/PUT/DELETE) অনুযায়ী view call করে |
| `http_method_not_allowed(request, *args, **kwargs)` | method allow না করলে error দেয়                          |
| `get_context_data(**kwargs)`                        | Template context এ extra data যোগ করতে                  |
| `setup(request, *args, **kwargs)`                   | request process শুরুর আগে setup করার জন্য               |

</h6>



# 2. TemplateView


### Attributes
<h6>


| **Attribute / Method**       | **Description**                          |
| ---------------------------- | ---------------------------------------- |
| `template_name`              | কোন template render হবে                  |
| `get_context_data(**kwargs)` | Template এ অতিরিক্ত context পাঠানোর জন্য |

</h6>



### Methods
<h6>

| **Method**                                       | **কাজ**                            |
| ------------------------------------------------ | ---------------------------------- |
| `get_context_data(**kwargs)`                     | Template এ context data পাঠায়      |
| `render_to_response(context, **response_kwargs)` | Template render করে response পাঠায় |
</h6>






# 3. ListView 



### Attributes
<h6>

| **Attribute / Method** | **Description**                                         |
| ---------------------- | ------------------------------------------------------- |
| `model`                | কোন model থেকে ডাটা আনবে                                |
| `queryset`             | custom queryset ব্যবহার করা যাবে                        |
| `context_object_name`  | template এ object list এর নাম (default = `object_list`) |
| `paginate_by`          | pagination limit                                        |
| `ordering`             | default order সেট করতে                                  |
| `get_queryset()`       | custom queryset রিটার্ন করে                             |
| `get_context_data()`   | extra context পাঠাতে                                    |
| `object_list`          | context এ থাকা queryset                                 |

</h6>

### Methods

<h6>


| **Method**                               | **কাজ**                                    |
| ---------------------------------------- | ------------------------------------------ |
| `get_queryset()`                         | কোন queryset ব্যবহার করবে সেটা রিটার্ন করে |
| `get_context_data(**kwargs)`             | Template context extra customize করে       |
| `get_ordering()`                         | default ordering পরিবর্তন করতে             |
| `paginate_queryset(queryset, page_size)` | pagination handle করে                      |
| `get_paginate_by(queryset)`              | কত data প্রতি page থাকবে সেট করে           |
</h6>





# 3. 4. DetailView


### Attributes
<h6>

| **Attribute / Method** | **Description**                                    |
| ---------------------- | -------------------------------------------------- |
| `model`                | কোন model এর single object দেখাবে                  |
| `queryset`             | object আনার queryset                               |
| `context_object_name`  | template এ object এর নাম (default = `object`)      |
| `pk_url_kwarg`         | URL থেকে কোন kwarg দ্বারা pk নেবে (default = `pk`) |
| `slug_url_kwarg`       | URL থেকে কোন slug নেবে                             |
| `slug_field`           | model এর slug field নাম                            |
| `get_object()`         | object রিটার্ন করে                                 |
| `object`               | instance of model                                  |


</h6>
 
### Methods

<h6>

| **Method**                   | **কাজ**                           |
| ---------------------------- | --------------------------------- |
| `get_object(queryset=None)`  | কোন object দেখাবে সেটা return করে |
| `get_context_data(**kwargs)` | Template এ extra data পাঠায়       |

</h6>






# 5. CreateView


### Attributes

<h6>

| **Attribute / Method** | **Description**                            |
| ---------------------- | ------------------------------------------ |
| `model`                | কোন model এ নতুন object তৈরি হবে           |
| `form_class`           | কোন form ব্যবহার করবে                      |
| `fields`               | form auto generate এর জন্য model এর fields |
| `template_name`        | কোন template render হবে                    |
| `success_url`          | form valid হলে কোথায় redirect হবে          |
| `get_form()`           | form instance তৈরি করে                     |
| `form_valid(form)`     | form valid হলে কী হবে                      |
| `form_invalid(form)`   | form invalid হলে কী হবে                    |
| `get_success_url()`    | success\_url custom করার জন্য              |

</h6>


### Methods

<h6>

| **Method**                  | **কাজ**                                     |
| --------------------------- | ------------------------------------------- |
| `get_form_class()`          | কোন form class ব্যবহার করবে                 |
| `get_form(form_class=None)` | form instance তৈরি করে                      |
| `get_form_kwargs()`         | form এর initialization arguments return করে |
| `form_valid(form)`          | form valid হলে save করে                     |
| `form_invalid(form)`        | form invalid হলে আবার render করে            |
| `get_success_url()`         | success হলে redirect কোথায় হবে              |


</h6>


# 6. UpdateView


### Attributes

<h6>

| **Attribute / Method** | **Description**                        |
| ---------------------- | -------------------------------------- |
| `model`                | কোন model এর object update হবে         |
| `form_class`           | কোন form ব্যবহার করবে                  |
| `fields`               | কোন field update হবে                   |
| `template_name`        | কোন template render হবে                |
| `success_url`          | update complete হলে কোথায় redirect হবে |
| `get_object()`         | update করার জন্য object আনবে           |
| `form_valid(form)`     | update success হলে action              |
| `form_invalid(form)`   | error হলে action                       |

</h6>

### Methods
<h6>

| **Method**                  | **কাজ**                               |
| --------------------------- | ------------------------------------- |
| `get_object(queryset=None)` | কোন object update হবে সেটা return করে |
| `get_form_class()`          | form class return করে                 |
| `get_form(form_class=None)` | form instance return করে              |
| `form_valid(form)`          | update success হলে save করে           |
| `form_invalid(form)`        | invalid হলে আবার render করে           |
| `get_success_url()`         | redirect URL return করে               |

</h6>



# 7. DeleteView


### Attributes

<h6>

| **Attribute / Method** | **Description**                  |
| ---------------------- | -------------------------------- |
| `model`                | কোন model থেকে object delete হবে |
| `template_name`        | delete confirm করার template     |
| `success_url`          | delete complete হলে redirect     |
| `get_object()`         | কোন object delete হবে            |
| `delete()`             | delete action handle করে         |


</h6>

### Methods
<h6>

| **Method**                         | **কাজ**                                    |
| ---------------------------------- | ------------------------------------------ |
| `get_object(queryset=None)`        | কোন object delete হবে সেটা return করে      |
| `get_context_data(**kwargs)`       | Template context এ extra data পাঠায়        |
| `delete(request, *args, **kwargs)` | delete action perform করে                  |
| `get_success_url()`                | delete হয়ে গেলে কোথায় যাবে সেটা return করে |


</h6>



# Generic Class-Based View — Common Attributes & Methods
<h6>

| **Attribute / Method**                    | **Use / Description**                                                                   |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| `self.request`                            | বর্তমান request object (`HttpRequest`)। এর মধ্যে `GET`, `POST`, `user`, `session` থাকে। |
| `self.kwargs`                             | URLconf থেকে পাওয়া keyword arguments (যেমন: `<int:pk>`)।                                |
| `self.args`                               | URLconf থেকে পাওয়া positional arguments। খুব কম ব্যবহার হয়।                             |
| `self.object`                             | Single object (যেমন `DetailView` বা `UpdateView` এ)।                                    |
| `self.object_list`                        | Object এর queryset (যেমন `ListView` এ)।                                                 |
| `self.model`                              | কোন model নিয়ে কাজ করছে সেটা। (যদি সেট করা থাকে)                                        |
| `self.queryset`                           | কোন queryset ব্যবহার করছে সেটা (override করলে কাজ দেয়)।                                 |
| `self.form_class`                         | কোন form ব্যবহার করছে সেটা (যেমন `CreateView`, `UpdateView`)।                           |
| `self.template_name`                      | কোন template render হবে সেটা।                                                           |
| `self.context_object_name`                | template এ object এর জন্য context নাম।                                                  |
| `self.success_url`                        | form submit এর পর কোথায় redirect করবে।                                                  |
| `self.get_object()`                       | একটি object বের করে (Detail, Update, Delete views)।                                     |
| `self.get_queryset()`                     | queryset return করে (ListView, ইত্যাদি)।                                                |
| `self.get_context_data(**kwargs)`         | template এ context data যোগ করার জন্য।                                                  |
| `self.get_form()`                         | form instance তৈরি করে।                                                                 |
| `self.form_valid(form)`                   | form valid হলে কী হবে।                                                                  |
| `self.form_invalid(form)`                 | form invalid হলে কী হবে।                                                                |
| `self.get_success_url()`                  | কোথায় redirect করবে সেটি নির্ধারণ করে।                                                  |
| `self.dispatch(request, *args, **kwargs)` | HTTP method (`get`, `post`) কে handle করে।                                              |

</h6>

```py
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("dashboard")  # সফল হলে dashboard এ redirect
 
    def form_valid(self, form):
        response = super().form_valid(form)  # user save করবে
        login(self.request, self.object)     # self.object == নতুন user
        return response
```