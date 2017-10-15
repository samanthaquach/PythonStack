from django.shortcuts import render, HttpResponse, redirect
import string
import random

# Create your views here.
def index(request):
    random_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    
    if request.session.has_key('counter') == False:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 0

    context = {
        'string': random_str,
        'counter': request.session['counter'],
    
    }

    return render(request, 'index.html', context)

def generate(request):
    request.session['counter'] += 1

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session['counter']

    # request.session.modified = True
    # try:
    #     del request.session['counter']
    # except KeyError:
    #     pass
    
    return redirect('/')

    