from __future__ import unicode_literals
from django.db import IntegrityError
from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return "<Users object: {} {} {}>".format(self.first_name, self.last_name, self.email)

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(Users, related_name="uploaded_books")
    liked_by = models.ManyToManyField(Users, related_name="liked_books")

    def __repr__(self):
        return "<Users object: {} {}>".format(self.name, self.desc)
    
    