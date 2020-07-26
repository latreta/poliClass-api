from rest_framework.serializers import ModelSerializer

from blocos.models import Bloco


class BlocoSerializer(ModelSerializer):
    class Meta:
        model = Bloco
        fields = ['id', 'name']
