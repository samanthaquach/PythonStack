from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'survey_app/index.html')

def process(request):
    if request.session.has_key('counter') == True:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    request.session['counter']

    context = {
        'counter': request.session['counter']
    }

    return render (request, 'survey_app/result.html', context)

    

