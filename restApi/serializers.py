from rest_framework import serializers
from restApi.models import Account, EmailCheck

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email',
                  'pw',
                  'nickname')

class EmailcheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCheck
        fields =('email',
                 'code')

