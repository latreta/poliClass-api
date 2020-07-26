from rest_framework.serializers import ModelSerializer

from cadeiras.models import Cadeira


class CadeiraSerializer(ModelSerializer):

    class Meta:
        model = Cadeira
        fields = ['id', 'name']
