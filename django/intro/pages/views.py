from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
# Template Variable
def dinner(request):
    menu = ['족발', '집밥', '인크레더블버거', '치파오치킨']
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner' : pick})
    
# Variable routing 주소 자체를 변수로 사용하는
def hello(request, take1):
    return render(request, 'hello.html', {'name' : take1})
    
def lotto(request):
    number = range(1,46)
    bomb = range(6)
    o=[]
    for i in bomb:
        atari = random.choice(number)
        i = atari
        o.append(i)
    o.sort()
    return render(request, 'lotto.html', {'price' : o})
    
# Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message' : message})
    
# Form 외부로 요청
def naver(request):
    return render(request, 'naver.html')
    
# Bootstrap
def bootstrap(request):
    return render(request, 'bootstrap.html')