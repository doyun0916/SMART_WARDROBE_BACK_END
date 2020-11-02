from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress
from clothes.serializers import OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer, DressSerializer
from coordi.models import Mcasual, Mcampus, Mminimal, Mstreet, Mtravel, Msports, Mformal, Mdandy, Wsports, Wcasual, Wformal, Wromantic, Wgirlish, Wstreet, Wfeminine, Wtravel
from coordi.serializers import McasualSerializer, McampusSerializer, MminimalSerializer, MstreetSerializer, MtravelSerializer, MsportsSerializer, MformalSerializer, MdandySerializer, MuniqueSerializer, MworkwearSerializer, WsportsSerializer, WcasualSerializer, WformalSerializer, WromanticSerializer, WgirlishSerializer, WstreetSerializer, WfeminineSerializer, WtravelSerializer, WcampusSerializer, WuniqueSerializer, WworkwearSerializer, WminimalSerializer, WdandySerializer
from restApi.models import Token
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.utils import timezone


othik = ['coat', 'coat fur', 'parka']
othin = ['cardigan', 'blazer', 'bomber', 'denim', 'leather', 'trench coat', 'vest']
tlong = ['long blouse', 'long shirt', 'long tee', 'hoodie', 'sweater', 'turtleneck']
tshort = ['short blouse', 'short shirt', 'short tee', 'sling']
blong = ['long skirt', 'jeans', 'sweatpants', 'chinos', 'leggings']
bshort = ['short skirt', 'denim shorts', 'shorts']
onepiece = ['long dress', 'short dress', 'sling dress', 'vest dress', 'jumpsuit', 'romper']
# temp = ['very hot', 'hot', 'warm', 'cool', 'cold', 'very cold']

@api_view(['POST'])
def coordination(request):
    user_info = JSONParser().parse(request)
    comment = {}
    if "token" not in user_info:
        comment['token'] = ["This field is required."]
        return JsonResponse({'status': 'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    try:
        session = Token.objects.get(token=user_info['token'])
    except Token.DoesNotExist:
            comment['token'] = ["user not present"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

    final_list=[]
    def recommend(temperature, obj):
        if temperature >= 23:
            style_set = obj.objects.filter(outer__isnull=True,top__in=tshort,bottom__in=bshort,dress__isnull=True).values()[0:5]
            for style in style_set:
                final_dict={}
                myclothes_list=[]
                t_list=TopShort.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                # if not t_list:
                #     comment['token'] = ["There is no item recommended"]
                #     return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
                t=TopShortSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomShortSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 23 and temperature >= 20:
            style_set1 = obj.objects.filter(outer__isnull=True,top__in=tshort,bottom__in=blong,dress__isnull=True).values()[0:5]
            style_set2 = obj.objects.filter(outer__isnull=True,top__in=tlong,bottom__in=bshort,dress__isnull=True).values()[0:5]
            style_set3 = obj.objects.filter(outer__isnull=True,top__isnull=True,bottom__isnull=True,dress__in=onepiece).values()[0:5]
            for style in style_set1:
                final_dict={}
                myclothes_list=[]
                t_list=TopShort.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopShortSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            for style in style_set2:
                final_dict={}
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomShortSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            for style in style_set3:
                final_dict={}
                myclothes_list=[]
                d_list=Dress.objects.filter(email=session.email, color=style['dresscol'], subcategory=style['dress']).order_by("?")
                d=DressSerializer(d_list,many=True)
                myclothes_list+=d.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 20 and temperature >= 17:
            style_set = obj.objects.filter(outer__isnull=True,top__in=tlong,bottom__in=blong,dress__isnull=True).values()[0:5]
            for style in style_set:
                final_dict={}
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
            """
            for i in range(2):
                final_dict={}
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, subcategory='long shirt').order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']='url'
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
            """
        elif temperature < 17 and temperature >= 12:
            style_set1 = obj.objects.filter(outer__in=othin,top__in=tlong,bottom__in=blong,dress__isnull=True).values()[0:5]
            style_set2 = obj.objects.filter(outer__isnull=True,top__in=tlong,bottom__in=blong,dress__isnull=True).values()[0:5]
            for style in style_set1:
                final_dict={}
                myclothes_list=[]
                o_list=OuterThin.objects.filter(email=session.email, color=style['outercol'], subcategory=style['outer']).order_by("?")
                o=OuterThinSerializer(o_list,many=True)
                myclothes_list+=o.data[0:1]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            for style in style_set2:
                final_dict={}
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 12 and temperature >= 9:
            style_set = obj.objects.filter(outer__in=othin,top__in=tlong,bottom__in=blong,dress__isnull=True).values()[0:5]
            for style in style_set:
                final_dict={}
                myclothes_list=[]
                o_list=OuterThin.objects.filter(email=session.email, color=style['outercol'], subcategory=style['outer']).order_by("?")
                o=OuterThinSerializer(o_list,many=True)
                myclothes_list+=o.data[0:1]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 9:
            style_set = obj.objects.filter(outer__in=othick,top__in=tlong,bottom__in=blong,dress__isnull=True).values()[0:5]
            for style in style_set:
                final_dict={}
                myclothes_list=[]
                o_list=OuterThick.objects.filter(email=session.email, color=style['outercol'], subcategory=style['outer']).order_by("?")
                o=OuterThickSerializer(o_list,many=True)
                myclothes_list+=o.data[0:1]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        else:
            comment['temp'] = ["Wrong temperature"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

    if user_info['sex'] == 'male':
        if user_info['style'] == 'campus':
            return recommend(user_info['temp'],Mcampus)
        elif user_info['style'] == 'casual':
            return recommend(user_info['temp'],Mcasual)
        elif user_info['style'] == 'dandy':
            return recommend(user_info['temp'],Mdandy)
        elif user_info['style'] == 'formal':
            return recommend(user_info['temp'],Mformal)
        elif user_info['style'] == 'minimal':
            return recommend(user_info['temp'],Mminimal)
        elif user_info['style'] == 'sports':
            return recommend(user_info['temp'],Msports)
        elif user_info['style'] == 'street':
            return recommend(user_info['temp'],Mstreet)
        elif user_info['style'] == 'travel':
            return recommend(user_info['temp'],Mtravel)
        elif user_info['style'] == 'unique':
            return recommend(user_info['temp'],Munique)
        elif user_info['style'] == 'workwear':
            return recommend(user_info['temp'],Mworkwear)
        else:
            comment['style'] = ["Wrong style name"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    elif user_info['sex'] == 'female':
        if user_info['style'] == 'campus':
            return recommend(user_info['temp'],Wcampus)
        elif user_info['style'] == 'casual':
            return recommend(user_info['temp'],Wcasual)
        elif user_info['style'] == 'dandy':
            return recommend(user_info['temp'],Wdandy)
        elif user_info['style'] == 'formal':
            return recommend(user_info['temp'],Wformal)
        elif user_info['style'] == 'minimal':
            return recommend(user_info['temp'],Wminimal)
        elif user_info['style'] == 'sports':
            return recommend(user_info['temp'],Wsports)
        elif user_info['style'] == 'street':
            return recommend(user_info['temp'],Wstreet)
        elif user_info['style'] == 'travel':
            return recommend(user_info['temp'],Wtravel)
        elif user_info['style'] == 'unique':
            return recommend(user_info['temp'],Wunique)
        elif user_info['style'] == 'workwear':
            return recommend(user_info['temp'],Wworkwear)
        elif user_info['style'] == 'girlish':
            return recommend(user_info['temp'],Wgirlish)
        elif user_info['style'] == 'feminine':
            return recommend(user_info['temp'],Wfeminine)
        elif user_info['style'] == 'romantic':
            return recommend(user_info['temp'],Wromantic)
        else:
            comment['style'] = ["Wrong style name"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    else:
        comment['sex'] = ["Wrong sex"]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

