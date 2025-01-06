from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView

from django.views.generic import DeleteView
from .models import Book, Category
# Create your views here.

from django.shortcuts import redirect

class BookView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()

        cat_slug  = kwargs.get('cat_slug',None) 

        if cat_slug:
            category = Category.objects.get(slug=cat_slug)
            books = Book.objects.filter(category=category)

        context['books'] = books
        context['categorys'] = Category.objects.all()

        return context
     

from review.forms import CommentForm
from transactions.models import Transaction
from django.contrib import messages
from transactions.constants import PURCHASE,RETURN
class BookDetailsView(FormView):
    template_name = 'book_details.html'
    model = Book
    pk_url_kwarg = 'book_id' 
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book_id = self.kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)
        context['book'] = book 
        context['related_books'] = Book.objects.all()[:5]

        context['similar_category_books'] = []
        for cat in book.category.all():
            some_books = Book.objects.filter(category=cat).exclude(id=book.id)  # Get books in the same category, excluding the current book
            context['similar_category_books'].extend(some_books)  # Append the books to the list

        context['comment_form'] = self.form_class()
        context['comments'] = book.comments.all()  # Assuming the `Book` model has a related_name 'comments'

        return context  
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not request.user.is_authenticated:
                messages.error(request,"Your should login for review")
                return redirect('login') 
        
        book_id = kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)

        profile = self.request.user.profile
        read = Transaction.objects.filter( profile=profile,  transaction_type__in=[PURCHASE, RETURN], book=book).exists()

        if  not read:
            messages.error(self.request, "You have not purchased the book. First, buy and read it to leave a review.")
            # Re-render the page with the current context 
            return redirect('books_details',book_id=book_id)

        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect('login') 
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            messages.success(request, "Your review has been submitted successfully!")
            return redirect('books_details', book_id=book_id)
 
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

 