from django.shortcuts import render

from .models import Mancasual, Mancampus, Manminimal, Manstreet, Mantravel, Mansports, Manformal, Mandandy, Wosports, Wocasual, Woformal, Woromantic, Wogirlish, Wostreet, Wofeminine, Wotravel
from .serializers import CoordiSerializer
from django.utils import timezone

def insert(x):
    insert_check = AccountSerializer(data=x)
    if insert_check.is_valid():
        insert_check.save()

test = { "url": "asdas", "outer": "asdasas"}

insert(test)
