from django.shortcuts import render, redirect
from .models import Student

def index(request):
    # All Post 모든 학생들의 정보를 다 가져와서! 리스트 형태의 자료형으로 가져온다!
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
    
    s = Student(name=name, email=email, birthday=birthday, age=age)
    s.save()
    return render(request, 'create.html', {'pk':s.pk})
    
def detail(request, student_id):
    s = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student' : s} )
    
def delete(request, student_id):
    s = Student.objects.get(pk=student_id)
    s.delete()
    return redirect('/students/')
    
def edit(request, student_id):
    s = Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':s})
    
def update(request, student_id):
    s = Student.objects.get(pk=student_id)
    s.name = request.POST.get('name')
    s.email = request.POST.get('email')
    s.birthday = request.POST.get('birthday')
    s.age = request.POST.get('age')
    s.save()
    return redirect(f'/students/{s.pk}/')
    