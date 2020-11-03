from rest_framework import serializers
from clothes.models import OuterThick, OuterThin, TopLong, TopShort, BottomLong, BottomShort, Dress

class Item(serializers.ModelSerializer):
    class Meta:
        model = OuterThick
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand'
                  )
class OuterThickSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterThick
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

class OuterThinSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterThin
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

class TopLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopLong
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

class TopShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopShort
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

class BottomLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomLong
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

class BottomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomShort
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ('id',
                  'name',
                  'color',
                  'subcategory',
                  'url',
                  'descript',
                  'brand',
                  'email')

