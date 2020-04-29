from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'loc' : request.POST['location'],
            'lang': request.POST['language'],
            'com' : request.POST['message']
        }
    return render(request, 'result.html', context)
