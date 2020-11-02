from django.db import models
from django.utils import timezone
from restApi.models import Account

class OuterThick(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70, null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class OuterThin(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70,  null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class TopLong(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70, null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class TopShort(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70, null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class BottomLong(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70, null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class BottomShort(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70, null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

class Dress(models.Model):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    subcategory = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    descript = models.CharField(max_length=70, null=True)
    brand = models.CharField(max_length=70, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

# Create your models here.

