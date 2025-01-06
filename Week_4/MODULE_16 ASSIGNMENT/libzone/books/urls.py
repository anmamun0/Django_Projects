from django.urls import path,include

from .views import BookView, BookDetailsView

urlpatterns = [
    path('',BookView.as_view(),name='books'),
    path('cat/<slug:cat_slug>/',BookView.as_view(),name='filter_category'),
    path('details/<int:book_id>/',BookDetailsView.as_view(),name='books_details'),
]
