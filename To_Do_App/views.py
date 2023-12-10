from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks


def home(request, pk=-1):
    pending_tasks = Tasks.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Tasks.objects.filter(is_completed=True).order_by('-created_at')

    context = {
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "editable_task": None,
    }

    if pk != -1:
        editable_task = get_object_or_404(Tasks, pk=pk)
        context["editable_task"] = editable_task
        editable_task.delete()

    return render(request, 'To_Do_App/indx.html', context)


def add(request):
    Tasks.objects.create(description=request.POST["task"])
    return redirect('home')


def action(request, action, id):
    task = get_object_or_404(Tasks, id=id)
    if action == 'complete':
        task.is_completed = True
        task.save()

    elif action == 'delete':
        task.delete()

    elif action == 'undone':
        task.is_completed = False
        task.save()

    elif action == 'edit':
        return redirect('editing_home', pk=id)

    return redirect('home')
