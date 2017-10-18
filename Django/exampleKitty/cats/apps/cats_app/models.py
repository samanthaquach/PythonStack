from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cats(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(Author, related_name="books")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# class Cat(models.model):
#     name = models.Charfield(maxlength = 255)
#     age = models.IntegerField()
#     image_link = models.charfield(max_length = 255)

    #here would define your model