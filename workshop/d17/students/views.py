from django.shortcuts import render, redirect
from .models import Student

def index(request):
    # All Post
    students = Student.objects.all() # => [< >, < >, < >]
    
    return render(request, 'index.html', {'students' : students})

def new(request):
    return render(request, 'new.html')

def create(request):
    # request.GET / request.POST
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday= request.POST.get('birthday')
    age = request.POST.get('age')
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save()
    return render(request, 'create.html', {'pk':student.pk})
    
def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student' : student} )
    
def delete(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/students/')
    
def edit(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':student})
    
def update(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.title = request.POST.get('title')
    student.content = request.POST.get('content')
    student.save()
    return redirect(f'/students/{student_id}/')
    