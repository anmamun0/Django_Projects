from django.shortcuts import render ,redirect

from django.views.generic import CreateView , DetailView , UpdateView  ,TemplateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CarForm
from .models import Car
# Create your views here.
from django.urls import reverse_lazy,reverse
from django.contrib import messages

from django.views import View

from auth_system.models import History
from django.contrib.auth.decorators import login_required

class CarView(LoginRequiredMixin,CreateView):
    template_name = 'add_car.html'
    form_class = CarForm
    model = Car 
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,"Added successfull")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"invalid info")
        return super().form_invalid(form)

    
from comments.forms import CommentForm
from comments.models import Comment

class DetailsCarView(DetailView):
    template_name = 'details_car.html'
    model = Car
    pk_url_kwarg = 'id'
    def post(self,request,*args,**kwargs):
        
        comment_form = CommentForm(request.POST)
        if self.request.user.is_authenticated:
            if comment_form.is_valid():
                post = Car.objects.get(pk=self.kwargs['id'])
                print(post.name)
                comment_form.post = post
                c = comment_form.save(commit=False)
                c.post = post
                c.commented_user = request.user
                c.save()
                return redirect('details_car',id=self.kwargs['id'])
        else:
            return  redirect('login')

        return super().get(request,args,kwargs)

    def get_context_data(self, **kwargs):
        post = Car.objects.get(pk=self.kwargs['id'])
        comment_form = CommentForm()
        comments = Comment.objects.filter(post=post).all()

        context =  super().get_context_data(**kwargs)
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


class EditCarView(LoginRequiredMixin,UpdateView):
    template_name = 'edit_car.html'
    form_class = CarForm
    model = Car
    pk_url_kwarg = 'id' 
    def get_success_url(self):
        return reverse_lazy('details_car',kwargs={'id':self.object.pk})
    def form_valid(self, form):
        messages.success(self.request,"Edit successfull")
        return super().form_valid(form)
    
class DeleteCarView(LoginRequiredMixin,DeleteView):  
    model = Car
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    template_name = 'confirm_delete_car.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, "Car deleted successfully!")
        return redirect(self.success_url)


@login_required() 
def update_now(request, buy_id=None):
    if buy_id:
        car = Car.objects.get(pk=buy_id) 
        user = request.user
        history = user.history

        print(user.username) 
        if car.quantity > 0:
            car.quantity -= 1
            car.save()  
            History.objects.create(
                title=f"Purchased {car.name}",
                money=car.price,  # Assuming `car.price` exists
                author=user  # Set the logged-in user as the author
            )
            messages.success(request, 'Congratulation! Best of luck!') 

        else:
            messages.error(request,'Unabilable Cars')
        return redirect('details_car', id=buy_id)
    else:
        return redirect('homepage')

     