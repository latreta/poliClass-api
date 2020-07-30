from rest_framework.serializers import ModelSerializer
from docentes.models import Docente


class DocenteSerializer(ModelSerializer):

    class Meta:
        model = Docente
        fields = ['id', 'name']
