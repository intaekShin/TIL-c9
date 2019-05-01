from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView, CreateView   # 상속받기.
from django.contrib.auth.mixins import LoginRequiredMixin


class PersonList(ListView):
    model = Person  # 모델에서 꺼내오는 데이터 Person
    context_object_name = 'person'  # html에 쓰일 변수 'person'
    # urls.py 도 수정해야함.


# def list(request):
#     person = Person.objects.all()
#     return render(request, 'person/person_list.html', {'person': person})


# def create(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person:list')
#     else:
#         form = PersonForm()
        
#     return render(request, 'person/person_form.html', {'form':form})

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/person/'