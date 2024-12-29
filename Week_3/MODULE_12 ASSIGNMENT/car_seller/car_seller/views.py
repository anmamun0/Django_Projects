from django.shortcuts import render, redirect
from brands.models import Brand
from cars.models import Car
from comments.models import Comment
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['cars'] = Car.objects.all()
        comments = Comment.objects.all()[:2]
        context['comments'] = comments
         
        brand_slug  = kwargs.get('brand_slug',None) 
        if brand_slug:
            brand = Brand.objects.get(slug=brand_slug)
            cars = Car.objects.filter(brand=brand)
            context['cars'] = cars

        return context
 