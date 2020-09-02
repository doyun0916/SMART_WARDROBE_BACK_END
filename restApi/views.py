from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


from restApi.models import Account, EmailCheck
from restApi.serializers import AccountSerializer, EmailcheckSerializer
from rest_framework.decorators import api_view

import bcrypt
import random
import jwt
from .my_set import SECRET_KEY, ALGORITHM

from django.core.mail import EmailMessage
from django.conf import settings

# 'safe=False' for objects serialization in JsonResponse option
@api_view(['POST'])
def account_register(request):
    account_data = JSONParser().parse(request)  
    salt = bcrypt.gensalt()
    bytes_pw = account_data['pw'].encode('utf-8')
    hashed_pw = bcrypt.hashpw(bytes_pw, salt)
    stri_hashed_pw = hashed_pw.decode('utf-8')
    account_data['pw'] = stri_hashed_pw
    account_serializer = AccountSerializer(data=account_data)
    if account_serializer.is_valid():
        account_serializer.save()
        return JsonResponse({'message':'Account created successfully'}, status=status.HTTP_201_CREATED)
    return JsonResponse(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def account_withdrawal(request):
    account_data = JSONParser().parse(request)
    account = Account.objects.get(email=account_data['email'])
    account.delete()
    return JsonResponse({'message': 'Account was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def account_login(request):
    account_data = JSONParser().parse(request)
    try:
        account = Account.objects.get(email=account_data['email'])
    except Account.DoesNotExist:
        return JsonResponse({'message':'email is not present'}, status=status.HTTP_400_BAD_REQUEST)
    bytes_input_pw = account_data['pw'].encode('utf-8')
    bytes_db_pw = account.pw.encode('utf=8')
    if bcrypt.checkpw(bytes_input_pw, bytes_db_pw) == True:
        data = { 'email': account_data['email']}
        token = jwt.encode(data, SECRET_KEY, ALGORITHM)
        token_str = token.decode('utf-8')
        account.token = token_str
        account.save(update_fields=['token'])
        return JsonResponse({'token': token_str})
    else:
        return JsonResponse({'message':'password incorrect'})

@api_view(['GET'])
def account_emailcheck(request):
    email_data = JSONParser().parse(request)
    try: 
        Account.objects.get(email=email_data['email'])
    except Account.DoesNotExist:
        return JsonResponse({'message':'unique'}, status=status.HTTP_201_CREATED)
    return JsonResponse({'message':'dup'}, status=status.HTTP_201_CREATED)

@api_view(['POST']) # 코드 전송후, 코드 db에 email과 함께 저장 
def account_codesend(request):
    email_data = JSONParser().parse(request)
    key = str(random.randrange(1001, 10001))
    email = EmailMessage(
            'This is the varification Message:',
            key,
            settings.EMAIL_HOST_USER,
            [email_data['email']],
            )
    email.fail_silently=False
    email.send()
    email_data['code'] = key
    try:
        email_current = EmailCheck.objects.get(email=email_data['email'])
    except EmailCheck.DoesNotExist:
        emailcheck_serializer = EmailcheckSerializer(data=email_data)
        if emailcheck_serializer.is_valid():
            emailcheck_serializer.save()
            return JsonResponse({'message':'SUCCESSFUL!!!'}, status=status.HTTP_201_CREATED)
        return JsonResponse(emailcheck_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    email_current.code = key
    email_current.save(update_fields=['code'])
    return JsonResponse({'message':'successfil!'})

@api_view(['GET'])
def account_codeconfig(request):
    emailcode_data = JSONParser().parse(request)
    try:
        emailcode_db = EmailCheck.objects.get(email=emailcode_data['email'])
    except EmailCheck.DoesNotExist:
            return JsonResponse({'message':'email is not present'}, status=status.HTTP_400_BAD_REQUEST)
    if emailcode_db.code == emailcode_data['code']:
        return JsonResponse({'message':'match'})
    else:
        return JsonResponse({'message':'dismatch'})

