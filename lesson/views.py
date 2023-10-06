from django.http import HttpResponse
from django.shortcuts import render
from .models import Lesson
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
def index(request):
    model=Lesson
    lesson = Lesson.objects.all()
    template_name = 'lesson/index.html'
    context_object_name = 'lesson'
    context = {
        'lesson': lesson
    }
    return render(request, 'lesson/index.html', context=context)


class NewsListView(ListView):
    model = Lesson