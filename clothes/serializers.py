from rest_framework import serializers
from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress

class OuterThickSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterThick
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

class OuterThinSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterThin
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

class TopLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopLong
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

class TopShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopShort
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

class BottomLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomLong
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

class BottomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomShort
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ('name',
                  'color',
                  'category',
                  'url',
                  'descript',
                  'brand',
                  'email')

