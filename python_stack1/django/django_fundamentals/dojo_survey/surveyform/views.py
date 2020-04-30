from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')


def process(request):
    if request.method == 'POST':
        request.session['user_name'] = request.POST['name']
        request.session['user_location'] = request.POST['location']
        request.session['user_language'] = request.POST['language']
        request.session['user_comment'] = request.POST['message']

    return redirect('/submission')

def submission(request):
    print("reached results method")
    return render(request, 'result.html')
