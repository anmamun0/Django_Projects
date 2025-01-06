from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from books.models import Book, Category
from transactions.models import Transaction

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all() 
        # Safely retrieve specific categories by ID or other fields (e.g., slug or name)
        try:
            first_cat = Category.objects.get(id=1)  # Replace `id=1` with your actual identifier
            second_cat = Category.objects.get(id=2)
            third_cat = Category.objects.get(id=3)
            four_cat = Category.objects.get(id=4)
        except Category.DoesNotExist:
            first_cat = second_cat = third_cat = four_cat = None
 
        # Fetch books for each category if the category exists
        # Fetch up to 4 books for each category if the category exists
        first_cat_books = Book.objects.filter(category=first_cat)[:4] if first_cat else []
        second_cat_books = Book.objects.filter(category=second_cat)[:4] if second_cat else []
        third_cat_books = Book.objects.filter(category=third_cat)[:4] if third_cat else []
        four_cat_books = Book.objects.filter(category=four_cat)[:4] if four_cat else []


        context['first_cat'] = first_cat
        context['second_cat'] = second_cat
        context['third_cat'] = third_cat
        context['four_cat'] = four_cat
        # Add the results to context
        context['first_cat_books'] = first_cat_books
        context['second_cat_books'] = second_cat_books
        context['third_cat_books'] = third_cat_books
        context['four_cat_books'] = four_cat_books 
        return context 

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['historys'] = Transaction.objects.filter(profile=self.request.user.profile)
        return context