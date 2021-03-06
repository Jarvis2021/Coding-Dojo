from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Message(models.Model):
    message = models.CharField(max_length=100)
    poster = models.ForeignKey(User, related_name='all_messages', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
