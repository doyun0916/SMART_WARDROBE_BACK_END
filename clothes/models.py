from django.db import models
from django.utils import timezone
from restApi.models import Account

class OuterThick(models.Model):
    name = models.IntegerField()
    color = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    descript = models.CharField(max_length=70)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class OuterThin(models.Model):
    name = models.IntegerField()
    color = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    descript = models.CharField(max_length=70)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class TopLong(models.Model):
    name = models.IntegerField()
    color = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    descript = models.CharField(max_length=70)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class TopShort(models.Model):
    name = models.IntegerField()
    color = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    descript = models.CharField(max_length=70)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class BottomLong(models.Model):
    name = models.IntegerField()
    color = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    descript = models.CharField(max_length=70)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class BottomShort(models.Model):
    name = models.IntegerField()
    color = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    url = models.CharField(max_length=70)
    descript = models.CharField(max_length=70)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

# Create your models here.

