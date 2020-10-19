from rest_framework import serializers
from coordi.models import Mcasual, Mcampus, Mminimal, Mstreet, Mtravel, Msports, Mformal, Mdandy, Munique, Mworkwear, Wcampus, Wsports, Wcasual, Wformal, Wromantic, Wgirlish, Wstreet, Wfeminine, Wtravel, Wunique, Wworkwear, Wminimal, Wdandy

class McasualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcasual
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
        model = Mcampus
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
        model = Mminimal
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
        model = Mstreet
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
        model = Mtravel
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
        model = Msports
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
        model = Mformal
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
        model = Mdandy
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
        model = Munique
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
        model = Mworkwear
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
        model = Wsports
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
        model = Wcasual
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
        model = Wformal
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
        model = Wromantic
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
        model = Wgirlish
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
        model = Wstreet
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
        model = Wfeminine
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
        model = Wtravel
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
        model = Wcampus
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
        model = Wunique
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
        model = Wworkwear
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
        model = Wminimal
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
        model = Wdandy
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'dress',
                  'dresscol',
                  'url')
