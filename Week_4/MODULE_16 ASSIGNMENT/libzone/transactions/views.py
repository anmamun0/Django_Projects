from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT ,PURCHASE,RETURN
from datetime import datetime
from django.db.models import Sum
from transactions.forms import DepositForm  
from transactions.models import Transaction
from django.template.loader import render_to_string

from django.core.mail import EmailMessage , EmailMultiAlternatives

from books.models import Book

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'profile': self.request.user.profile
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # template e context data pass kora
        context.update({
            'title': self.title
        })

        return context



class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        coin = form.cleaned_data.get('coin')
        profile = self.request.user.profile 
        profile.coin += coin  
        profile.save(
            update_fields=[
                'coin'
            ]
        ) 
        return super().form_valid(form)


class BuyBookView(TransactionCreateMixin,View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
 
        profile = request.user.profile
        user_coin = profile.coin
 
        if user_coin >= book.price: 
            profile.coin -= book.price
            profile.save() 
            Transaction.objects.create(
                profile=profile,
                book = book,
                coin = book.price,
                coin_after_transaction=profile.coin,
                transaction_type = PURCHASE,
            ) 
            messages.success(request, f'You have successfully purchased "{book.title}". Coin: {book.price}') 
            return redirect('books_details', book_id=book_id) 
        else: 
            messages.error(request, 'You do not have enough balance to buy this book.')
 
            return redirect('books_details', book_id=book_id) 
        
 

class ReturnBookView(TransactionCreateMixin, View):
    def get(self, request, trn_id):
        transaction = get_object_or_404(Transaction, pk=trn_id)
        profile = request.user.profile
        book = transaction.book   
        main_book = Book.objects.get(id=book.id)  
        print(main_book.id)   

        
        profile.coin += book.price
        profile.save(
            update_fields=[
                'coin'
            ]
        )  
        transaction.transaction_type = RETURN
        transaction.save() 

        messages.success(request, f'Thank you for returning the book. You have received {book.price} coins back.')
        # return redirect('profile')
    
        return redirect('books_details', book_id=main_book.id)  # Redirect to book details page
   