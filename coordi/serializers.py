from rest_framework import serializers
from coordi.models import Mancasual

class CoordiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancasual
        fields = ('outer',
                  'outercol',
                  'top',
                  'topcol',
                  'bottom',
                  'bottomcol',
                  'imgurl')

