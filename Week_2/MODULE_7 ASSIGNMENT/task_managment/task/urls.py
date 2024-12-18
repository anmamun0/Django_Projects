from django.urls import path
from .views import add_task,edit,delete

urlpatterns = [
    path('add_task/',add_task,name='add_task'),
    path('edit/<int:id>/',edit,name='edit_task'),
    path('delete/<int:id>/',delete,name='edit_delete'),
]