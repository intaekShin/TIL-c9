from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info.html')
    
def detail(request, name):
    return render(request, 'detail.html', {'name': name})