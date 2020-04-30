from django.shortcuts import render, HttpResponse, redirect





# Create your views here.

def index(request):

    return render(request, 'index.html')

def process(request):
    print("The user submitted a form!")
    print(request.POST)
    print(request.POST['email'])
    print(request.POST['password'])
    request.session['user_details'] = f"User email : {request.POST['email']},  User password: {request.POST['password']}"
    return redirect ('/')
