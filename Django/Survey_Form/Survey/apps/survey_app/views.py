from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'index.html')

def process(request):
    request.session['name'] = request.form['name']
    request.session['location'] = request.form['location']
    request.session['language'] = request.form['language']
    request.session['comment'] = request.form['comment']

    return redirect('/result')

def result(request):
    request.session['counter'] += 1

    context = {
        'counter': request.session['counter'],
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }

    return render (request, 'result.html', context)

