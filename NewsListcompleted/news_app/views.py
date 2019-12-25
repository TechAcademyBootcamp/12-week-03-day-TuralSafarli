from django.shortcuts import render
from news_app.models import News
from django.views.generic import ListView, DetailView
# import random

class NewsListView(ListView):
    model=News
    template_name= 'news.html'
    context_object_name='newslist'

class NewsDetailView(DetailView):
    model=News
    template_name='newsdetail.html'
    


# Create your views here.


   
    