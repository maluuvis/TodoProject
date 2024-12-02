from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.
def index(request): #função cujo parâmetro é um requerimento
    var_task = Task.objects.all()#váriavel que armazena todos os objtos "tasks"
    count_todos = var_task.count()#conta os todos
    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    uncompleted_todo = count_todos - count_completed_todo

    if request.method=='POST': 
        form = TaskForm(request.POST)
        if form.is_valid(): #se o forms tiver te 100 carac. 
            form.save() #salvar
            return redirect('/') #retornar para a página inicial
    else:
        form = TaskForm(request.POST)

    context = {
        'todas_tasks': var_task,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'uncompleted_todo': uncompleted_todo,
    }
        
    return render(request, 'partials/todo/index.html', context )
    #retornará um arquivo .html e a váriavel que guarda as tasks

def update(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method=='POST':
        form = UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UpdateTaskForm(instance=todo)
    context = {
        'form' : form
    }

    return render(request, 'partials/todo/update.html', context)


def view_boatarde(request):
    
    return render(request, 'partials/todo/boa-tarde.html', )

def delete(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    return render(request, 'partials/todo/delete.html')