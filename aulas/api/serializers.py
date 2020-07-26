from rest_framework.serializers import ModelSerializer

from aulas.models import Aula


class AulaSerializer(ModelSerializer):

    class Meta:
        model = Aula
        fields = ['id', 'sala', 'disciplina', 'inicio', 'discente']
