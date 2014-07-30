from django.shortcuts import render, render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from StudentsListing.models import Group, Student
from StudentsDatabase.utils import render_to

from StudentsListing.forms import GroupForm, StudentForm, Confirm
# Create your views here.

@render_to("StudentsListing/index.html")
def index(request):
    groups = Group.objects.all()
    return {"groups": groups}


@render_to("StudentsListing/list_students.html")
def list_students(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students_list = group.student_set.all()

    return {'students': students_list,
            'group': group
    }

@login_required(login_url='/login/')
@render_to("StudentsListing/manage_students.html")
def student_manager(request, student_id=None):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        student = None

    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('index')

    return {'form': form,
            'student': student
    }

@login_required(login_url='/login/')
@render_to("StudentsListing/manage_groups.html")
def group_manager(request, group_id=None):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        group = None

    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('index')

    return {'form': form,
            'group': group
    }

@render_to("StudentsListing/delete.html")
@login_required(login_url='/login/')
def delete_student(request, student_id=None):
    obj = get_object_or_404(Student, pk=student_id)

    form = Confirm(request.POST or None)
    if form.is_valid():
        choice = form.cleaned_data.get('choice')
        if choice:
            obj.delete()
        return redirect('index')

    return {'form': form, 'target': obj}

@render_to("StudentsListing/delete.html")
@login_required(login_url='/login/')
def delete_group(request, group_id=None):
    obj = get_object_or_404(Group, pk=group_id)

    form = Confirm(request.POST or None)
    if form.is_valid():
        choice = form.cleaned_data.get('choice')
        if choice:
            obj.delete()
        return redirect('index')

    return {'form': form, 'target': obj}