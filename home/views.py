from django.shortcuts import render
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-pub_date')
    return render(request, 'home/index.html', {'todos': todos})


def add_todo(request):
    now = timezone.now()
    todo_text = request.POST['todo_text']
    Todo.objects.create(pub_date=now, text=todo_text)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
