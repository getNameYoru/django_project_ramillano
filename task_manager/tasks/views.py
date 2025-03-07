from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')

        if title and due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                return HttpResponse("Invalid date format", status=400)

            Task.objects.create(title=title, description=description, due_date=due_date)
            return redirect('task_list')

    return render(request, 'tasks/task_form.html')

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')

        if task.title and due_date:
            try:
                task.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                return HttpResponse("Invalid date format", status=400)

            task.save()
            return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
