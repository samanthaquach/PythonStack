from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
    def login_validator(self,postData):
        errors = []
        if len(self.filter(email=postData['email'])) > 0:
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                 errors.append ("Invalid password")
        else: 
            errors.append ("No such user")

        if errors:
            return errors

        return user

    def register_valid(self, postData):
        errors = []
        # -----------------------------------
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors.append("name fields must be at least 3 characters")
        #  -----------------------------------
        if len(postData['password']) < 4:
            errors.append("password must be at least 4 characters")
        #  -----------------------------------           
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append('name fields must be letter characters only')
        #  -----------------------------------
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("invalid email")
        #  -----------------------------------
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("email already in use")
        #  -----------------------------------
        if postData['password'] != postData['confirm_password']:
            errors.append("passwords do not match")

        if not errors:
            # hash password
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=hashed,
                bday=postData['bday']
            )
            return new_user

        objects = UserManager()
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bday = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {} {}>".format(self.id, self.email, self.password, self.created_at, self.updated_at)