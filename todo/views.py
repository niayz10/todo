from webbrowser import get
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import ToDo, Item
from .forms import ToDoTitleForm, ItemForm
# Create your views here.


def create_todo(request):
    if request.method == 'POST':
        form = ToDoTitleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            todo = ToDo.objects.create(title=title)
            messages.success(request, "Todo has been created successfully")
            return redirect('list_todos')
    form = ToDoTitleForm()
    return render(request, 'todo/create_todo.html', {'form': form})


def list_todos(request):
    todos = ToDo.objects.all()
    return render(request, "todo/list_todos.html", {"todos": todos, "show_create_todo": True})


def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    
    return render(request, 'todo/delete-todo.html', {'todo':todo, 'pk':pk})


def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'todo/todo-detail.html', {'todo': todo})


def items_list(request, pk):
    items = Item.objects.filter(todo__id=pk)
    return render(request, 'todo/items-list.html', {'items': items, 'show_create_item': True, 'todo_id': pk})


def create_items_of_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            new_item = item_form.save(commit=False)
            new_item.todo = todo
            new_item.save()
            return redirect('items-list', pk=pk)
    else:
        item_form = ItemForm()
    return render(request, 'todo/create_items_of_todo.html', {'form': item_form})
