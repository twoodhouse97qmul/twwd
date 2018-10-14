from django import forms
from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    message = models.CharField(max_length=900, blank=True)
