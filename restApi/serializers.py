from rest_framework import serializers
from restApi.models import Account, EmailCheck, Token

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email',
                  'pw',
                  'nickname',
                  'sex')

class EmailcheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCheck
        fields =('email',
                 'code')

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('email',
                  'token')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email',
                  'pw')
