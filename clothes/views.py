from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort
from clothes.serializers import OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer
from rest_framework.decorators import api_view

import bcrypt
import random
import jwt
#from restApi.my_set import SECRET_KEY, ALGORITHM

from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
# Create your views here.
