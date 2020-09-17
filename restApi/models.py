from django.db import models
from django.utils import timezone

class Account(models.Model):
    email = models.EmailField(max_length=70, primary_key=True)
    pw = models.CharField(max_length=70)
    nickname = models.CharField(max_length=70),
    sex = models.CharField(max_length=10),
    createdAt = models.DateTimeField(default=timezone.now)

class EmailCheck(models.Model):
    email = models.EmailField(max_length=70, primary_key=True)
    code = models.IntegerField()

class Token(models.Model):
    email = models.EmailField(max_length=70, primary_key=True)
    token = models.CharField(max_length=150)

# Create your models here.
