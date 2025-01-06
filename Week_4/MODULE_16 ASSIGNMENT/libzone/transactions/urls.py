from django.urls import path 

from .views import DepositMoneyView ,BuyBookView,ReturnBookView
urlpatterns = [
    path('deposit/',DepositMoneyView.as_view(),name='deposit'),
    path('buy_now/<int:book_id>/',BuyBookView.as_view(),name='buy_now'),
    path('return_back/<int:trn_id>/',ReturnBookView.as_view(),name='return_back'),
]