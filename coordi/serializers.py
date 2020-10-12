from rest_framework import serializers
from coordi.models import Mancasual

class McasualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancasual                           
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class McampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancampus
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class MminimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manminimal
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class MstreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manstreet
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class MtravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantravel
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class MsportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mansports
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class MformalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manformal
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class MdandySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandandy
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WsportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wosports
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WcasualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wocasual
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WformalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woformal
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WromanticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woromantic
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WgirlishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wogirlish
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WstreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wostreet
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WfeminineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wofeminine
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

class WtravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wotravel
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'imgurl')

