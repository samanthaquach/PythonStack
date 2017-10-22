from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.db import models
import re
import bcrypt
from ..loginregis_app.models import User, UserManager

# Create your models here.
class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = []
        # -----------------------------------
        if len(postData['title']) < 0:
            errors.append("No title can be empty!")
        if len(postData['review']) < 0:
            errors.append("No review can be empty!")
        #  -----------------------------------           
        # if not int(postData['rating']) > 0 or not int(postData['rating']) <= 5:
        #     errors.append("invalid rating")
        return errors

    def create(self, user_id):
        # retreive or create author
        the_author = None
        if len(postData['new_author']) < 1:
            the_author = Author.objects.get(id=int(postData['author']))
        else:
            the_author = Author.objects.create(name=postData['new_author'])
        # retreive or create book
        the_book = None
        if not Book.objects.filter(title=postData['title']):
            the_book = Book.objects.create(title=postData['title'], author=the_author)
        else:
            the_book = Book.objects.get(title=postData['title'])
        # returns a Review object
        return self.create(
            review = postData['review'],
            rating = postData['rating'],
            book = the_book,
            reviewer = User.objects.get(id=user_id))
        
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "<Author object: {}>".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")
    def __str__(self):
        return "<Book object: {}>".format(self.title)
        
class Review(models.Model):
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    book = models.ForeignKey(Book, related_name="reviews")
    reviewer = models.ForeignKey(User, related_name="reviews_left")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()
    def __str__(self):
        return "<Review object: {}>".format(self.book.title)