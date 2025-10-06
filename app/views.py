from django.shortcuts import render, redirect
from .models import Task

from datetime import datetime

# Create your views here.


def all_tasks_view(request):

    return render(request=request, template_name='index.html', context={'tasks': Task.objects.all()})


def edit_task(request, id):

    return render(request=request, template_name='edit.html')

def edit_task_feature(request, id, num):

    return render(request=request, template_name='edit_feature.html', context={'task':Task.objects.get(id = id), 'num':num, 'id':id})

def edit_feature_full(request, id, num):

    task = Task.objects.get(id=id)

    if request.POST:

        if int(num)==1:
            title = request.POST.get('title')
            task.title = title

        if int(num) == 2:
            desc = request.POST.get('desc')
            task.desc = desc

        if int(num) == 3:
            deadline = request.POST.get('deadline')

            deadline = datetime.strptime(deadline, "%Y-%m-%d")

            task.deadline = deadline


        if int(num) == 4:
            is_complete = request.POST.get('is_complete')
            task.is_complete = is_complete


    task.save()

    return  redirect('/')


def delete_task(request, id):

    Task.objects.get(id = id).delete()

    return redirect('/')


def view_task(request, id):

    pass

def new_task(request):

    if request.POST:

        title = request.POST.get('title')

        desc = request.POST.get('desc')

        deadline = request.POST.get('deadline')

        deadline = datetime.strptime(deadline, "%Y-%m-%d")

        is_complete = request.POST.get('is_complete')


        Task.objects.create(
            title=title,
            desc=desc,
            deadline=deadline,
            is_complete=is_complete
        )

    return  redirect('/')

def more(request, id):

    task = Task.objects.get(id = id)

    return render(request=request, template_name='more.html', context={'task':task})