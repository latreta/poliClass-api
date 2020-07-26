from rest_framework.serializers import ModelSerializer

from blocos.api.serializers import BlocoSerializer
from salas.models import Sala


class SalaSerializer(ModelSerializer):

    class Meta:
        model = Sala
        fields = ['id', 'name', 'bloco']
