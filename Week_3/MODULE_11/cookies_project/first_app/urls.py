from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='homepage'),
    path('',views.set_session,name='homepage'),
    path('cookie/',views.get_cookie,name='get_cookie'),
    path('delete/',views.delete_cookie,name='delete'),

    path('get_session/',views.get_session,name='get_session'),
]