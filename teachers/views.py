from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        subject = request.POST['subject']
        Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
        return redirect('teachers:teacher_list')
    return render(request, 'teachers/teacher_form.html')

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:teacher_list')
