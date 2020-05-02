from django.shortcuts import render, redirect
from random import randrange
from datetime import datetime
from time import strftime, gmtime


# Create your views here.


def index(request):

    if 'gold' not in request.session:

        request.session['gold'] = 0

    if 'activity_log' not in request.session:

        request.session['activity_log'] = []

    return render(request,'index.html')


def process_money(request):

    if request.GET.get('building')=="farm":
        gold = randrange(10,20)

    elif request.GET.get('building')=="cave":
        gold = randrange(5,10)

    elif request.GET.get('building')=="house":
        gold = randrange(2,5)

    elif request.GET.get('building')=="casino":
        gold = randrange(-50,50)

    else:

        print("There is no request submitted")

    request.session['gold'] = request.session['gold'] + gold

    if gold < 0:

        user_dict = {}
        user_dict['color'] = "red"
        user_dict['useractivity'] = f"Entered a casino and lost {gold} golds...ouch. ({strftime('%Y-%m-%d %H:%M %p',gmtime())})"

        request.session['activity_log'].append(user_dict)



    if gold > 0:

        user_dict = {}
        user_dict['color'] = "green"
        user_dict['useractivity'] = f"Earned {gold} golds from casino! ({strftime('%Y-%m-%d %H:%M %p',gmtime())})"

        request.session['activity_log'].append(user_dict)


    return redirect('/')



def logout(request):

    print("User clicked on Reset")
    request.session.flush()

    return redirect('/')
