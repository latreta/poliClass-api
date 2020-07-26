from rest_framework.serializers import ModelSerializer
from discentes.models import Discente


class DiscenteSerializer(ModelSerializer):

    class Meta:
        model = Discente
        fields = ['id', 'name']
