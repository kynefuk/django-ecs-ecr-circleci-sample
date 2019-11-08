from django.shortcuts import render, reverse

from django.http import HttpResponse
from django.views import generic
from .models import Todo
from .forms import TodoCreateForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TodoListView(generic.ListView):
    model = Todo
    template_name = 'todo/list.html'


class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = 'todo/create.html'
    form_class = TodoCreateForm

    def get_success_url(self):
        return reverse('todo:list')


def about(request):
    return HttpResponse("aboutページ")
