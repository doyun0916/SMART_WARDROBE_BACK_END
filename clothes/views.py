from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress
from clothes.serializers import OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer, DressSerializer
from restApi.models import Token
from rest_framework.decorators import api_view

from django.conf import settings
from django.utils import timezone


def insert(x):
    if x.is_valid():
        x.save()
        return JsonResponse({'status': 'true'})
    else:
        return JsonResponse({'status': 'false', 'message': x.errors}, status=status.HTTP_400_BAD_REQUEST)
 

othick = ['coat', 'coat_fur', 'parka']
tlong = ['long blouse', 'long shirt', 'long tee', 'hoodie', 'sweater', 'turtleneck', 'long dress']
bshort = ['short skirt', 'romper', 'denim shorts', 'shorts']

@api_view(['POST'])
def item_insert(request):
    item_info = JSONParser().parse(request)
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['session'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    item_info['email'] = item_info.pop('token')
    item_info['email'] = session.email
    if item_info['category'] == 'outer':
        if item_info['subcategory'] in othick:
            othick_serializer = OuterThickSerializer(data=item_info)
            insert(othick_serializer)
        else:
            othin_serializer = OuterThinSerializer(data=item_info)
            insert(othin_serializer)
    if item_info['category'] == 'top':
        if item_info['subcategory'] in tlong:
            tlong_serializer = TopLongSerializer(data=item_info)
            insert(tlong_serializer)
        else:
            tshort_serializer = TopShortSerializer(data=item_info)
            insert(tshort_serializer)
    if item_info['category'] == 'bottom':
        if item_info['subcategory'] in bshort:
            bshort_serializer = BottomShortSerializer(data=item_info)
            insert(bshort_serializer)
        else:
            blong_serializer = BottomLongSerializer(data=item_info)
            insert(blong_serializer)


@api_view(['POST'])             # request = token, -------------> response = user's top, bottom, short seperation
def item_get(request):
    item_info = JSONParser().parse(request)
    result = []
    outer = {}
    top = {}
    bottom = {}
    dress = {}
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['session'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    outer['outerthick'] = OuterThick.objects.get(email=session.email)
    outer['outerthin'] = OuterThin.objects.get(email=session.email)
    result.append(outer)
    top['toplong'] = TopLong.objects.get(email=session.email)
    top['topshort'] = Topshort.objects.get(email=session.email)
    result.append(top)
    bottom['bottomlong'] = BottomLong.objects.get(email=session.email)
    bottom['bottomshort'] = BottomShort.objects.get(email=session.email)
    result.append(bottom)
    dress['dress'] = Dress.objects.get(email=session.email)
    result.append(dress)
    return JsonResponse({'status':'true', 'items': result}, status=status.HTTP_202_SUCCESSFUL)
#            try:
#                token_current = Token.objects.get(email=account_data['email'])
#            except Token.DoesNotExist:
#                token_serializer = TokenSerializer(data=token_info)
#                if token_serializer.is_valid():
#                    token_serializer.save()
#                    return JsonResponse({'status': 'true', 'token': token_str})
#                else:
#                    return JsonResponse(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#            token_current.token = token_str
#            token_current.save(update_fields=['token'])
#            return JsonResponse({'status': 'true', 'token': token_str})
#        else:
#            comment['pw'] = ["password incorrect"]
#            return JsonResponse({'status': 'false', 'message': comment})




@api_view(['POST'])
def item_update(request):
    item_info = JSONParser().parse(request)
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['session'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    item_info['email'] = item_info.pop('token')
    item_info['email'] = session.email
    try:
        items = item_info['category'].objects.filter(id=item_info['num'], email=session.email)
    except item_info['category'].DoesNotExist:
        comment['email'] = ["account with this email does not exists."]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    #items.name = item_info['name']
    #items.brand = item_info['brand']
    #items.color = item_info['color']
    #items.descript = item_info['descript']
    if item_info['category'] == 'outer':
        if item_info['subcategory'] in othick:
            othick_serializer = OuterThickSerializer(data=item_info)
            insert(othick_serializer)
        else:
            othin_serializer = OuterThinSerializer(data=item_info)
            insert(othin_serializer)
    if item_info['category'] == 'top':
        if item_info['subcategory'] in tlong:
            tlong_serializer = TopLongSerializer(data=item_info)
            insert(tlong_serializer)
        else:
            tshort_serializer = TopShortSerializer(data=item_info)
            insert(tshort_serializer)
    if item_info['category'] == 'bottom':
        if item_info['subcategory'] in bshort:
            bshort_serializer = BottomShortSerializer(data=item_info)
            insert(bshort_serializer)
        else:
            blong_serializer = BottomLongSerializer(data=item_info)
            insert(blong_serializer)


@api_view(['DELETE'])          # num, category, token
def item_delete(request):
    item_info = JSONParser().parse(request)
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['session'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    try:
        items = item_info['category'].objects.filter(id=item_info['num'], email=session.email)
    except item_info['category'].DoesNotExist:
        comment['email'] = ["account with this email does not exists."]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    items.delete()
    return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)


