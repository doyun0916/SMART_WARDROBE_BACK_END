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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

class MuniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manunique
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

class MworkwearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manworkwear
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

# woman styles


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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

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
                  'url')

class WcampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wocampus
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

class WuniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wounique
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

class WworkwearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woworkwear
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

class WminimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wominimal
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

class WdandySerializer(serializers.ModelSerializer):
    class Meta:
        model = Wodandy
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')

