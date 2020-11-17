from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress
from clothes.serializers import OuterThickSerializer, OuterThinSerializer, TopLongSerializer, TopShortSerializer, BottomLongSerializer, BottomShortSerializer, DressSerializer
from coordi.models import Mcasual, Mcampus, Mminimal, Mstreet, Mtravel, Msports, Mformal, Mdandy, Munique, Mworkwear, Wcampus, Wsports, Wcasual, Wformal, Wromantic, Wgirlish, Wstreet, Wfeminine, Wtravel, Wunique, Wworkwear, Wminimal, Wdandy
from coordi.serializers import McasualSerializer, McampusSerializer, MminimalSerializer, MstreetSerializer, MtravelSerializer, MsportsSerializer, MformalSerializer, MdandySerializer, MuniqueSerializer, MworkwearSerializer, WsportsSerializer, WcasualSerializer, WformalSerializer, WromanticSerializer, WgirlishSerializer, WstreetSerializer, WfeminineSerializer, WtravelSerializer, WcampusSerializer, WuniqueSerializer, WworkwearSerializer, WminimalSerializer, WdandySerializer
from restApi.models import Account, Token
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.utils import timezone
import random

othik = ['coat', 'coat fur', 'parka']
othin = ['cardigan', 'blazer', 'bomber', 'denim', 'leather', 'trench coat', 'vest']
tlong = ['long blouse', 'long shirt', 'long tee', 'sweater', 'turtleneck']
tshort = ['short blouse', 'short shirt', 'short tee', 'sling']
blong = ['long skirt', 'jeans', 'sweatpants', 'chinos', 'leggings']
bshort = ['short skirt', 'denim shorts', 'shorts']
onepiece = ['long dress', 'short dress', 'sling dress', 'vest dress', 'jumpsuit', 'romper']
all_clothes = othik+othin+tlong+tshort+blong+bshort+onepiece

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
    account = Account.objects.get(email=session.email)
    sex = account.sex
    final_list=[]
    def recommend(temperature, obj):
        if temperature >= 23:
            style_set = obj.objects.filter(outer='',top__in=tshort,bottom__in=bshort,dress='').order_by("?").values()[0:5]
            for style in style_set:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                t_list=TopShort.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopShort.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopShort.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopShortSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomShort.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomShortSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 23 and temperature >= 20:
            style_set1 = obj.objects.filter(outer='',top__in=tshort,bottom__in=blong,dress='').order_by("?").values()[0:5]
            style_set2 = obj.objects.filter(outer='',top__in=tlong,bottom__in=bshort,dress='').order_by("?").values()[0:5]
            style_set3 = obj.objects.filter(outer='',top='',bottom='',dress__in=onepiece).order_by("?").values()[0:5]
            for style in style_set1:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                t_list=TopShort.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopShort.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopShort.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopShortSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            for style in style_set2:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopLong.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomShort.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomShort.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomShortSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            for style in style_set3:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                d_list=Dress.objects.filter(email=session.email, color=style['dresscol'], subcategory=style['dress']).order_by("?")
                if not d_list:
                    d_list=Dress.objects.filter(email=session.email, color=style['dresscol']).order_by("?")
                    if not d_list:
                        d_list=Dress.objects.filter(email=session.email).order_by("?")
                        if not d_list:
                            myclothes_list.append('There is no onepiece recommended')
                d=DressSerializer(d_list,many=True)
                myclothes_list+=d.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 20 and temperature >= 17:
            style_set = obj.objects.filter(outer='',top__in=tlong,bottom__in=blong,dress='').order_by("?").values()[0:5]
            for style in style_set:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopLong.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
            """
            for i in range(1):
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, subcategory='long tee').order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email).order_by("?") # 중분류 같은 옷
                    if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, subcategory='chinos').order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email).order_by("?") # 중분류 같은 옷
                    if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']='url'
                final_dict['itemList']+=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        """
        elif temperature < 17 and temperature >= 12:
            style_set1 = obj.objects.filter(outer__in=othin,top__in=tlong,bottom__in=blong,dress='').order_by("?").values()[0:5]
            style_set2 = obj.objects.filter(outer='',top__in=tlong,bottom__in=blong,dress='').order_by("?").values()[0:5]
            for style in style_set1:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                o_list=OuterThin.objects.filter(email=session.email, color=style['outercol'], subcategory=style['outer']).order_by("?")
                if not o_list:
                    o_list=OuterThin.objects.filter(email=session.email, color=style['outercol']).order_by("?")
                    if not o_list:
                        # o_list=OuterThin.objects.filter(email=session.email).order_by("?")
                        # if not o_list:
                        myclothes_list.append('There is no outer recommended')
                o=OuterThinSerializer(o_list,many=True)
                myclothes_list+=o.data[0:1]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopLong.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            for style in style_set2:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopLong.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 12 and temperature >= 9:
            style_set = obj.objects.filter(outer__in=othin,top__in=tlong,bottom__in=blong,dress='').order_by("?").values()[0:5]
            for style in style_set:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                o_list=OuterThin.objects.filter(email=session.email, color=style['outercol'], subcategory=style['outer']).order_by("?")
                if not o_list:
                    o_list=OuterThin.objects.filter(email=session.email, color=style['outercol']).order_by("?")
                    if not o_list:
                        # o_list=OuterThin.objects.filter(email=session.email).order_by("?")
                        # if not o_list:
                        myclothes_list.append('There is no outer recommended')
                o=OuterThinSerializer(o_list,many=True)
                myclothes_list+=o.data[0:1]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopLong.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        elif temperature < 9:
            style_set = obj.objects.filter(outer__in=othik,top__in=tlong,bottom__in=blong).order_by("?").values()[0:5]
#            style_set = obj.objects.filter(outer='parka').order_by("?").values()[0:5]
            for style in style_set:
                final_dict={}
                final_dict['recommendImageURL']=[]
                final_dict['itemList']=[]
                myclothes_list=[]
                o_list=OuterThick.objects.filter(email=session.email, color=style['outercol'], subcategory=style['outer']).order_by("?")
                if not o_list:
                    o_list=OuterThick.objects.filter(email=session.email, color=style['outercol']).order_by("?")
                    if not o_list:
                        # o_list=OuterThick.objects.filter(email=session.email).order_by("?")
                        # if not o_list:
                        myclothes_list.append('There is no outer recommended')
                o=OuterThickSerializer(o_list,many=True)
                myclothes_list+=o.data[0:1]
                t_list=TopLong.objects.filter(email=session.email, color=style['topcol'], subcategory=style['top']).order_by("?")
                if not t_list:
                    t_list=TopLong.objects.filter(email=session.email, color=style['topcol']).order_by("?")
                    if not t_list:
                        # t_list=TopLong.objects.filter(email=session.email).order_by("?")
                        # if not t_list:
                        myclothes_list.append('There is no top recommended')
                t=TopLongSerializer(t_list,many=True)
                myclothes_list+=t.data[0:1]
                b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol'], subcategory=style['bottom']).order_by("?")
                if not b_list:
                    b_list=BottomLong.objects.filter(email=session.email, color=style['bottomcol']).order_by("?")
                    if not b_list:
                        # b_list=BottomLong.objects.filter(email=session.email).order_by("?")
                        # if not b_list:
                        myclothes_list.append('There is no bottom recommended')
                b=BottomLongSerializer(b_list,many=True)
                myclothes_list+=b.data[0:1]
                final_dict['recommendImageURL']=style['url']
                final_dict['itemList']=myclothes_list
                final_list.append(final_dict)
            return JsonResponse(final_list,safe=False)
        else:
            comment['temp'] = ["Wrong temperature"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

    if sex == 'male':
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
    elif sex == 'female':
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

@api_view(['POST'])
def coordination_myclothes(request):
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
    account = Account.objects.get(email=session.email)
    sex = account.sex
    mstyle_list = ['campus', 'casual', 'dandy', 'formal', 'minimal', 'sports', 'street', 'travel', 'unique', 'workwear']
    wstyle_list = ['campus', 'casual', 'dandy', 'formal', 'minimal', 'sports', 'street', 'travel', 'unique', 'workwear', 'girlish', 'feminine', 'romantic']
    url_list=[]
    if not user_info['subcategory'] in all_clothes:
        comment['subcategory'] = ["Wrong subcategory"]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    def recommend_myclothes(my_color, my_subcate, obj, objsrlz):
        if my_subcate in othik:
            style_set = obj.objects.filter(outer=my_subcate,outercol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(outer__in=othik,outercol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(outer__in=othik).order_by("?")
#                    o=objsrlz(style_set,many=True)
#                    url_list.append('url')
        elif my_subcate in othin:
            style_set = obj.objects.filter(outer=my_subcate,outercol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(outer__in=othin,outercol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(outer__in=othin).order_by("?")
#                    o=objsrlz(style_set,many=True)
        elif my_subcate in tlong:
            style_set = obj.objects.filter(top=my_subcate,topcol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(top__in=tlong,topcol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(top__in=tlong).order_by("?")
#                    o=objsrlz(style_set,many=True)
        elif my_subcate in tshort:
            style_set = obj.objects.filter(top=my_subcate,topcol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(top__in=tshort,topcol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(top__in=tshort).order_by("?")
#                    o=objsrlz(style_set,many=True)
        elif my_subcate in blong:
            style_set = obj.objects.filter(bottom=my_subcate,bottomcol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(bottom__in=blong,bottomcol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(bottom__in=blong).order_by("?")
#                    o=objsrlz(style_set,many=True)
        elif my_subcate in bshort:
            style_set = obj.objects.filter(bottom=my_subcate,bottomcol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(bottom__in=bshort,bottomcol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(bottom__in=bshort).order_by("?")
#                    o=objsrlz(style_set,many=True)
        elif my_subcate in onepiece:
            style_set = obj.objects.filter(dress=my_subcate,dresscol=my_color).order_by("?")
            o=objsrlz(style_set,many=True)
            if o.data:
                url_list.append(o.data[0]['url'])
#            if not o.data:
#                style_set = obj.objects.filter(dress__in=onepiece,dresscol=my_color).order_by("?")
#                o=objsrlz(style_set,many=True)
#                if not o.data:
#                    style_set = obj.objects.filter(dress__in=onepiece).order_by("?")
#                    o=objsrlz(style_set,many=True)
        else:
            comment['subcategory'] = ["Wrong subcategory"]
            return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
    if sex == 'male':
        for i in range(1000):
        # while len(url_list)<5:
            a=random.randrange(0,len(mstyle_list))
            style=mstyle_list[a]
            if style == 'campus':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mcampus,McampusSerializer)
            elif style == 'casual':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mcasual,McasualSerializer)
            elif style == 'dandy':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mdandy,MdandySerializer)
            elif style == 'formal':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mformal,MformalSerializer)
            elif style == 'minimal':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mminimal,MminimalSerializer)
            elif style == 'sports':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Msports,MsportsSerializer)
            elif style == 'street':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mstreet,MstreetSerializer)
            elif style == 'travel':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mtravel,MtravelSerializer)
            elif style == 'unique':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Munique,MuniqueSerializer)
            elif style == 'workwear':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Mworkwear,MworkwearSerializer)
            else:
                comment['style'] = ["Wrong style name"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            url_set = set(url_list)
            url_list = list(url_set)
            if len(url_list)>=5:
                return JsonResponse(url_list,safe=False)
        if not url_list:
            url_list.append('There is no image recommended')
        return JsonResponse(url_list,safe=False)
    elif sex == 'female':
        for i in range(1000):
        # while len(url_list)<5:
            a=random.randrange(0,len(wstyle_list))
            style=wstyle_list[a]
            if style == 'campus':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wcampus,WcampusSerializer)
            elif style == 'casual':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wcasual,WcasualSerializer)
            elif style == 'dandy':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wdandy,WdandySerializer)
            elif style == 'formal':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wformal,WformalSerializer)
            elif style == 'minimal':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wminimal,WminimalSerializer)
            elif style == 'sports':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wsports,WsportsSerializer)
            elif style == 'street':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wstreet,WstreetSerializer)
            elif style == 'travel':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wtravel,WtravelSerializer)
            elif style == 'unique':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wunique,WuniqueSerializer)
            elif style == 'workwear':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wworkwear,WworkwearSerializer)
            elif style == 'girlish':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wgirlish,WgirlishSerializer)
            elif style == 'feminine':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wfeminine,WfeminineSerializer)
            elif style == 'romantic':
                recommend_myclothes(user_info['color'],user_info['subcategory'],Wromantic,WromanticSerializer)
            else:
                comment['style'] = ["Wrong style name"]
                return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)
            url_set = set(url_list)
            url_list = list(url_set)
            if len(url_list)>=5:
                return JsonResponse(url_list,safe=False)
        if not url_list:
            url_list.append('There is no image recommended')
        return JsonResponse(url_list,safe=False)
    else:
        comment['sex'] = ["Wrong sex"]
        return JsonResponse({'status':'false', 'message': comment}, status=status.HTTP_400_BAD_REQUEST)

