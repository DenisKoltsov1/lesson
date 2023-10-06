from django.http import HttpResponse
from django.shortcuts import render
from .models import Lesson
from user.models import  MyUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
def index(request):
   
    model=Lesson
    model = MyUser
    lesson = Lesson.objects.all()
    template_name = 'lesson/index.html'
    context_object_name = 'lesson'
    context_object_name = 'user'
    context = {
        'lesson': lesson,
        
    }

    
    return render(request, 'lesson/index.html', context=context)


class NewsListView(ListView):
    model = Lesson