from rest_framework import serializers
from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort

class OuterThickSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterThick
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'email')

class OuterThinSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterThin
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'email')

class TopLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopLong
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'email')

class TopShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopShort
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'email')

class BottomLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomLong
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'email')

class BottomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomShort
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'email')
