from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


from restApi.models import Account, EmailCheck, Token
from restApi.serializers import AccountSerializer, EmailcheckSerializer, TokenSerializer, LoginSerializer
from rest_framework.decorators import api_view

import bcrypt
import random
import jwt
from .my_set import SECRET_KEY, ALGORITHM

from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone

# 'safe=False' for objects serialization in JsonResponse option
@api_view(['POST'])
def account_register(request):
    account_data = JSONParser().parse(request)  
    account_check = AccountSerializer(data=account_data)
    if account_check.is_valid():
        salt = bcrypt.gensalt()
        bytes_pw = account_data['pw'].encode('utf-8')
        hashed_pw = bcrypt.hashpw(bytes_pw, salt)
        stri_hashed_pw = hashed_pw.decode('utf-8')
        account_data['pw'] = stri_hashed_pw
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse({'status': 'true'}, status=status.HTTP_201_CREATED)
    return JsonResponse({'status': 'false', 'message': account_check.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def account_withdrawal(request):
    account_data = JSONParser().parse(request)
    comment = {}
    if "email" not in account_data:
        comment['email'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    try:
        account = Account.objects.get(email=account_data['email'])
    except Account.DoesNotExist:
        comment['email'] = ["account with this email does not exists."]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    account.delete()
    return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def account_changepw(request):
    account_data = JSONParser().parse(request) 
    comment = {}
    if "email" not in account_data and "newpw" not in account_data:
        comment['email'] = ["This field is required."]
        comment['newpw'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    if "email" not in account_data:
        comment['email'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    elif "newpw" not in account_data:
        comment['newpw'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            account = Account.objects.get(email=account_data['email'])
        except Account.DoesNotExist:
            comment['email'] = ["account with this email does not exists."]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
        salt = bcrypt.gensalt()
        bytes_pw = account_data['newpw'].encode('utf-8')
        hashed_pw = bcrypt.hashpw(bytes_pw, salt)
        stri_hashed_pw = hashed_pw.decode('utf-8')
        account.pw = stri_hashed_pw
        account.save(update_fields=['pw'])
        return JsonResponse({'status': 'true'})
@api_view(['POST'])
def account_login(request):
    account_data = JSONParser().parse(request)
    comment = {}
    if "email" not in account_data and "pw" not in account_data:
        comment['email'] = ["This field is required."]
        comment['pw'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    if "email" not in account_data:
        comment['email'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    elif "pw" not in account_data:
        comment['pw'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    else:     
        token_info = {}
        try:
            account = Account.objects.get(email=account_data['email'])
        except Account.DoesNotExist:
            comment['email'] = ["email incorrect"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
        bytes_input_pw = account_data['pw'].encode('utf-8')
        bytes_db_pw = account.pw.encode('utf=8')
        if bcrypt.checkpw(bytes_input_pw, bytes_db_pw) == True:
            key = str(random.randrange(1001, 10001))
            data = { 'email': account_data['email'], 'key': key}
            token = jwt.encode(data, SECRET_KEY, ALGORITHM)
            token_str = token.decode('utf-8')
            token_info['email'] = account_data['email']
            token_info['token'] = token_str
            try:
                token_current = Token.objects.get(email=account_data['email'])
            except Token.DoesNotExist:
                token_serializer = TokenSerializer(data=token_info)
                if token_serializer.is_valid():
                    token_serializer.save()
                    return JsonResponse({'status': 'true', 'token': token_str})
                else:
                    return JsonResponse(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            token_current.token = token_str
            token_current.save(update_fields=['token'])
            return JsonResponse({'status': 'true', 'token': token_str})
        else:
            comment['pw'] = ["password incorrect"]
            return JsonResponse({'status': 'false', 'message': comment})

@api_view(['DELETE'])
def account_logout(request):
    token_data = JSONParser().parse(request)
    comment = {}
    if "email" not in token_data:
        comment['email'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    try:
        account = Account.objects.get(email=token_data['email'])
    except Account.DoesNotExist:
        comment['email'] = ["account with this email does not exists."]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    token = Token.objects.get(email=token_data['email'])
    token.delete()
    return JsonResponse({'status': 'true'})

@api_view(['POST']) # 코드 전송후, 코드 db에 email과 함께 저장 
def account_codesend(request):
    email_data = JSONParser().parse(request)
    comment = {}
    comment['email'] = ["This field is required."]
    if not email_data:
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    comment = {}
    comment['email'] = ["account with this email already exists."]
    try:
        account = Account.objects.get(email=email_data['email'])
    except Account.DoesNotExist:
        comment['email'] = ["account with this email does not exists."]
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
            return JsonResponse({'status':'true', 'message': comment}, status=status.HTTP_201_CREATED)
        return JsonResponse({'status':'false', 'message': emailcheck_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    email_current.code = key
    email_current.save(update_fields=['code'])
    return JsonResponse({'status':'true', 'message': comment})

@api_view(['POST'])
def account_codeconfig(request):
    emailcode_data = JSONParser().parse(request)
    comment = {}
    if "email" not in emailcode_data and "code" not in emailcode_data:
        comment['email'] = ["This field is required."]
        comment['code'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    if "email" not in emailcode_data:
        comment['email'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    elif "code" not in emailcode_data:
        comment['code'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            emailcode_db = EmailCheck.objects.get(email=emailcode_data['email'])
        except EmailCheck.DoesNotExist:
            comment['email'] = ["email incorrect"]
            return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
        if emailcode_db.code == emailcode_data['code']:
            return JsonResponse({'status':'true'})
        else:
            comment['code'] = ["code incorrect"]
            return JsonResponse({'status':'false', 'message': comment})

