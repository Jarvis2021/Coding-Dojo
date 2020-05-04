from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Rendering Template

def logandreg(request):

    return render(request, 'index.html')


def register(request):

    print(request.POST)
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')

        new_user = User.objects.create(first_name=request.POST['fname'], last_name= request.POST['lname'],
        email = request.POST['email'], password=request.POST['pwd'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id

        return redirect('/success')

def login(request):


    logged_user = User.objects.filter(email=request.POST['email'])


    context = {

        "loginstatus" : "User is not registered yet!! or Email and Password do not match!!"
        }

    if len(logged_user) > 0:
        logged_user = logged_user[0]

        if logged_user.password == request.POST['pwd']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            request.session['lname'] = logged_user.last_name
            request.session['email'] = logged_user.email

            return redirect('/quotes')

    return render(request,'index.html',context)


def quotes(request):

    if 'user' not in request.session:

        return redirect('/')

    context = {

        'author_quotes': Wall_Quote.objects.all()
    }

    return render(request, 'quotes.html', context)




def process_quote(request):

    errors = Wall_Quote.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
            return redirect('/quotes')
    else:
        Wall_Quote.objects.create(author = request.POST['authorname'], message=request.POST['userquote'], poster=User.objects.get(id=request.session['id']))
        return redirect('/quotes')


def profile(request,id):
    context={
        'user' : User.objects.get(id=id)
        }

    return render(request,'profile.html', context)

def add_like(request,id):

    liked_quote = Wall_Quote.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_quote.user_likes.add(user_liking)

    return redirect('/quotes')

def updateaccount(request,id):

    if 'user' not in request.session:

        return redirect('/')



    print("user reached edit page")

    return render (request,'editaccount.html')


def logout(request):
    print("user clicked on Logout")
    print(request.session)
    request.session.flush()
    print(request.session)

    return redirect('/')
