from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Classroom
from .forms import ClassroomForm

def list_classrooms(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classrooms/list.html', {'classrooms': classrooms})

def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom created successfully.')
            return redirect('list_classrooms')
    else:
        form = ClassroomForm()
    return render(request, 'classrooms/create.html', {'form': form})

def edit_classroom(request, id):
    classroom = get_object_or_404(Classroom, id=id)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom updated successfully.')
            return redirect('list_classrooms')
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'classrooms/edit.html', {'form': form, 'classroom': classroom})

def delete_classroom(request, id):
    classroom = get_object_or_404(Classroom, id=id)
    if request.method == 'POST':
        classroom.delete()
        messages.success(request, 'Classroom deleted successfully.')
        return redirect('list_classrooms')
    return render(request, 'classrooms/delete.html', {'classroom': classroom})