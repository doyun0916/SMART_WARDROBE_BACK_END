from django.db import models
from django.utils import timezone

class Account(models.Model):
    email = models.EmailField(max_length=70, primary_key=True)
    pw = models.CharField(max_length=70)
    nickname = models.CharField(max_length=70)
    token = models.CharField(default='', max_length=150)
    createdAt = models.DateTimeField(default=timezone.now)

class EmailCheck(models.Model):
    email = models.EmailField(max_length=70, primary_key=True)
    code = models.IntegerField()

# Create your models here.
