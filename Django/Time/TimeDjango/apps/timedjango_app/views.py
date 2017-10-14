from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime



# Create your views here.

def index(request):
    
    # date = datetime.now().date().strftime('%B %-d, %Y')
    # time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        "datetime": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p",gmtime())

    }
    return render(request, 'index.html', context)

