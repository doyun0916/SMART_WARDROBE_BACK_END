from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress
from clothes.serializers import OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer, DressSerializer
from coordi.models import Mcasual, Mcampus, Mminimal, Mstreet, Mtravel, Msports, Mformal, Mdandy, Munique, Mworkwear, Wsports, Wcasual, Wformal, Wromantic, Wgirlish, Wstreet, Wfeminine, Wtravel, Wcampus, Wunique, Wworkwear, Wminimal, Wdandy
from coordi.serializers import McasualSerializer, McampusSerializer, MminimalSerializer, MstreetSerializer, MtravelSerializer, MsportsSerializer, MformalSerializer, MdandySerializer, MuniqueSerializer, MworkwearSerializer, WsportsSerializer, WcasualSerializer, WformalSerializer, WromanticSerializer, WgirlishSerializer, WstreetSerializer, WfeminineSerializer, WtravelSerializer, WcampusSerializer, WuniqueSerializer, WworkwearSerializer, WminimalSerializer, WdandySerializer
from restApi.models import Token
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.utils import timezone
from django.db.models import F


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

    recommend_list={}   #나중에 삭제하기
    final_list=[]
    def recommend(temperature, obj):
        if temperature >= 23:
            style_set = obj.objects.filter(outer__isnull=True,top__in=tshort,bottom__in=bshort,dress__isnull=True).values()
            for style in style_set:
                myclothes_list=[]
                t_list=TopShort.objects.filter(email=session.email, color=style['topcol'])
                t=TopShortSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomShortSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list   #{'url주소':리스트} 형태로 반환됨
            return JsonResponse({'recommendList':recommend_list})
        elif temperature < 23 and temperature >= 20:
            style_set1 = obj.objects.filter(outer__isnull=True,top__in=tshort,bottom__in=blong,dress__isnull=True).values()
            style_set2 = obj.objects.filter(outer__isnull=True,top__in=tlong,bottom__in=bshort,dress__isnull=True).values()
            style_set3 = obj.objects.filter(outer__isnull=True,top__isnull=True,bottom__isnull=True,dress__in=onepiece).values()
            for style in style_set1:
                myclothes_list=[]
                t_list=TopShort.objects.filter(email=session.email, color=style['topcol'])
                t=TopShortSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list
            for style in style_set2:
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'])
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomShortSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list
            for style in style_set3:
                myclothes_list=[]
                d_list=Dress.objects.filter(email=session.email, color=style['dresscol'])
                d=DressSerializer(d_list,many=True)
                myclothes_list+=d.data
                recommend_list[style['url']]=myclothes_list
            return JsonResponse({'recommendList':recommend_list})
        elif temperature < 20 and temperature >= 17:
#            style_set = obj.objects.filter(outer__isnull=True,top__in=tlong,bottom__in=blong,dress__isnull=True).values()  #5개만 뽑기
#            for style in style_set:
#                final_dict={}
#                myclothes_list=[]
#                t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
#                t=TopLongSerializer(t_list,many=True)
#                myclothes_list+=t.data[0:1]
#                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
#                b=BottomLongSerializer(b_list,many=True)
#                myclothes_list+=b.data[0:1]
#                final_dict['recommendImageURL']=style['url']
#                final_dict['itemList']=myclothes_list
#                final_list.append(final_dict)
#            return JsonResponse(final_list,safe=False)
            final_dict={}
            myclothes_list=[]
            t_list=TopLong.objects.filter(email=session.email).order_by("?")
            t=TopLongSerializer(t_list,many=True)
            myclothes_list+=t.data[0:1]
            b_list=BottomLong.objects.filter(email=session.email).order_by("?")
            b=BottomLongSerializer(b_list,many=True)
            myclothes_list+=b.data[0:1]
            final_dict['recommendImageURL']='url'
            final_dict['itemList']=myclothes_list
            final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 17 and temperature >= 12:
            style_set1 = obj.objects.filter(outer__in=othin,top__in=tlong,bottom__in=blong,dress__isnull=True).values()
            style_set2 = obj.objects.filter(outer__isnull=True,top__in=tlong,bottom__in=blong,dress__isnull=True).values()
            for style in style_set1:
                myclothes_list=[]
                o_list=OuterThin.objects.filter(email=session.email, color=style['outercol'])
                o=OuterThinSerializer(o_list,many=True)
                myclothes_list+=o.data
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'])
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list
            for style in style_set2:
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'])
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list
            return JsonResponse({'recommendList':recommend_list})
        elif temperature < 12 and temperature >= 9:
            style_set = obj.objects.filter(outer__in=othin,top__in=tlong,bottom__in=blong,dress__isnull=True).values()
            for style in style_set:
                myclothes_list=[]
                o_list=OuterThin.objects.filter(email=session.email, color=style['outercol'])
                o=OuterThinSerializer(o_list,many=True)
                myclothes_list+=o.data
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'])
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list
            return JsonResponse({'recommendList':recommend_list})
        elif temperature < 9:
            style_set = obj.objects.filter(outer__in=othick,top__in=tlong,bottom__in=blong,dress__isnull=True).values()
            for style in style_set:
                myclothes_list=[]
                o_list=OuterThick.objects.filter(email=session.email, color=style['outercol'])
                o=OuterThickSerializer(o_list,many=True)
                myclothes_list+=o.data
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'])
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'])
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data
                recommend_list[style['url']]=myclothes_list
            return JsonResponse({'recommendList':recommend_list})
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
