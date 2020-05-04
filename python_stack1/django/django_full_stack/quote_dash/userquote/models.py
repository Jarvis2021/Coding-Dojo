from django.db import models
import re

# Create your models here.


class UserManager(models.Manager):

    def basic_validator(self, postdata):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postdata['fname']) < 2 or len(postdata['lname']) < 2 :
            errors['name'] = "First Name or Last Name should be atleast 2 characters"

        if len(postdata['pwd']) < 8:
            errors['pwd'] = "Password should be atleast 8 characters"

        if postdata['pwd'] != postdata['confpwd']:
            errors['pdm'] = "Password and Confirm Password do not match"

        if not email_check.match(postdata['email']):
            errors['email'] = "Invalid email address!"

        return errors


class QuoteManager(models.Manager):

    def basic_validator(self, postdata):
        errors = {}

        if len(postdata['authorname']) < 3 :
            errors['authorname'] = "Author should be atleast 3 characters"

        if len(postdata['userquote']) < 10 :
            errors['authorquote'] = "User Quote should be atleast 10 characters"

        return errors



class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



class Wall_Quote(models.Model):

    message = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    poster = models.ForeignKey(User,related_name='usermessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    objects = QuoteManager()


class Edit_Manager(models.Model):

    def basic_validator(self, postdata):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postdata['fname']) < 2 or len(postdata['lname']) < 2 :
            errors['name'] = "First Name or Last Name should be atleast 2 characters"

        if len(postdata['pwd']) < 8:
            errors['pwd'] = "Password should be atleast 8 characters"

        if postdata['pwd'] != postdata['confpwd']:
            errors['pdm'] = "Password and Confirm Password do not match"

        if not email_check.match(postdata['email']):
            errors['email'] = "Invalid email address!"

        return errors
