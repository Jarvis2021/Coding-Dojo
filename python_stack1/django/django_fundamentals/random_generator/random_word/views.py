from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.



def random_word(request):
    count = request.session.get('attempts',0)
    request.session['attempts'] = count
    if request.method == 'GET':
        request.session['newword'] = get_random_string(length=14)
        request.session['attempts'] = count + 1
    return render(request,'wordgenerator.html')


def reset_attempt(request):
    request.session.flush()

    return redirect('/random_word')
