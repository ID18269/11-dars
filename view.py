from django.shortcuts import render, redirect
from .models import *


def lessons(request):
    if "search" in request.GET:
        lessons = LessonsModel.objects.filter(title__icontains = request.GET['search'])
    else:
        lessons = LessonsModel.objects.all().order_by('-id')
    return render(request, 'lessons.html', {"lessons": lessons})


def add_lesson(request):
    if request.method == "POST":
        title = request.POST.get('title')  # 'name' bo'lgan maydon nomini o'zgartiring
        img = request.FILES.get('image')

        lesson = LessonsModel(title=title, img=img)
        lesson.save()
        return redirect('/themes')
    else:
        return render(request, 'add_form.html')

def delete_lesson(request, id):
    LessonsModel.objects.filter(pk=id).delete()
    return redirect('/themes')

def edit_lesson(request, id):
    lesson = LessonsModel.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        img = request.FILES.get('image')

        lesson.title = title
        lesson.img = img
        lesson.save()
        return redirect('/themes')
    else:
        return render(request, 'edit_lesson.html', {'lesson': lesson})
