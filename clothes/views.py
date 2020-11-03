from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress
from clothes.serializers import Item, OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer, DressSerializer
from restApi.models import Token, Account
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.utils import timezone


othick = ['coat', 'coat fur', 'parka']
tlong = ['long blouse', 'long shirt', 'long tee', 'hoodie', 'sweater', 'turtleneck']
bshort = ['short skirt', 'denim shorts', 'shorts']
delcheck = ['token', 'id', 'category', 'subcategory']
upcheck = ['token', 'id', 'name', 'brand', 'color', 'url', 'category', 'subcategory', 'categoryNew', 'subcategoryNew', 'descript']
insertcheck = ['name', 'color', 'subcategory', 'category', 'url' ]

@api_view(['POST'])
def item_insert(request):
    item_info = JSONParser().parse(request)
    comment = {}
    item = {}
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

    for i in range(len(insertcheck)):
        if insertcheck[i] not in item_info:
            comment[insertcheck[i]] = ["This field is required"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    check = OuterThickSerializer(data=item_info)
    if check.is_valid():
        if item_info['category'] == 'outer':
            if item_info['subcategory'] in othick:
                othick_serializer = OuterThickSerializer(data=item_info)
                if othick_serializer.is_valid():
                    othick_serializer.save()
                    item = OuterThick.objects.get(url=item_info['url'])
                    itemSe = Item(item)
                    return JsonResponse({'status': 'true', 'item': itemSe.data})
                else:
                    return JsonResponse({'status': 'false', 'message': othick_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                othin_serializer = OuterThinSerializer(data=item_info)
                if othin_serializer.is_valid():
                    othin_serializer.save()
                    item = OuterThin.objects.get(url=item_info['url'])
                    itemSe = Item(item)
                    return JsonResponse({'status': 'true', 'item': itemSe.data})
                else:
                    return JsonResponse({'status': 'false', 'message': othin_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        
        if item_info['category'] == 'top':
            if item_info['subcategory'] in tlong:
                tlong_serializer = TopLongSerializer(data=item_info)
                if tlong_serializer.is_valid():
                    tlong_serializer.save()
                    item = TopLong.objects.get(url=item_info['url'])
                    itemSe = Item(item)
                    return JsonResponse({'status': 'true', 'item': itemSe.data})
                else:
                    return JsonResponse({'status': 'false', 'message': tlong_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                tshort_serializer = TopShortSerializer(data=item_info)
                if tshort_serializer.is_valid():
                    tshort_serializer.save()
                    item = TopShort.objects.get(url=item_info['url'])
                    itemSe = Item(item)
                    return JsonResponse({'status': 'true', 'item': itemSe.data})
                else:
                    return JsonResponse({'status': 'false', 'message': tshort_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
        if item_info['category'] == 'bottom':
            if item_info['subcategory'] in bshort:
                bshort_serializer = BottomShortSerializer(data=item_info)
                if bshort_serializer.is_valid():
                    bshort_serializer.save()
                    item = BottomShort.objects.get(url=item_info['url'])
                    itemSe = Item(item)
                    return JsonResponse({'status': 'true', 'item': itemSe.data})
                else:
                    return JsonResponse({'status': 'false', 'message': bshort_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                blong_serializer = BottomLongSerializer(data=item_info)
                if blong_serializer.is_valid():
                    blong_serializer.save()
                    item = BottomLong.objects.get(url=item_info['url'])
                    itemSe = Item(item)
                    return JsonResponse({'status': 'true', 'item': itemSe.data})
                else:
                    return JsonResponse({'status': 'false', 'message': blong_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        if item_info['category'] == 'onepiece':
            dress_serializer = DressSerializer(data=item_info)
            if dress_serializer.is_valid():
                dress_serializer.save()
                item = Dress.objects.get(url=item_info['url'])
                itemSe = Item(item)
                return JsonResponse({'status': 'true', 'item': itemSe.data})
            else:
                return JsonResponse({'status': 'false', 'message': dress_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
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
    
    outerthickdb = OuterThick.objects.filter(email=session.email)
    othick = OuterThickSerializer(outerthickdb, many=True)
    if not bool(othick.data):
        outer['outerthick'] = {}
    else:
        othick.data[0].pop('email')
        outer['outerthick'] = othick.data
    
    outerthindb = OuterThin.objects.filter(email=session.email)
    othin = OuterThinSerializer(outerthindb, many=True)
    if not bool(othin.data):
        outer['outerthin'] = {}
    else:
        othin.data[0].pop('email')
        outer['outerthin'] = othin.data
    result['outer'] = outer
    



    toplongdb = TopLong.objects.filter(email=session.email)
    tlong = TopLongSerializer(toplongdb, many=True)
    if not bool(tlong.data):
        top['toplong'] = {}
    else:
        tlong.data[0].pop('email')
        top['toplong'] = tlong.data

    topshortdb = TopShort.objects.filter(email=session.email)
    tshort = TopShortSerializer(topshortdb, many=True)
    if not bool(tshort.data):
        top['topshort'] = {}
    else:
        tshort.data[0].pop('email')
        top['topshort'] = tshort.data
    result['top'] = top



    bottomlongdb = BottomLong.objects.filter(email=session.email)
    blong = BottomLongSerializer(bottomlongdb, many=True)
    if not bool(blong.data):
        bottom['bottomlong'] = {}
    else:
        blong.data[0].pop('email')
        bottom['bottomlong'] = blong.data
  
    bottomshortdb = BottomShort.objects.filter(email=session.email)
    bshort = BottomShortSerializer(bottomshortdb, many=True) 
    if not bool(bshort.data):
        bottom['bottomshort'] = {}
    else:
        bshort.data[0].pop('email')
        bottom['bottomshort'] = bshort.data
    result['bottom'] = bottom

    dressdb = Dress.objects.filter(email=session.email)
    dre = DressSerializer(dressdb, many=True)
    if not bool(dre.data):
        dress['dress'] = {}
    else:
        dre.data[0].pop('email')
        dress['dress'] = dre.data
    result['dress'] = dress
    return JsonResponse({'status':'true', 'items': result}, safe=False)



@api_view(['POST'])
def item_update(request):
    item_info = JSONParser().parse(request)
    comment = {}
    for i in range(len(upcheck)):
        if upcheck[i] not in item_info:
            comment[upcheck[i]] = ["This field is required"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['token'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    
    item_info['email'] = item_info.pop('token')
    item_info['email'] = session.email
    
    def replace(x, y):
        x.name = y['name']
        x.brand = y['brand']
        x.color = y['color']
        x.descript = y['descript']
        x.save()
        return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)

    def outerinsert(x, sel, y):
        if x in sel:
            othick_serializer = OuterThickSerializer(data=y)
            if othick_serializer.is_valid():
                othick_serializer.save()
                return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'status': 'false', 'message': othick_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            othin_serializer = OuterThinSerializer(data=y)
            if othin_serializer.is_valid():
                othin_serializer.save()
                return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'status': 'false', 'message': othin_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def topinsert(x, sel, y):
        if x in sel:
            tlong_serializer = TopLongSerializer(data=y)
            if tlong_serializer.is_valid():
                tlong_serializer.save()
                return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'status': 'false', 'message': tlong_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            tshort_serializer = TopShortSerializer(data=y)
            if tshort_serializer.is_valid():
                tshort_serializer.save()
                return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'status': 'false', 'message': tshort_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def bottominsert(x, sel,  y):
        if x in sel:
            bshort_serializer = BottomShortSerializer(data=y)
            if bshort_serializer.is_valid():
                bshort_serializer.save()
                return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'status': 'false', 'message': bshort_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            blong_serializer = BottomLongSerializer(data=y)
            if blong_serializer.is_valid():
                blong_serializer.save()
                return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'status': 'false', 'message': blong_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def onepieceinsert(y):
        dress_serializer = DressSerializer(data=y)
        if dress_serializer.is_valid():
            dress_serializer.save()
            return JsonResponse({'status': 'true'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'status': 'false', 'message': dress_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    if item_info['category'] == 'outer':
        if item_info['subcategory'] in othick:
            try:
                items = OuterThick.objects.get(id=item_info['id'], email=session.email)
            except OuterThick.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
                
            if item_info['category'] != item_info['categoryNew']:
                items.delete()
                if item_info['categoryNew'] == 'outer':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
                if item_info['categoryNew'] == 'top':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                if item_info['categoryNew'] == 'bottom':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                if item_info['categoryNew'] == 'onepiece':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return onepieceinsert(item_info)
                
            if item_info['subcategory'] == item_info['subcategoryNew']:
                return replace(items, item_info)
            
            elif item_info['subcategory'] != item_info['subcategoryNew']:
                if item_info['subcategoryNew'] in othick:
                    items.subcategory = item_info['subcategoryNew']
                    return replace(items, item_info)
                else:
                    items.delete()
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
        else:
            try:
                items = OuterThin.objects.get(id=item_info['id'], email=session.email)
            except OuterThin.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)            
            
            if item_info['category'] != item_info['categoryNew']:
                items.delete()
                if item_info['categoryNew'] == 'outer':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
                if item_info['categoryNew'] == 'top':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                if item_info['categoryNew'] == 'bottom':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                if item_info['categoryNew'] == 'onepiece':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return onepieceinsert(item_info)

            if item_info['subcategory'] == item_info['subcategoryNew']:
                return replace(items, item_info)
            elif item_info['subcategory'] != item_info['subcategoryNew']:
                if item_info['subcategoryNew'] in othick:
                    items.delete()
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(items_info['subcategory'], othick, item_info)
                else:
                    items.subcategory = item_info['subcategoryNew']
                    return replace(items, item_info)


    elif item_info['category'] == 'top':
        if item_info['subcategory'] in tlong:
            try:
                items = TopLong.objects.get(id=item_info['id'], email=session.email)
            except TopLong.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            
            if item_info['category'] != item_info['categoryNew']:
                items.delete()
                if item_info['categoryNew'] == 'outer':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
                if item_info['categoryNew'] == 'top':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                if item_info['categoryNew'] == 'bottom':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                if item_info['categoryNew'] == 'onepiece':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return onepieceinsert(item_info)

            if item_info['subcategory'] == item_info['subcategoryNew']:
                return replace(items, item_info)

            elif item_info['subcategory'] != item_info['subcategoryNew']:
                if item_info['subcategoryNew'] in tlong:
                    items.subcategory = item_info['subcategoryNew']
                    return replace(items, item_info)
                else:
                    items.delete()
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)    
            
        else:
            try:
                items = TopShort.objects.get(id=item_info['id'], email=session.email)
            except TopShort.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
           
            if item_info['category'] != item_info['categoryNew']:
                items.delete()
                if item_info['categoryNew'] == 'outer':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
                if item_info['categoryNew'] == 'top':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                if item_info['categoryNew'] == 'bottom':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                if item_info['categoryNew'] == 'onepiece':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return onepieceinsert(item_info)

            if item_info['subcategory'] == item_info['subcategoryNew']:
                return replace(items, item_info)

            elif item_info['subcategory'] != item_info['subcategoryNew']:
                if item_info['subcategoryNew'] in tlong:
                    items.delete()
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                else:
                    items.subcategory = item_info['subcategoryNew']
                    return replace(items, item_info)


    elif item_info['category'] == 'bottom':
        if item_info['subcategory'] in bshort:
            try:
                items = BottomShort.objects.get(id=item_info['id'], email=session.email)
            except BottomShort.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

            if item_info['category'] != item_info['categoryNew']:
                items.delete()
                if item_info['categoryNew'] == 'outer':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
                if item_info['categoryNew'] == 'top':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                if item_info['categoryNew'] == 'bottom':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                if item_info['categoryNew'] == 'onepiece':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return onepieceinsert(item_info)

            if item_info['subcategory'] == item_info['subcategoryNew']:
                return replace(items, item_info)

            elif item_info['subcategory'] != item_info['subcategoryNew']:
                if item_info['subcategoryNew'] in bshort:
                    items.subcategory = item_info['subcategoryNew']
                    return replace(items, item_info)
                else:
                    items.delete()
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)

            
        else:
            try:
                items = BottomLong.objects.get(id=item_info['id'], email=session.email)
            except BottomLong.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            
            if item_info['category'] != item_info['categoryNew']:
                items.delete()
                if item_info['categoryNew'] == 'outer':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return outerinsert(item_info['subcategory'], othick, item_info)
                if item_info['categoryNew'] == 'top':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return topinsert(item_info['subcategory'], tlong, item_info)
                if item_info['categoryNew'] == 'bottom':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                if item_info['categoryNew'] == 'onepiece':
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return onepieceinsert(item_info)

            if item_info['subcategory'] == item_info['subcategoryNew']:
                return replace(items, item_info)

            elif item_info['subcategory'] != item_info['subcategoryNew']:
                if item_info['subcategoryNew'] in bshort:
                    items.delete()
                    item_info['subcategory'] = item_info['subcategoryNew']
                    return bottominsert(item_info['subcategory'], bshort, item_info)
                else:
                    items.subcategory = item_info['subcategoryNew']
                    return replace(items, item_info)

    elif item_info['category'] == 'onepiece':
        try:
            items = Dress.objects.get(id=item_info['id'], email=session.email)
        except Dress.DoesNotExist:
            comment['id'] = ["item not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
        
        if item_info['category'] != item_info['categoryNew']:
            items.delete()
            if item_info['categoryNew'] == 'outer':
                item_info['subcategory'] = item_info['subcategoryNew']
                return outerinsert(item_info['subcategory'], othick, item_info)
            if item_info['categoryNew'] == 'top':
                item_info['subcategory'] = item_info['subcategoryNew']
                return topinsert(item_info['subcategory'], tlong, item_info)
            if item_info['categoryNew'] == 'bottom':
                item_info['subcategory'] = item_info['subcategoryNew']
                return bottominsert(item_info['subcategory'], bshort, item_info)
            if item_info['categoryNew'] == 'onepiece':
                item_info['subcategory'] = item_info['subcategoryNew']
                return onepieceinsert(item_info)

        else:
            items.subcategory = item_info['subcategoryNew']
            return replace(items, item_info)
    
    else:
        comment['category'] = ["Wrong category name"]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])          # num, category, token
def item_delete(request):
    item_info = JSONParser().parse(request)
    comment = {}
    for i in range(len(delcheck)):
        if delcheck[i] not in item_info:
            comment[delcheck[i]] = ["This field is required"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

    try:
        session = Token.objects.get(token=item_info['token'])
    except Token.DoesNotExist:
            comment['token'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

    if item_info['category'] == 'outer':
        if item_info['subcategory'] in othick:
            try:
                items = OuterThick.objects.filter(id=item_info['id'], email=session.email)
            except OuterThick.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            items.delete()
            return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)
        else:
            try:
                items = OuterThin.objects.filter(id=item_info['id'], email=session.email)
            except OuterThin.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            items.delete()
            return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)

 
    if item_info['category'] == 'top':
        if item_info['subcategory'] in tlong:
            try:
                items = TopLong.objects.filter(id=item_info['id'], email=session.email)
            except TopLong.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            items.delete()
            return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)
        else:
            try:
                items = TopShort.objects.filter(id=item_info['id'], email=session.email)
            except TopShort.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            items.delete()
            return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT) 

    if item_info['category'] == 'bottom':
        if item_info['subcategory'] in bshort:
            try:
                items = BottomShort.objects.filter(id=item_info['id'], email=session.email)
            except BottomShort.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            items.delete()
            return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)
        else:
            try:
                items = BottomLong.objects.filter(id=item_info['id'], email=session.email)
            except BottomLong.DoesNotExist:
                comment['id'] = ["item not present"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            items.delete()
            return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)
 
    if item_info['category'] == 'onepiece':
        try:
            items = Dress.objects.filter(id=item_info['id'], email=session.email)
        except Dress.DoesNotExist:
            comment['id'] = ["item not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
        items.delete()
        return JsonResponse({'status':'true'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def item_get_all(request):
    item_info = JSONParser().parse(request)
    user = {}
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
        user_in = Account.objects.get(email=session.email)
    except Token.DoesNotExist:
        comment['email'] = ["account not present"]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST) 
    
    user['email'] = user_in.email
    user['nickname'] = user_in.nickname
    user['sex'] = user_in.sex

    outerthickdb = OuterThick.objects.filter(email=session.email)
    othick = OuterThickSerializer(outerthickdb, many=True)
    if not bool(othick.data):
        outer['outerthick'] = {}
    else:
        othick.data[0].pop('email')
        outer['outerthick'] = othick.data

    outerthindb = OuterThin.objects.filter(email=session.email)
    othin = OuterThinSerializer(outerthindb, many=True)
    if not bool(othin.data):
        outer['outerthin'] = {}
    else:
        othin.data[0].pop('email')
        outer['outerthin'] = othin.data
    result['outer'] = outer




    toplongdb = TopLong.objects.filter(email=session.email)
    tlong = TopLongSerializer(toplongdb, many=True)
    if not bool(tlong.data):
        top['toplong'] = {}
    else:
        tlong.data[0].pop('email')
        top['toplong'] = tlong.data

    topshortdb = TopShort.objects.filter(email=session.email)
    tshort = TopShortSerializer(topshortdb, many=True)
    if not bool(tshort.data):
        top['topshort'] = {}
    else:
        tshort.data[0].pop('email')
        top['topshort'] = tshort.data
    result['top'] = top



    bottomlongdb = BottomLong.objects.filter(email=session.email)
    blong = BottomLongSerializer(bottomlongdb, many=True)
    if not bool(blong.data):
        bottom['bottomlong'] = {}
    else:
        blong.data[0].pop('email')
        bottom['bottomlong'] = blong.data

    bottomshortdb = BottomShort.objects.filter(email=session.email)
    bshort = BottomShortSerializer(bottomshortdb, many=True)
    if not bool(bshort.data):
        bottom['bottomshort'] = {}
    else:
        bshort.data[0].pop('email')
        bottom['bottomshort'] = bshort.data
    result['bottom'] = bottom

    dressdb = Dress.objects.filter(email=session.email)
    dre = DressSerializer(dressdb, many=True)
    if not bool(dre.data):
        dress['dress'] = {}
    else:
        dre.data[0].pop('email')
        dress['dress'] = dre.data
    result['dress'] = dress
    return JsonResponse({'status':'true', 'user': user, 'items': result}, safe=False)

