from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from ..loginregis_app.models import User, UserManager
from models import Author, Book, ReviewManager, Review
from django.contrib import messages
from datetime import date
from django.urls import reverse

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'beltreview_app/index.html', context)

def clear(request):
#To Log Out
    del request.session['user_id']
    return redirect('/')

def AddBookPage(request):
#AddBook or Review Page 
    print ("YOU ARE ADDING A BOOK PAGE")
    print request.session['user_id']

    #check to see if user is signed in
    is_signed_in = request.session.get('is_signed_in', False)
    if (is_signed_in == True):
        print ("YOU MADE IT")
        return render(request, 'beltreview_app/AddBook.html')        
    else:
        return redirect(reverse('beltreview:index'))
    

def submitreview(request):
#creating a book or a review

    result = Review.objects.review_validator(request.POST)
    if type(result) == list:
        if len(result) > 0:
            messages.error(request, result)
            print result
            return redirect(reverse('beltreview:addbook'))
    else:
        user = Users.objects.get(id = request.session['user_id'])
        book = Books.objects.get(id = request.POST['idnum'])
        book.save()
        review = Reviews.objects.create(rating = request.POST['rating'], description = request.POST['description'], user = user, book = book)
        review.save()
    return redirect(reverse('beltreview:index'))

    # messages.success(request, "You successfully submitted!") 
    # return redirect(redirect(reverse('beltreview:index'))