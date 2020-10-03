from django.db import models
from django.utils import timezone

class Style(models.Model):
    style = models.CharField(max_length=30)

class Coordi(models.Model):                 #place to preserve coordinates image
    # squence of coordi
    outerthick = models.CharField(max_length=10),
    outerthin = models.CharField(max_length=10),
    toplong = models.CharField(max_length=10)
    topshort = models.CharField(max_length=10),
    bottomlong = models.CharField(max_length=10),
    bottomshort = models.CharField(max_length=10)
