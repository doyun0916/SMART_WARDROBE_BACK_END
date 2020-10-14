from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress
from clothes.serializers import OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer, DressSerializer
from restApi.models import Token
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.utils import timezone


othick = ['coat', 'coat fur', 'parka']
tlong = ['long blouse', 'long shirt', 'long tee', 'hoodie', 'sweater', 'turtleneck', 'long dress']
bshort = ['short skirt', 'romper', 'denim shorts', 'shorts']

@api_view(['POST'])
def item_insert(request):
    item_info = JSONParser().parse(request)
    comment = {}
    if "token" not in item_info:
        comment['token'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['token'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    item_info['email'] = item_info.pop('token')
    item_info['email'] = session.email
    check = OuterThickSerializer(data=item_info)
    if check.is_valid():
        if item_info['category'] == 'outer':
            if item_info['subcategory'] in othick:
                othick_serializer = OuterThickSerializer(data=item_info)
                if othick_serializer.is_valid():
                    othick_serializer.save()
                    return JsonResponse({'status': 'true'})
                else:
                    return JsonResponse({'status': 'false', 'message': othick_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                othin_serializer = OuterThinSerializer(data=item_info)
                if othin_serializer.is_valid():
                    othin_serializer.save()
                    return JsonResponse({'status': 'true'})
                else:
                    return JsonResponse({'status': 'false', 'message': othin_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        
        if item_info['category'] == 'top':
            if item_info['subcategory'] in tlong:
                tlong_serializer = TopLongSerializer(data=item_info)
                if tlong_serializer.is_valid():
                    tlong_serializer.save()
                    return JsonResponse({'status': 'true'})
                else:
                    return JsonResponse({'status': 'false', 'message': tlong_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                tshort_serializer = TopShortSerializer(data=item_info)
                if tshort_serializer.is_valid():
                    tshort_serializer.save()
                    return JsonResponse({'status': 'true'})
                else:
                    return JsonResponse({'status': 'false', 'message': tshort_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
        if item_info['category'] == 'bottom':
            if item_info['subcategory'] in bshort:
                bshort_serializer = BottomShortSerializer(data=item_info)
                if bshort_serializer.is_valid():
                    bshort_serializer.save()
                    return JsonResponse({'status': 'true'})
                else:
                    return JsonResponse({'status': 'false', 'message': bshort_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                blong_serializer = BottomLongSerializer(data=item_info)
                if blong_serializer.is_valid():
                    blong_serializer.save()
                    return JsonResponse({'status': 'true'})
                else:
                    return JsonResponse({'status': 'false', 'message': blong_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'status': 'false', 'message': check.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])             # request = token, -------------> response = user's top, bottom, short seperation
def item_get(request):
    item_info = JSONParser().parse(request)
    result = {}
    outer = {}
    top = {}
    bottom = {}
    dress = {}
    comment = {}
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
        comment['token'] = ["user not present"]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        outerthickdb = OuterThick.objects.filter(email=session.email)
        othick = OuterThickSerializer(outerthickdb, many=True)
        othick.data[0].pop('email')
        outer['outerthick'] = othick.data
    except OuterThick.DoesNotExist:
        outer['outerthick'] = {}
    
    try:
        outerthindb = OuterThin.objects.filter(email=session.email)
        othin = OuterThinSerializer(outerthindb, many=True)
        othin.data[0].pop('email')
        outer['outerthin'] = othin.data
    except OuterThin.DoesNotExist:
        outer['outerthin'] = {} 
    result['outer'] = outer
    
    try:
        toplongdb = TopLong.objects.filter(email=session.email)
        tlong = TopLongSerializer(toplongdb, many=True)
        tlong.data[0].pop('email')
        top['toplong'] = tlong.data
    except TopLong.DoesNotExist:
        top['toplong'] = {}
    
    try:
        topshortdb = TopShort.objects.filter(email=session.email)
        tshort = TopShortSerializer(topshortdb, many=True)
        tshort.data[0].pop('email')
        top['topshort'] = tshort.data
    except TopShort.DoesNotExist:
        top['topshort'] = {}
    result['top'] = top
    
    try:
        bottomlongdb = BottomLong.objects.filter(email=session.email)
        blong = BottomLongSerializer(bottomlongdb, many=True)
        blong.data[0].pop('email')
        bottom['bottomlong'] = blong.data
    except BottomLong.DoesNotExist:
        bottom['bottomlong'] = {}
    
    try:
        bottomshortdb = BottomShort.objects.filter(email=session.email)
        bshort = BottomShortSerializer(bottomshortdb, many=True)
        bshort.data[0].pop('email')
        bottom['bottomshort'] = bshort.data
    except BottomShort.DoesNotExist:
        bottom['bottomshort'] = {} 
    result['bottom'] = bottom
    
    try:
        dressdb = Dress.objects.filter(email=session.email)
        dre = DressSerializer(dressdb, many=True) 
        dre.data[0].pop('email')
        dress['dress'] = dre.data
    except Dress.DoesNotExist:
        dress['dress'] = {}
    result['dress'] = dress
    return JsonResponse({'status':'true', 'items': result}, safe=False)



@api_view(['POST'])
def item_update(request):
    item_info = JSONParser().parse(request)
    comment = {}
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['token'] = ["user not present"]
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
    comment = {}
    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['token'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    try:
        items = item_info['category'].objects.filter(id=item_info['num'], email=session.email)
    except item_info['category'].DoesNotExist:
        comment['email'] = ["account with this email does not exists."]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    items.delete()
    return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)


